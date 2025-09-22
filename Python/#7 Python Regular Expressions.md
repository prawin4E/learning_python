#  What Are Regular Expressions?

# **1. Introduction to Regular Expressions (Regex)**

A **regular expression** (or **regex**) is a powerful tool for finding, validating, and manipulating patterns in text. Think of regex as a “pattern-search language”—helping you zap through text and pick out, replace, or validate the parts that match your desired format.[^1][^2][^3]

**Analogy:**
Regex is like a super-smart magnet. You tune it to only pick up paper clips (or any shape you want), letting everything else stay behind!

***

## **2. Why Use Regex in Python?**

- Searching for specific text patterns in files or strings.
- Validating user input (e.g. emails, phone numbers).
- Extracting structured data from unstructured sources.
- Replacing or splitting text in bulk.

***

## **3. Regex in Python – The Basics**

Python’s built-in `re` module is your regex toolkit.

```python
import re
# Find all digits in a string
print(re.findall(r"\d+", "I have 2 cats and 10 fish."))
```

**Key functions:**

- `re.search(pattern, string)`: find first match
- `re.findall(pattern, string)`: get all matches
- `re.match(pattern, string)`: check if pattern is at start
- `re.split(pattern, string)`: split by pattern
- `re.sub(pattern, replacement, string)`: replace matches

***

## **4. Essential Patterns and What They Do**

| Symbol | Pattern | Example String | Matches |
| :-- | :-- | :-- | :-- |
| `.` | Any single character | `"cat." vs "cats", "cat!"` | `cats`, `cat!` |
| `\d` | Any digit | `"Price: 45"` | `4`, `5` |
| `\w` | Word character | `"A23#B"` | `A23`, `B` |
| `\s` | Whitespace | `"Hi \t there \n"` | spaces, tab, newline |
| `^abc` | Starts with 'abc' | `"abcdef"` | `abcdef` |
| `abc$` | Ends with 'abc' | `"xyzabc"` | `xyzabc` |
| `[a-d]` | Any a, b, c, d | `"bead"` | `b`, `e`, `a`, `d` |
| `[^0-9]` | Not a digit | `"abc8def"` | `a`, `b`, `c`, `d`, `e`, `f` |
| `a*` | Zero or more a's | `"baaa"` | `aaa` |
| `a+` | One or more a's | `"baaa"` | `aaa` |
| `a?` | Zero or one a | `"ba"` | `a` |
| `{n}` | Exactly n repeats | `"aaaab"` | Matches 4 a's |
| `{n,m}` | n to m repeats | `"aaaaabc"` | Matches 4–5 a's |
| `(cat|dog)` | cat OR dog | `"my cat and dog"` | `cat`, `dog` |


***

## **5. Practical Examples – Search, Extraction, Validation**

### **A. Extract All Words Starting With ‘a’**

```python
import re
text = "apple apricot banana avocado"
words = re.findall(r"\ba\w*", text)
print(words)  # Output: ['apple', 'apricot', 'avocado']
```


***

### **B. Find All Email Addresses in Text**

```python
msg = "Contact: alice@gmail.com, bob@institute.edu"
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", msg)
print(emails)  # Output: ['alice@gmail.com', 'bob@institute.edu']
```


***

### **C. Check if Phone Number Is Indian Format**

```python
phone = "9876543210"
if re.fullmatch(r"^[6-9]\d{9}$", phone):
    print("Valid Indian phone number!")
```


***

### **D. Validate Password (8+ chars, at least 1 digit and 1 uppercase)**

```python
pw = "PyThon2025"
pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
if re.match(pattern, pw):
    print("Strong password!")
```

- `(?=.*[A-Z])`: must contain uppercase
- `(?=.*\d)`: must contain digit
- `.{8,}`: at least 8 characters

***

### **E. Extract Dates in dd-mm-yyyy Format**

```python
sentence = "Born: 23-08-2000, joined on 01-02-2020"
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', sentence)
print(dates)  # [\'23-08-2000\', \'01-02-2020\']
```


***

### **F. Replace Multiple Spaces With a Single Space**

```python
text = "This      is   spaced   out."
cleaned = re.sub(r"\s+", " ", text)
print(cleaned)  # Output: "This is spaced out."
```


***

### **G. Split Text by Comma or Semicolon**

```python
data = "A,B;C,D;E"
items = re.split(r"[;,]", data)
print(items)    # [\'A\', \'B\', \'C\', \'D\', \'E\']
```


***

### **H. Extract All Uppercase Words**

```python
s = "This is a TEST of CAPS and Python"
caps = re.findall(r"\b[A-Z]{2,}\b", s)
print(caps)  # [\'TEST\', \'CAPS\']
```


***

### **I. Find Hashtags in a Sentence**

```python
tweet = "#Python is cool #AI #2025"
tags = re.findall(r"#\w+", tweet)
print(tags)  # [\'#Python\', \'#AI\', \'#2025\']
```


***

### **J. Validate Time in 24-hour Format**

```python
times = "Meeting at 18:30, call at 09:05"
all_times = re.findall(r"\b([01]\d|2[0-3]):[0-5]\d\b", times)
print(all_times)  # ['18:30', '09:05']
```


***

## **6. Advanced: Groups and Alternations**

**Extract First Name and Last Name:**

```python
name = "Name: Arun Kumar"
match = re.search(r"Name: (\w+) (\w+)", name)
if match:
    print(match.group(1), match.group(2))  # Arun Kumar
```

**Match Either “cat” or “dog”:**

```python
pets = "My pets: cat, dog, fish"
for pet in re.findall(r"cat|dog", pets):
    print(pet)  # cat, dog
```


***

## **7. Best Practices**

- Use raw strings: `r"pattern"`
- Document tricky patterns alongside code!
- For complex extraction, use groups with parentheses `()`
- Useful online testers: regex101.com

***

## **8. References for Deep Learning**

- W3Schools: Python Regex[^1]
- RealPython: Regex Tutorial[^3]
- Google Python Education: Regular Expressions[^2]
- GeeksforGeeks: Python RegEx Examples[^4]
- Programiz: Regex Examples[^5]

***

## **9. YouTube Tutorials**

- **Regular Expressions in Python – FULL COURSE** ([YouTube])[^6]
- **Python Regular Expressions Tutorial** ([YouTube])[^7]
- **Python re Module Explained** ([YouTube])[^8]

***

## **10. Practice Exercises (Try These!)**

1. Extract all domain names from a list of emails.
2. Replace all numbers in text with `#`.
3. Find all hexadecimal numbers like `0x1A3F`.
4. Validate Indian postal codes (6 digits, starts with 1-9).
5. Extract all links from HTML: `href="..."`.

***

**Summary:**
Regular expressions are the Swiss Army knife for manipulating and searching text. Practice with more patterns for real-world tasks, and you’ll find “regex” invaluable in data science, web development, and scripting!
<span style="display:none">[^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.w3schools.com/python/python_regex.asp

[^2]: https://developers.google.com/edu/python/regular-expressions

[^3]: https://realpython.com/regex-python/

[^4]: https://www.geeksforgeeks.org/python/regular-expression-python-examples/

[^5]: https://www.programiz.com/python-programming/regex

[^6]: https://www.youtube.com/watch?v=AEE9ecgLgdQ

[^7]: https://www.youtube.com/watch?v=V_BozMwoYe4

[^8]: https://www.youtube.com/watch?v=K8L6KVGG-7o

[^9]: Screenshot-2025-08-29-at-1.19.55-AM.jpg


## Extended Regular Expressions and Wildcards

**Extended regular expressions (EREs)** build on basic regex patterns, adding new metacharacters and functionality for even more powerful text searching and extraction. **Wildcards** are symbols in regex that represent variable characters—they’re at the heart of flexible pattern matching in Python.[^1][^2][^3]

***

## **2. Wildcards in Regex**

- The **dot (`.`)** is the classic wildcard: it matches **any single character** except a newline.

```python
import re
print(re.search(r'c.t', 'cat'))     # Matches "cat"
print(re.search(r'c.t', 'cut'))     # Matches "cut"
print(re.search(r'c.t', 'ct'))      # No match (missing character)
```

- The **asterisk (`*`)** matches **zero or more** of the character or group before it.

```python
print(re.search(r'ab*', 'a'))       # Matches "a"
print(re.search(r'ab*', 'abbb'))    # Matches "abbb"
print(re.search(r'ab*', 'ac'))      # Matches "a" (b not required)
```

- The **plus (`+`)** matches **one or more** of the preceding character/group.

```python
print(re.search(r'st+op', 'stop'))  # Matches "stop"
print(re.search(r'st+op', 'sttop')) # Matches "sttop"
print(re.search(r'st+op', 'sop'))   # No match (t required)
```

- The **question mark (`?`)** matches **zero or one** of the group before it.

```python
print(re.search(r'colou?r', 'color'))   # Matches "color"
print(re.search(r'colou?r', 'colour'))  # Matches "colour"
print(re.search(r'colou?r', 'colur'))   # No match
```


***

## **3. Quantifiers and Extended Patterns**

- **Curly braces (`{m,n}`):** Match the previous character/group between `m` and `n` times.

```python
re.search(r'a{3,5}', 'aaaaaa')  # Matches "aaaaa" (most possible)
re.search(r'a{3,5}?', 'aaaaaa') # Matches "aaa"  (least possible)
```

    - `{3,}` means 'at least 3 times'; `{,5}` means 'up to 5 times'.

**Examples:**

- `r"\d{2,4}"` — Match a 2 to 4 digit number (`23`, `2025`)
- `r"[A-Z]{1,3}"` — 1 to 3 uppercase letters

***

## **4. Groups and Non-capturing Groups (Extended Syntax)**

- Parentheses create **groups**: `r"(abc)+"` matches one or more repetitions of `abc`.
- Non-capturing group: `r"(?:abc)+"` — groups pattern without capturing the match for later retrieval.[^1]

```python
m = re.match(r"([abc])+", "abc")
print(m.groups())    # ('c',)
m = re.match(r"(?:[abc])+", "abc")
print(m.groups())    # ()
```


***

## **5. OR and Alternation (`|`)**

`A|B` means match either `A` or `B` pattern.

```python
text = "dog and cat"
print(re.findall(r"dog|cat", text))    # ['dog', 'cat']
```


***

## **6. Anchors: Start, End (`^`, `$`)**

- `^` matches the **start** of a string.
- `$` matches the **end** of a string.

```python
print(re.search(r"^Hello", "Hello World"))   # Match
print(re.search(r"World$", "Hello World"))   # Match
print(re.search(r"^World", "Hello World"))   # No match
```


***

## **7. Advanced Wildcard Patterns**

### Match Any Number of Any Character (Greedy vs Non-Greedy)

- `.*` matches **any number of any character** (greedy).
- `.*?` matches as few as possible (non-greedy).

```python
s = "<p>Some <b>bold</b> text</p>"
print(re.findall(r"<.*?>", s))  # Matches all HTML tags efficiently
```


### Wildcards for Flexible Searches

- Match words with one letter different: `r"p.th.n"` with `"python"`.
- Match variable endings: `r"work.*"` matches `"work"`, `"worker"`, `"working"`.
- Find file extensions: `r"\.\w+$"` matches `".py"`, `".txt"` at end of filenames.

***

## **8. Character Classes and Ranges**

- `[A-Za-z]` any letter (upper or lower)
- `[0-9]` any digit
- `[^e]` anything except `e`
- `[a-zA-Z0-9_]` any “word” character

**Example:**

```python
re.findall(r"\w+\.(jpg|png|gif)", "img1.jpg img2.txt img3.png")  # ['jpg', 'png']
```


***

## **9. Flags (re Module Extensions)**

Extend regex capabilities with flags:

- `re.IGNORECASE` (`re.I`): Ignore case
- `re.MULTILINE` (`re.M`): `^`/`$` match at start/end of each line
- `re.DOTALL` (`re.S`): `.` matches newlines too

```python
pattern = re.compile(r'^python', re.IGNORECASE)
print(pattern.search('PyThOn is powerful'))  # Matches
```


***

## **10. Extended Regex Examples**

### a. Find Valid HTML Tag Names

```python
text = "<div> <h1> <title> <my-custom-tag>"
tags = re.findall(r"<([a-zA-Z0-9-]+)>", text)
print(tags)  # ['div', 'h1', 'title', 'my-custom-tag']
```


### b. Extract All Words with Exactly 5 Letters

```python
sentence = "Hello world, this regex helps!"
words = re.findall(r"\b\w{5}\b", sentence)
print(words)  # ['Hello', 'world']
```


### c. Replace All Vowels With `*`

```python
s = "Regular Expressions"
finished = re.sub(r"[aeiou]", "*", s, flags=re.IGNORECASE)
print(finished)  # "R*g*l*r Expr*ss**ns"
```


### d. Find All Words Ending With 'ing'

```python
re.findall(r"\b\w+ing\b", "working, ping, ring, sing, going, go")
```


***

## **11. Practical Wildcard Applications**

- Filter data by partial matches: `r"2025.*\.csv"` matches `"202501_final.csv"`
- Search for alternate spellings: `r"colou?r"` matches both `"color"` and `"colour"`
- Parse formatted strings: e.g. dates, emails, custom IDs using concise patterns

***

## **12. References & Further Learning**

- Python Docs: Regular Expression HOWTO, Module: re[^4][^1]
- Google Python Education: Regular Expressions[^2]
- Dataquest: Python Regex Cheat Sheet[^3]
- GeeksforGeeks: Python Regex[^5]

***

## **13. YouTube Tutorials**

- **Regular Expressions in Python – FULL COURSE** ([YouTube])[^6]
- **Regular Expression Methods in Python** ([YouTube])[^7]
- **Complete Regular Expressions Tutorial (Wildcard & More)** ([YouTube])[^8]

***

**Tip:**
Extended regular expressions and wildcards transform regex from simple string searchers into flexible engines—ideal for log parsing, file searches, data cleaning, and much more. Practice with various combinations to become a regex master!

**Practice Challenge:**

1. Find all `.txt` and `.csv` files in a list of filenames using `.*\.(txt|csv)$`.
2. Extract all words of 2–3 letters from a paragraph.
3. Match either "Arun Kumar" or "Arun Singh" using `Arun (Kumar|Singh)`.
4. Use flags to match "python" in any case and across multi-line inputs.

With extended regex and wildcards, there’s almost no pattern you can’t match!
<span style="display:none">[^10][^11][^12][^13][^14][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://docs.python.org/3/howto/regex.html

[^2]: https://developers.google.com/edu/python/regular-expressions

[^3]: https://www.dataquest.io/cheat-sheet/regular-expressions-cheat-sheet/

[^4]: https://docs.python.org/3/library/re.html

[^5]: https://www.geeksforgeeks.org/python/python-regex/

[^6]: https://www.youtube.com/watch?v=AEE9ecgLgdQ

[^7]: https://www.youtube.com/watch?v=EzeeypMKx7o

[^8]: https://www.youtube.com/watch?v=vsa9GGzMFXQ

[^9]: https://realpython.com/regex-python/

[^10]: https://www.educative.io/answers/how-to-implement-wildcards-in-python

[^11]: https://stackoverflow.com/questions/8826499/expanding-regex-in-python

[^12]: https://www.reddit.com/r/learnpython/comments/10lm3qt/how_to_search_strings_in_python_using_a_wildcard/

[^13]: https://facelessuser.github.io/BracketHighlighter/extended-regex/

[^14]: https://stackoverflow.com/questions/1996482/wildcard-matching-a-string-in-python-regex-search
