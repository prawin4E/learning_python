"""
CAD Drawing Augmentation Pipeline
Inputs : image file + JSON annotation file
Outputs: augmented images + corresponding annotation JSONs in output/

Annotation JSON format accepted (auto-detected):
  COCO  : {"images":[...], "annotations":[...], "categories":[...]}
  Simple: {"annotations":[{"label":"OPEN","bbox":[x1,y1,x2,y2]},...]}
  YOLO-JSON: [{"bbox":[x_c,y_c,w,h],"class":0}, ...]   (normalised 0-1)

Usage:
  python augment.py --image drawing.png --json annotations.json [options]

  --output_dir   output/          where to save results
  --copies       5                augmented copies per technique
  --neg_dir      negatives/       folder of background-only CAD patches
  --seed         42               RNG seed for reproducibility
"""

import argparse
import json
import os
import random
import sys
from pathlib import Path
from typing import Optional

import cv2
import numpy as np
from PIL import Image, ImageFilter


# ─────────────────────────── annotation helpers ───────────────────────────

def load_json(path: str) -> dict | list:
    with open(path) as f:
        return json.load(f)


def save_json(data, path: str):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


class Annotation:
    """Normalised [0-1] bounding box: cx, cy, w, h."""

    def __init__(self, label: str, cx: float, cy: float, w: float, h: float):
        self.label = label
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h

    def to_abs(self, img_w: int, img_h: int):
        """Return (x1, y1, x2, y2) in pixel coords."""
        x1 = int((self.cx - self.w / 2) * img_w)
        y1 = int((self.cy - self.h / 2) * img_h)
        x2 = int((self.cx + self.w / 2) * img_w)
        y2 = int((self.cy + self.h / 2) * img_h)
        return max(0, x1), max(0, y1), min(img_w, x2), min(img_h, y2)

    def to_dict(self) -> dict:
        return {"label": self.label, "cx": self.cx, "cy": self.cy,
                "w": self.w, "h": self.h}

    @classmethod
    def from_abs(cls, label: str, x1, y1, x2, y2, img_w, img_h):
        cx = ((x1 + x2) / 2) / img_w
        cy = ((y1 + y2) / 2) / img_h
        w  = (x2 - x1) / img_w
        h  = (y2 - y1) / img_h
        return cls(label, cx, cy, w, h)


def parse_annotations(raw, img_w: int, img_h: int) -> list[Annotation]:
    """Parse any of the three supported JSON formats into Annotation list."""
    anns: list[Annotation] = []

    # ── COCO format ──────────────────────────────────────────────────
    if isinstance(raw, dict) and "annotations" in raw and "images" in raw:
        cat_map = {c["id"]: c["name"] for c in raw.get("categories", [])}
        for a in raw["annotations"]:
            x, y, bw, bh = a["bbox"]          # COCO: x,y,w,h absolute
            label = cat_map.get(a.get("category_id", 0), "object")
            anns.append(Annotation.from_abs(label, x, y, x + bw, y + bh, img_w, img_h))

    # ── Simple dict format ────────────────────────────────────────────
    elif isinstance(raw, dict) and "annotations" in raw:
        for a in raw["annotations"]:
            bbox  = a["bbox"]
            label = a.get("label", a.get("class", "object"))
            if all(v <= 1.0 for v in bbox):   # already normalised cx,cy,w,h
                anns.append(Annotation(label, *bbox))
            else:                               # absolute x1,y1,x2,y2
                anns.append(Annotation.from_abs(label, *bbox, img_w, img_h))

    # ── YOLO-JSON list format ─────────────────────────────────────────
    elif isinstance(raw, list):
        for a in raw:
            bbox  = a["bbox"]
            label = str(a.get("class", a.get("label", "object")))
            if all(v <= 1.0 for v in bbox):
                anns.append(Annotation(label, *bbox))
            else:
                anns.append(Annotation.from_abs(label, *bbox, img_w, img_h))

    else:
        raise ValueError("Unrecognised annotation JSON format.")

    return anns


# ─────────────────────────── augmentation core ────────────────────────────

class CADAugmentor:
    def __init__(self, rng: random.Random, np_rng: np.random.Generator):
        self.rng    = rng
        self.np_rng = np_rng

    # ── 1. Contextual Paste ───────────────────────────────────────────────

    def contextual_paste(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
        neg_images: list[np.ndarray],
    ) -> tuple[np.ndarray, list[Annotation]]:
        """
        Crop each annotated object, paste it onto a random negative CAD
        patch at a random position that doesn't overlap existing boxes.
        """
        if not neg_images:
            return image, annotations

        h, w = image.shape[:2]
        bg_raw = self.rng.choice(neg_images)
        bg     = cv2.resize(bg_raw, (w, h))
        result = bg.copy()
        placed: list[Annotation] = []

        for ann in annotations:
            x1, y1, x2, y2 = ann.to_abs(w, h)
            crop = image[y1:y2, x1:x2]
            if crop.size == 0:
                continue
            ch, cw = crop.shape[:2]

            # find a non-overlapping placement
            for _ in range(50):
                nx1 = self.rng.randint(0, max(1, w - cw))
                ny1 = self.rng.randint(0, max(1, h - ch))
                nx2, ny2 = nx1 + cw, ny1 + ch
                overlap = any(
                    not (nx2 < p.to_abs(w, h)[0] or nx1 > p.to_abs(w, h)[2] or
                         ny2 < p.to_abs(w, h)[1] or ny1 > p.to_abs(w, h)[3])
                    for p in placed
                )
                if not overlap:
                    break

            result[ny1:ny2, nx1:nx2] = crop
            placed.append(Annotation.from_abs(ann.label, nx1, ny1, nx2, ny2, w, h))

        return result, placed

    # ── 2. CAD-Specific Clutter ───────────────────────────────────────────

    def inject_cad_clutter(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
        n_grid_lines: int = 12,
        n_extra_lines: int = 8,
    ) -> tuple[np.ndarray, list[Annotation]]:
        """Inject orthogonal grid + random solid/dashed/dotted lines."""
        result = image.copy()
        h, w   = result.shape[:2]
        color  = (30, 30, 30) if len(result.shape) == 3 else 30

        # ── orthogonal grid ──────────────────────────────────────
        spacing_x = w // n_grid_lines
        spacing_y = h // n_grid_lines
        for i in range(n_grid_lines):
            x = i * spacing_x + self.rng.randint(-spacing_x // 4, spacing_x // 4)
            cv2.line(result, (x, 0), (x, h), color, 1)
        for j in range(n_grid_lines):
            y = j * spacing_y + self.rng.randint(-spacing_y // 4, spacing_y // 4)
            cv2.line(result, (0, y), (w, y), color, 1)

        # ── title block border ────────────────────────────────────
        cv2.rectangle(result, (5, 5), (w - 5, h - 5), color, 1)

        # ── random structural lines ───────────────────────────────
        line_styles = ["solid", "dashed", "dotted"]
        for _ in range(n_extra_lines):
            style    = self.rng.choice(line_styles)
            vertical = self.rng.random() > 0.5
            if vertical:
                x = self.rng.randint(0, w)
                p1, p2 = (x, 0), (x, h)
            else:
                y = self.rng.randint(0, h)
                p1, p2 = (0, y), (w, y)

            thickness = self.rng.randint(1, 2)
            if style == "solid":
                cv2.line(result, p1, p2, color, thickness)
            else:
                # draw segmented line for dashed/dotted
                seg = 8 if style == "dashed" else 3
                gap = 6 if style == "dashed" else 6
                pts = self._segment_line(p1, p2, seg, gap)
                for (a, b) in pts:
                    cv2.line(result, a, b, color, thickness)

        return result, annotations  # annotations unchanged (lines are background)

    def _segment_line(self, p1, p2, seg_len, gap_len):
        """Yield (start, end) pixel pairs for a dashed/dotted line."""
        x1, y1 = p1
        x2, y2 = p2
        length = max(1, int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5))
        dx, dy = (x2 - x1) / length, (y2 - y1) / length
        segs, i = [], 0
        while i < length:
            sx = int(x1 + dx * i)
            sy = int(y1 + dy * i)
            ex = int(x1 + dx * min(i + seg_len, length))
            ey = int(y1 + dy * min(i + seg_len, length))
            segs.append(((sx, sy), (ex, ey)))
            i += seg_len + gap_len
        return segs

    # ── 3. Morphological Line-Weight Variation ────────────────────────────

    def morphological_variation(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
        operation: Optional[str] = None,   # "dilate" | "erode" | None=random
        kernel_size: int = 2,
    ) -> tuple[np.ndarray, list[Annotation]]:
        """Randomly dilate or erode to simulate line-weight changes."""
        op   = operation or self.rng.choice(["dilate", "erode"])
        k    = np.ones((kernel_size, kernel_size), np.uint8)
        func = cv2.dilate if op == "dilate" else cv2.erode
        return func(image, k, iterations=1), annotations

    # ── 4. Realistic Noise & Artifacts ────────────────────────────────────

    def salt_and_pepper(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
        density: float = 0.02,
    ) -> tuple[np.ndarray, list[Annotation]]:
        result = image.copy()
        total  = image.size // (image.shape[2] if len(image.shape) == 3 else 1)
        n      = int(total * density)
        # salt
        coords = [self.np_rng.integers(0, d, n) for d in image.shape[:2]]
        result[coords[0], coords[1]] = 255
        # pepper
        coords = [self.np_rng.integers(0, d, n) for d in image.shape[:2]]
        result[coords[0], coords[1]] = 0
        return result, annotations

    def jpeg_artifacts(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
        quality: int = None,
    ) -> tuple[np.ndarray, list[Annotation]]:
        """Round-trip through JPEG at low quality to add compression artifacts."""
        q = quality or self.rng.randint(15, 45)
        _, buf = cv2.imencode(".jpg", image, [cv2.IMWRITE_JPEG_QUALITY, q])
        return cv2.imdecode(buf, cv2.IMREAD_UNCHANGED), annotations

    def binarization_variation(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
    ) -> tuple[np.ndarray, list[Annotation]]:
        """Shift the binarisation threshold to simulate faded/over-inked prints."""
        gray   = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        thresh = self.rng.randint(100, 200)
        _, bw  = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
        # convert back to BGR if input was colour
        if len(image.shape) == 3:
            bw = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)
        return bw, annotations

    def gaussian_noise(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
        sigma: float = None,
    ) -> tuple[np.ndarray, list[Annotation]]:
        s     = sigma or self.rng.uniform(5, 20)
        noise = self.np_rng.normal(0, s, image.shape).astype(np.float32)
        out   = np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)
        return out, annotations

    # ── 5. Orthogonal Geometric Transformations ───────────────────────────

    def orthogonal_rotate(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
        angle: int = None,          # 90 | 180 | 270; None = random
    ) -> tuple[np.ndarray, list[Annotation]]:
        """Rotate by 90°, 180°, or 270° and update bounding boxes."""
        a = angle or self.rng.choice([90, 180, 270])
        h, w = image.shape[:2]

        if a == 90:
            rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            new_w, new_h = h, w
            def _transform(cx, cy, bw, bh):
                return cy, 1.0 - cx, bh, bw
        elif a == 180:
            rotated = cv2.rotate(image, cv2.ROTATE_180)
            new_w, new_h = w, h
            def _transform(cx, cy, bw, bh):
                return 1.0 - cx, 1.0 - cy, bw, bh
        else:  # 270
            rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            new_w, new_h = h, w
            def _transform(cx, cy, bw, bh):
                return 1.0 - cy, cx, bh, bw

        new_anns = []
        for ann in annotations:
            # scale box to new image dimensions
            ncx, ncy, nbw, nbh = _transform(ann.cx, ann.cy, ann.w, ann.h)
            # correct aspect when image is non-square
            if a in (90, 270):
                ncx = ncx * h / new_w
                ncy = ncy * w / new_h
                nbw = nbw * h / new_w
                nbh = nbh * w / new_h
            new_anns.append(Annotation(ann.label, ncx, ncy, nbw, nbh))

        return rotated, new_anns

    def horizontal_flip(
        self,
        image: np.ndarray,
        annotations: list[Annotation],
    ) -> tuple[np.ndarray, list[Annotation]]:
        """Flip horizontally — suitable only if your CAD symbols are symmetric."""
        flipped  = cv2.flip(image, 1)
        new_anns = [Annotation(a.label, 1.0 - a.cx, a.cy, a.w, a.h)
                    for a in annotations]
        return flipped, new_anns


# ─────────────────────────── pipeline orchestrator ────────────────────────

TECHNIQUE_REGISTRY = {
    "contextual_paste":       "Contextual Paste onto CAD background",
    "inject_clutter":         "CAD Clutter Injection (grids + lines)",
    "morphological":          "Morphological Line-Weight Variation",
    "salt_pepper":            "Salt-and-Pepper Noise",
    "jpeg_artifacts":         "JPEG Compression Artifacts",
    "binarization":           "Binarisation Threshold Shift",
    "gaussian_noise":         "Gaussian Noise",
    "rotate_90":              "Orthogonal Rotation 90°",
    "rotate_180":             "Orthogonal Rotation 180°",
    "rotate_270":             "Orthogonal Rotation 270°",
    "horizontal_flip":        "Horizontal Flip",
}


def draw_annotations(image: np.ndarray, annotations: list[Annotation]) -> np.ndarray:
    """Draw bounding boxes on a copy — for visual QA only."""
    vis = image.copy()
    h, w = vis.shape[:2]
    for ann in annotations:
        x1, y1, x2, y2 = ann.to_abs(w, h)
        cv2.rectangle(vis, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(vis, ann.label, (x1, max(0, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 0), 1)
    return vis


def run_pipeline(
    image_path: str,
    json_path: str,
    output_dir: str,
    copies: int,
    neg_dir: Optional[str],
    seed: int,
    techniques: list[str],
    qa_preview: bool,
):
    rng    = random.Random(seed)
    np_rng = np.random.default_rng(seed)
    aug    = CADAugmentor(rng, np_rng)

    # ── load inputs ───────────────────────────────────────────────────────
    image = cv2.imread(image_path)
    if image is None:
        sys.exit(f"Error: cannot read image '{image_path}'")

    h, w  = image.shape[:2]
    raw   = load_json(json_path)
    anns  = parse_annotations(raw, w, h)
    print(f"Loaded {len(anns)} annotation(s) from '{json_path}'")
    print(f"Image size: {w}×{h}  |  seed: {seed}")

    # ── load negative backgrounds if provided ─────────────────────────────
    neg_images: list[np.ndarray] = []
    if neg_dir and os.path.isdir(neg_dir):
        exts = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp"}
        for p in Path(neg_dir).iterdir():
            if p.suffix.lower() in exts:
                img = cv2.imread(str(p))
                if img is not None:
                    neg_images.append(img)
        print(f"Loaded {len(neg_images)} negative background(s) from '{neg_dir}'")
    else:
        if "contextual_paste" in techniques:
            print("Warning: --neg_dir not set or not found; skipping contextual_paste")
            techniques = [t for t in techniques if t != "contextual_paste"]

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    qa_path  = out_path / "qa_preview"
    if qa_preview:
        qa_path.mkdir(exist_ok=True)

    stem    = Path(image_path).stem
    ext     = Path(image_path).suffix or ".png"
    count   = 0
    summary = []

    for tech in techniques:
        if tech not in TECHNIQUE_REGISTRY:
            print(f"  Skipping unknown technique '{tech}'")
            continue

        for i in range(copies):
            img_copy  = image.copy()
            ann_copy  = list(anns)
            aug_label = f"{stem}_{tech}_{i:03d}"

            try:
                if tech == "contextual_paste":
                    img_copy, ann_copy = aug.contextual_paste(img_copy, ann_copy, neg_images)
                elif tech == "inject_clutter":
                    img_copy, ann_copy = aug.inject_cad_clutter(img_copy, ann_copy)
                elif tech == "morphological":
                    img_copy, ann_copy = aug.morphological_variation(img_copy, ann_copy)
                elif tech == "salt_pepper":
                    img_copy, ann_copy = aug.salt_and_pepper(img_copy, ann_copy)
                elif tech == "jpeg_artifacts":
                    img_copy, ann_copy = aug.jpeg_artifacts(img_copy, ann_copy)
                elif tech == "binarization":
                    img_copy, ann_copy = aug.binarization_variation(img_copy, ann_copy)
                elif tech == "gaussian_noise":
                    img_copy, ann_copy = aug.gaussian_noise(img_copy, ann_copy)
                elif tech == "rotate_90":
                    img_copy, ann_copy = aug.orthogonal_rotate(img_copy, ann_copy, 90)
                elif tech == "rotate_180":
                    img_copy, ann_copy = aug.orthogonal_rotate(img_copy, ann_copy, 180)
                elif tech == "rotate_270":
                    img_copy, ann_copy = aug.orthogonal_rotate(img_copy, ann_copy, 270)
                elif tech == "horizontal_flip":
                    img_copy, ann_copy = aug.horizontal_flip(img_copy, ann_copy)
            except Exception as e:
                print(f"  ✗ {aug_label}: {e}")
                continue

            # ── save image ────────────────────────────────────────────────
            img_out = str(out_path / f"{aug_label}{ext}")
            cv2.imwrite(img_out, img_copy)

            # ── save annotation ───────────────────────────────────────────
            ann_data = {
                "source_image": os.path.abspath(image_path),
                "augmentation": tech,
                "copy_index": i,
                "image_width": img_copy.shape[1],
                "image_height": img_copy.shape[0],
                "annotations": [a.to_dict() for a in ann_copy],
            }
            json_out = str(out_path / f"{aug_label}.json")
            save_json(ann_data, json_out)

            # ── optional QA preview ───────────────────────────────────────
            if qa_preview:
                preview = draw_annotations(img_copy, ann_copy)
                cv2.imwrite(str(qa_path / f"{aug_label}_preview{ext}"), preview)

            count += 1
            summary.append((aug_label, TECHNIQUE_REGISTRY[tech]))

    # ── print summary ─────────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"  Done.  {count} augmented image(s) written to '{output_dir}'")
    print(f"{'─'*60}")
    tech_counts: dict[str, int] = {}
    for _, tech_name in summary:
        tech_counts[tech_name] = tech_counts.get(tech_name, 0) + 1
    for name, cnt in tech_counts.items():
        print(f"  {cnt:>3}×  {name}")
    if qa_preview:
        print(f"\n  QA previews (boxes drawn): {qa_path}")
    print()


# ─────────────────────────── CLI ──────────────────────────────────────────

ALL_TECHNIQUES = list(TECHNIQUE_REGISTRY.keys())


def main():
    parser = argparse.ArgumentParser(
        description="CAD Drawing Augmentation Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--image",      required=True, help="Input image path")
    parser.add_argument("--json",       required=True, help="Annotation JSON path")
    parser.add_argument("--output_dir", default="output", help="Output directory")
    parser.add_argument("--copies",     type=int, default=3,
                        help="Augmented copies per technique (default 3)")
    parser.add_argument("--neg_dir",    default=None,
                        help="Directory of negative CAD background images")
    parser.add_argument("--seed",       type=int, default=42)
    parser.add_argument("--techniques", nargs="+", default=ALL_TECHNIQUES,
                        metavar="TECH",
                        help=("Space-separated list of techniques. Available: "
                              + ", ".join(ALL_TECHNIQUES)))
    parser.add_argument("--qa_preview", action="store_true",
                        help="Save side-by-side preview with drawn bboxes (for QA)")
    args = parser.parse_args()

    print("\n  CAD Augmentation Pipeline")
    print(f"  Image      : {args.image}")
    print(f"  Annotations: {args.json}")
    print(f"  Techniques : {', '.join(args.techniques)}")
    print(f"  Copies/tech: {args.copies}")
    print(f"  Output     : {args.output_dir}\n")

    run_pipeline(
        image_path  = args.image,
        json_path   = args.json,
        output_dir  = args.output_dir,
        copies      = args.copies,
        neg_dir     = args.neg_dir,
        seed        = args.seed,
        techniques  = args.techniques,
        qa_preview  = args.qa_preview,
    )


if __name__ == "__main__":
    main()
