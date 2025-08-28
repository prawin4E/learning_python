## Reading and Writing Text Files

**Files** are used to store data on disk for long-term storage. Python makes working with text files super easy, and knowing how to work with files is essential for many programs (such as reading data, saving results, or configuration).[^1][^2][^3][^4]

***

## **2. Opening a File**

Use the built-in `open()` function:

```python
file = open("filename.txt", "mode")
```

- `filename.txt`: Name/path of your file
- `mode`: How you want to open the file (read, write, append, etc.)


### **Common File Modes**

| Mode | Name | Use Case |
| :-- | :-- | :-- |
| "r" | Read | Reading only (default). Error if not exist |
| "w" | Write | Overwrite or create file |
| "a" | Append | Add to end of file or create file |
| "r+" | Read/Write | Read and write (file must exist) |
| "w+" | Write/Read | Overwrite and read (creates new file) |
| "a+" | Append/Read | Read and append (creates if missing) |


***

## **3. Writing to a File**

### **A. Write a Single String**

```python
with open("myfile.txt", "w") as file:
    file.write("Hello, students!\n")
```

- `"w"` mode *creates* a new file or *overwrites* an existing file.
- Use `\n` to create a new line.


### **B. Write Multiple Lines**

```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("myfile.txt", "w") as file:
    file.writelines(lines)
```


### **C. Append to File**

```python
with open("myfile.txt", "a") as file:
    file.write("Another line at the end.\n")
```

- `"a"` mode will add content to the end without overwriting.

***

## **4. Reading from a File**

### **A. Entire File**

```python
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)
```

- Reads the whole file as one string.


### **B. One Line at a Time**

```python
with open("myfile.txt", "r") as file:
    first_line = file.readline()
    print(first_line)
```

- Each call to `.readline()` gives you the next line.


### **C. All Lines into a List**

```python
with open("myfile.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

- Loads all lines as strings into a list.

***

## **5. Best Practices**

- **Always use `with`** when opening files. This ensures the file is properly closed, even if errors occur.[^4][^5]
- **Always specify mode**: "r" for reading (default), "w" for writing, "a" for appending etc.
- If you open a file and forget to close it, you might cause memory leaks or other issues. Using `with` fixes this!

***

## **6. Example: Full Read \& Write Workflow**

```python
# Writing
with open("students.txt", "w") as f:
    f.write("Alice\nBob\nCharlie\n")

# Appending
with open("students.txt", "a") as f:
    f.write("David\n")

# Reading
with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())
```

- `.strip()` removes the trailing newline character for neat printing.

***

## **7. Handling Errors**

- If you try to open a non-existent file for reading, you get `FileNotFoundError`.
- Use `"w"` or `"a"` to create a file if it does not exist.[^6]
- Always read documentation or tutorials if unsure.[^6][^4]

***

## **8. Youtube Tutorials**

- **Python Tutorial: How to Read and Write Text Files** ([YouTube])[^7]
- **Master Python File Handling in 10 Minutes** ([YouTube])[^8]
- **File Operations in Python | Create, Open, Append, Read, Write** ([YouTube][^9])

***

## **9. References for Further Learning**

- FreeCodeCamp: File Handling in Python[^2]
- GeeksforGeeks: Reading and Writing Text Files[^10]
- W3Schools File Open \& File Write[^5][^4]
- Real Python: Reading and Writing Files in Python[^11]
- Programiz: Python File Handling

***

**Tip:**
Practice creating, reading, and writing your own text files—this solidifies your understanding!

**Practice Challenge:**

- Write a Python script to ask your name and save it to `names.txt`.
- Read the file and print each saved name.

You’re now ready to handle text files in Python like a pro!
<span style="display:none">[^12]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html

[^2]: https://www.freecodecamp.org/news/file-handling-in-python/

[^3]: https://www.codecademy.com/article/handling-text-files-in-python

[^4]: https://www.w3schools.com/python/python_file_open.asp

[^5]: https://www.w3schools.com/python/python_file_write.asp

[^6]: https://www.digitalocean.com/community/tutorials/python-read-file-open-write-delete-copy

[^7]: https://www.youtube.com/watch?v=gSbEXZvgyBw

[^8]: https://www.youtube.com/watch?v=yRXIbRuJ7yQ

[^9]: https://www.youtube.com/watch?v=XxRtj-GU5_8

[^10]: https://www.geeksforgeeks.org/python/reading-writing-text-files-python/

[^11]: https://realpython.com/read-write-files-python/

[^12]: https://stackoverflow.com/questions/6648493/how-to-open-a-file-for-both-reading-and-writing

## Appending to Files

Appending to a file means adding new data **to the end** of the file **without deleting or overwriting** the existing content. This is handy for logs, running data collection, or anytime you want to grow a file over time.[^1][^2][^3]

***

## **2. Opening a File in Append Mode**

- In Python, use the open mode **"a"** (append) or **"a+"** (append \& read) to open files for appending.

**Syntax:**

```python
file = open("filename.txt", "a")
```

- `"a"`: Add data at end (file is created if missing).
- `"a+"`: Like append, but also allows reading from the file.[^3][^1]


### **Using `with` statement (best practice):**

```python
with open("filename.txt", "a") as file:
    file.write("New line of data\n")
```


***

## **3. Writing Data When Appending**

- Data is always added at the end.
- If you want each new entry on a new line, include `\n`.

**Example:**

```python
with open("log.txt", "a") as log:
    log.write("New log entry\n")  # Each append adds a new line
```


***

## **4. Difference Between "w" and "a" Modes**

| Mode | Effect |
| :-- | :-- |
| "w" | Overwrites (deletes) existing content, or creates a new file |
| "a" | Adds to the end, keeps old content, creates file if needed |

**Quick Demo:**

```python
# Write mode (overwrites)
with open("example.txt", "w") as f:
    f.write("First line\n")

# Append mode (adds at end)
with open("example.txt", "a") as f:
    f.write("Just appended!\n")
```

> After both, `example.txt` has both "First line" and "Just appended!" lines.[^2][^1]

***

## **5. Appending Multiple Lines**

- Simply call `.write()` several times or use a loop.
- Remember to add `\n` if you want each line separate.

**Example:**

```python
with open("cities.txt", "a") as file:
    file.write("Chennai\n")
    file.write("Mumbai\n")
```


***

## **6. Appending Content of One File to Another**

**Example:**

```python
# Append all content from "source.txt" to "dest.txt"
with open("source.txt", "r") as src, open("dest.txt", "a") as dst:
    dst.write(src.read())
```

- Useful for merging files.[^4]

***

## **7. Appending and Reading ("a+" Mode)**

```python
with open("myfile.txt", "a+") as file:
    file.write("Extra data\n")
    file.seek(0)        # Move pointer to beginning before reading
    content = file.read()
    print(content)
```

- `"a+"` allows reading whole file after appending.[^1][^3]

***

## **8. Common Pitfalls**

- Forgetting to use `\n` means appended text may run together.
- Empty `{}` makes a dictionary, not a file or set!
- Always open in mode `"a"` or `"a+"` to append.

***

## **9. Appending Example - Step By Step**

```python
# Start with existing file or new file automatically created
with open("students.txt", "a") as f:
    f.write("Ravi\n")
    f.write("Priya\n")
# File now has previous content PLUS new appended names
```


***

## **10. Youtube Video Tutorials**

- **Append to Text File - Python Programming Basics For Beginners** ([YouTube])[^5]
- **Python for Beginners \#3: Append Content to Files Without Overwriting!** ([YouTube])[^6]

***

## **11. Further Learning References**

- GeeksforGeeks: Python append to a file[^1]
- Programiz: Append to a file[^7]
- W3Schools: Python File Write[^8][^2]
- Wiingy: Append to file in Python[^3]
- TutorialsPoint: how to open a file in append mode[^2]

***

**Tip:**
Always use `"a"` mode to add information to an existing file so nothing is lost!

**Practice Challenge:**

- Log students’ attendance: Ask for names and append to `"attendance.txt"` every time you run your program.

You can now confidently append to text files in Python!
<span style="display:none">[^10][^11][^12][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.geeksforgeeks.org/python/python-append-to-a-file/

[^2]: https://www.tutorialspoint.com/how-to-open-a-file-in-append-mode-with-python

[^3]: https://wiingy.com/learn/python/append-to-file-in-python/

[^4]: https://www.geeksforgeeks.org/python/python-append-content-of-one-text-file-to-another/

[^5]: https://www.youtube.com/watch?v=0BvNhu5qj8A

[^6]: https://www.youtube.com/watch?v=vl1Qrs2VT58

[^7]: https://www.programiz.com/python-programming/examples/append-to-file

[^8]: https://www.w3schools.com/python/python_file_write.asp

[^9]: https://www.youtube.com/watch?v=z1Klw2k_KJk

[^10]: https://stackoverflow.com/questions/4706499/how-do-i-append-to-a-file

[^11]: https://www.scaler.com/topics/append-to-file-python/

[^12]: https://docs.vultr.com/python/examples/append-to-a-file

## Writing Binary Files Manually and Using the Pickle Module

## **1. Understanding Binary vs. Text Files**

- **Text Files**: Store data as readable text (characters, lines, etc.). Editing and reading is easy and direct.
- **Binary Files**: Store data as raw bytes (images, audio, Python objects, etc.). Not human-readable. Allows compact and efficient storage of any kind of data.[^1][^2]

***

## **2. Writing Binary Files Manually**

### **A. Why write binary files?**

- Needed for saving non-textual info (like images, executables, or Python objects).
- Useful when efficiency or compactness is important.


### **B. Opening and Writing in Binary Mode**

- Use the `"wb"` (write-binary) mode with `open()`.

**Example 1: Write Raw Bytes**

```python
with open("sample.bin", "wb") as file:
    data = b"Hello"      # Bytes literal
    file.write(data)     # Writes 5 bytes to file
```

**Example 2: Using Struct for Packing Data**

```python
import struct

with open("data.bin", "wb") as file:
    i = 123
    f = 3.14
    # 'i' means integer, 'f' means float
    binary_data = struct.pack("if", i, f)
    file.write(binary_data)
```

- The `struct` module allows you to **convert Python numbers to binary format**.[^3]

**Example 3: Array to Binary File**

```python
import array

numbers = array.array("B", [10, 20, 30, 40])
with open("nums.bin", "wb") as file:
    file.write(numbers.tobytes())
```

- Array is converted to raw bytes and stored as binary.[^3]

***

## **3. Reading Binary Files**

- Use `"rb"` (read-binary) mode.
- Use `file.read()` for bytes.
- Use `struct.unpack()` or other methods to convert back to values.

***

## **4. Pickle Module: Serializing Python Objects**

### **A. What is Pickling?**

- **Pickling** is the process of converting a Python object into a byte stream (serialization).
- **Unpickling** recreates the object from the byte stream (deserialization).[^4][^5][^6]


### **B. Why Use Pickle?**

- Saves **any** Python object (list, dict, custom class, etc.) to a file for later use.
- Essential for saving data between runs, caching, or transmitting objects over a network.[^7][^6]

***

## **5. Writing to Binary Files with Pickle**

**Basic Example:**

```python
import pickle

data = {"name": "Arun", "age": 22, "marks": [95, 88, 90]}

with open("student.pkl", "wb") as file:
    pickle.dump(data, file)  # Dumps serialized data to file
```

- The object is now stored in binary format using pickle.

**To Read Back:**

```python
import pickle

with open("student.pkl", "rb") as file:
    record = pickle.load(file)
    print(record)
```

- The original object (dict) is reconstructed as it was!

***

## **6. Pickling Custom Objects**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Karthik", 20)

import pickle
with open("stud_obj.pkl", "wb") as f:
    pickle.dump(student1, f)

# To load back
with open("stud_obj.pkl", "rb") as f:
    student_loaded = pickle.load(f)
    print(student_loaded.name, student_loaded.age)
```

- You can save/load most Python objects, including class instances.

***

## **7. Important Notes \& Security Warnings**

- **Never unpickle data from an untrusted source** — it can execute arbitrary code during deserialization.[^5][^6]
- Pickle is **Python-specific** (not for sharing data with other languages).
- For long-term or more secure storage, consider alternatives like `json` (for simple objects).

***

## **8. Full Example: Pickling and Unpickling a Dictionary**

```python
import pickle

# Write (pickle)
mydata = {"Math": 90, "CompSci": 95}
with open("grades.pkl", "wb") as f:
    pickle.dump(mydata, f)

# Read (unpickle)
with open("grades.pkl", "rb") as f:
    data = pickle.load(f)
    print(data)  # Output: {'Math': 90, 'CompSci': 95}
```


***

## **9. YouTube Video Tutorials**

- **Python Binary Files | Python Tutorials for Beginners | 2025** ([YouTube][^8])
- **Python binary file handling to read and write a dictionary example using pickle** ([YouTube])[^9]

***

## **10. Further References**

- Tutorialspoint: How to write binary data to a file[^3]
- GeeksforGeeks: Understanding Python Pickling with example[^4]
- Real Python: The Python pickle Module[^7]
- DigitalOcean: Python Pickle Example[^6]
- Python4All: Working with binary files[^10]

***

**Quick Practice Challenges:**

- Save a list of numbers to a binary file using `.to_bytes()` or `array`.
- Pickle and unpickle a list of student dictionaries to a file.
- Make a Python function that takes any object and saves it to a binary file with pickle.

Now you know how to save and load complex Python data — not just as plain text, but as their actual Python objects!
<span style="display:none">[^11][^12][^13][^14][^15]</span>

<div style="text-align: center">⁂</div>

[^1]: https://connectjaya.com/text-files-vs-binary-files-in-python/

[^2]: https://techskillguru.com/python/python-file-handling

[^3]: https://www.tutorialspoint.com/how-to-write-binary-data-to-a-file-using-python

[^4]: https://www.geeksforgeeks.org/understanding-python-pickling-example/

[^5]: https://www.blackduck.com/blog/python-pickling.html

[^6]: https://www.digitalocean.com/community/tutorials/python-pickle-example

[^7]: https://realpython.com/python-pickle-module/

[^8]: https://www.youtube.com/watch?v=amH0xHKz0ck

[^9]: https://www.youtube.com/watch?v=7JNVNKyEnQE

[^10]: https://www.pythonforall.com/python/filehandling/fbinary

[^11]: https://www.geeksforgeeks.org/python/python-write-bytes-to-file/

[^12]: https://ai.thestempedia.com/example/working-with-binary-files-in-python/

[^13]: https://diveintopython.org/learn/file-handling/binary-files

[^14]: https://www.python4data.science/en/latest/data-processing/serialisation-formats/pickle/pickle-examples.html

[^15]: https://www.tutorialsteacher.com/python/python-read-write-file

