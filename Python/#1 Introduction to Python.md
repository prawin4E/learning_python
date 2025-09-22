# Introduction to Python

## What is Python and history of Python ? 

Python, the programming language, was conceived in the late 1980s by Dutch programmer Guido van Rossum as a successor to the ABC language, with its implementation beginning in December 1989 at the Centrum Wiskunde & Informatica (CWI) in the Netherlands. It was named after the BBC comedy series Monty Python's Flying Circus to reflect a sense of fun and readability in programming, and has evolved into one of the most popular languages due to its simplicity, versatility, and strong community support. 


![Alt text](https://blog.eduonix.com/wp-content/uploads/2019/03/Python-Versions-e1553084625758.jpg)


**Early Development (Late 1980s–1991)**

Van Rossum started Python as a hobby project during the 1989 Christmas holidays, aiming for a language that emphasized code readability, exception handling, and ease of use while addressing limitations in ABC, such as better interfacing with operating systems. The first public release, Python 0.9.0, occurred in February 1991, introducing core features like classes with inheritance, exception handling, functions, and data types including lists, dictionaries, and strings, along with a module system inspired by Modula-3.

**Python 1.x Era (1994–2000)**

Python 1.0 was officially released on January 26, 1994, adding functional programming tools (e.g., lambda, map, filter, reduce), support for complex numbers, improved error handling via exceptions, and enhanced object-oriented capabilities. This version laid foundational elements for Python's growth, and by 1994, the comp.lang.python discussion forum was established, fostering community involvement. Throughout the 1990s, Python gained traction for its readability and was influenced by languages like C, Modula-3, and Perl.

**Python 2.x Era (2000–2008)**

Python 2.0, released on October 16, 2000, marked a shift to a more community-driven development process and introduced key features such as list comprehensions, cycle-detecting garbage collection, Unicode support, augmented assignments, and keyword arguments. It became widely adopted in web development, scientific computing, scripting, and automation, with libraries like NumPy, SciPy, and Django emerging. Python 2.7, the final 2.x release, extended support until 2020, after which it received no further updates.

**Python 3.x Era (2008–Present)**

Python 3.0, a major backwards-incompatible redesign, was released on December 3, 2008, to fix inconsistencies in Python 2, including improved Unicode handling, syntax refinements (e.g., print as a function), and better integer division. A 2to3 utility helped migrate code from Python 2. Van Rossum stepped down as Benevolent Dictator for Life (BDFL) in July 2018, leading to a steering council model under the Python Software Foundation. As of June 2025, Python 3.13.5 is the latest stable release, with ongoing security updates for versions back to 3.9

Python's history reflects its evolution from a personal project to a global standard in fields like data science, AI, and web development, driven by open-source contributions and its emphasis on simplicity.

## Python 2 and Python 3 difference.

Python 2 and Python 3 are two major versions of the Python programming language, with Python 3 released in 2008 as an improved successor to Python 2 (released in 2000), introducing breaking changes for better syntax, performance, and features, though Python 2 reached end-of-life in 2020 and is no longer supported or recommended for new projects. Key differences include syntax variations, default behaviors, and library compatibility, making Python 3 the standard choice today while Python 2 is mainly relevant for legacy code maintenance.[^1][^2][^4][^5]

### Overview and Recommendation

Python 2 is no longer maintained or updated, with official support ending in January 2020, leading to potential security risks and lack of new features. Python 3 is actively developed, more readable, and used in fields like data science and software engineering, with most libraries now supporting it exclusively. For new development, always use Python 3; Python 2 should only be considered for migrating or maintaining old codebases.[^2][^4][^5][^1]

### Key Differences

The following table summarizes major differences based on syntax, behavior, and features. Examples are provided where relevant.


| Feature | Python 2 | Python 3 | Notes/Example |
| :-- | :-- | :-- | :-- |
| **Print** Keyword | Treated as a statement (e.g., `print "Hello"`) | Treated as a function requiring parentheses (e.g., `print("Hello")`) | This change allows for more flexibility, like printing to files; Python 2 accepts parentheses optionally, but Python 3 requires them[^1][^2][^3][^5][^7]. Example in Python 2: `print "Hi! This is Python 2"`; in Python 3: `print("Hi! This is Python 3")`[^1]. |
| **String Storage** | Strings stored as ASCII by default | Strings stored as Unicode (UTF-8) by default | Python 3's approach improves handling of international characters without extra declarations[^1][^2][^3][^5]. In Python 2, Unicode requires a separate type; Python 3 unifies them for better compatibility[^3]. |
| **Integer Division** | Division of integers yields an integer (floor division, e.g., `7/2` returns 3) | Division of integers yields a float (true division, e.g., `7/2` returns 3.5); use `//` for floor division | This prevents unexpected integer results in Python 3; Python 2's behavior can lead to precision loss without explicit floats[^1][^2][^3][^5]. Example: In Python 2, `1/2` is 0; in Python 3, it's 0.5[^5]. |
| **Exceptions** | Enclosed in notations (e.g., `except Exception, e:`) or without parentheses | Enclosed in parentheses with `as` keyword (e.g., `except Exception as e:`) | Python 3's syntax is stricter and more consistent for error handling[^1][^2]. Raising exceptions in Python 2 uses commas (e.g., `raise Exception, "Error"`); in Python 3, parentheses (e.g., `raise Exception("Error")`)[^2]. |
| **Iteration Functions** | Uses `xrange()` for memory-efficient iterations (returns an iterator) and `range()` which returns a list | Uses `range()` as an efficient iterator (similar to Python 2's `xrange()`); no `xrange()` exists | Python 3's `range()` is more memory-efficient for large ranges, reducing overhead[^1][^2][^3]. Python 2's `xrange()` was added for iterations to avoid full lists in memory[^2]. |
| **Variable Behavior in Loops** | Global variables can change if used inside loops (potential leakage) | Variables do not leak or change unexpectedly outside their scope | This makes Python 3 safer and less prone to subtle bugs[^1]. |
| **Unicode Support** | Optional and requires explicit declaration (separate `unicode()` type) | Default encoding, with no separate declaration needed | Python 3 simplifies text handling, especially for non-ASCII data[^2][^3]. Python 2 has ASCII `str()` and separate `unicode()`, while Python 3 has unified Unicode `str()` and byte types[^3]. |
| **Comparing Unorderable Types** | Allows comparisons that may return arbitrary results (e.g., `[^1][^2] > 'foo'` returns False without error) | Raises a `TypeError` for unorderable types | This prevents silent errors in Python 3, improving code reliability[^3]. Example in Python 2: `(1, 2) > 'foo'` returns True arbitrarily[^3]. |
| **Syntax Complexity** | More complicated and verbose in some cases | Simpler and more readable overall | Python 3 reduces boilerplate, making it easier for beginners[^1]. |
| **Libraries and Compatibility** | Many libraries are not forward-compatible; code can be ported to Python 3 with effort | Libraries are often Python 3-specific; not backward-compatible with Python 2 | Python 3 has broader modern library support, but migrating from Python 2 requires handling incompatibilities[^1][^5]. |
| **Performance Notes** | Generally faster in some benchmarks (e.g., loops) due to older optimizations | Can be slower in certain cases but offers better overall features; speed differences are minor and context-dependent | Python 3 may run loops slightly slower (e.g., a while loop test: 1.72 ms in Python 2 vs. 2.68 ms in Python 3), but this is not a core difference[^3]. |

### Additional Notes

- **Backward Compatibility**: Python 3 is not backward-compatible with Python 2, meaning Python 2 code often needs modifications to run on Python 3, while the reverse requires significant effort. Tools like `2to3` can assist in migration, but manual review is essential.[^5][^7][^1]
- **Legacy Usage**: Python 2 was commonly used for roles like DevOps engineering but is obsolete post-2020; Python 3 dominates in areas like data science and web development. Scientific libraries (e.g., NumPy) have largely dropped Python 2 support.[^1][^5]
- **Code Porting Tip**: To make Python 2 code more future-proof, import features like `from __future__ import print_function` to use Python 3-style print. However, full compatibility between versions is limited, and dual-support strategies are no longer recommended for new code.[^7][^5]
- If search results lack details on a specific aspect (e.g., advanced metaprogramming differences), note that Python 3 generally promotes cleaner practices, but consult official documentation for exhaustive lists.
<span style="display:none">[^6]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.interviewbit.com/blog/difference-between-python-2-and-3/

[^2]: https://testbook.com/key-differences/difference-between-python-2-and-python-3

[^3]: https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html

[^4]: https://www.reddit.com/r/learnpython/comments/vvxghq/what_are_the_differences_between_python_2_and/

[^5]: https://scipy-lectures.org/intro/python_2_python_3.html

[^6]: https://www.ibm.com/docs/en/cloud-pak-sec-aas?topic=scripts-python-2-python-3-differences

[^7]: https://cv-tricks.com/how-to/developer-guide-to-key-differences-between-python-2-and-3/

## Python Identifiers, Keywords and Indentation

**Definition**:
Identifiers are **names** used to identify variables, functions, classes, modules, or other objects in Python code.

**Rules for Identifiers:**

- An identifier can be made of letters (a-z, A-Z), digits (0-9), and underscores (_).
- It **must not** start with a digit.
- Python identifiers are **case-sensitive** (`Var` and `var` are different).
- Cannot use Python **keywords** as identifiers (more below).
- Special symbols like `@`, `$`, `%`, etc. are **not allowed**.
- There’s no strict length limit, but keep them readable.

**Good Identifier Examples:**

```python
student_name = "Arun"
age = 20
marks2025 = 95
_total = 150
user_ID = "S001"
```

**Bad Identifier Examples (INVALID):**

```python
score1 = 25          # Does not start with a digit
user_at = "abc"        # No special symbols allowed
class_string = "Maths"      # 'class' is not a Keyword
```

**Tips:**

- Use meaningful names: `total_amount` instead of `ta`
- Use underscores to increase readability (snake_case).

***

## 2. What are Keywords in Python?

**Definition**:
**Keywords** are reserved words in Python with special meaning. You **cannot use these as identifiers**. They are the “vocabulary” of Python’s language.

**Some Common Python Keywords:**

```python
"""
and, as, assert, break, class, continue, def, del,
elif, else, except, False, finally, for, from, global,
if, import, in, is, lambda, None, nonlocal, not, or,
pass, raise, return, True, try, while, with, yield
"""
```

**How to list keywords in Python:**

```python
import keyword
print(keyword.kwlist)
```

**Example (using a keyword correctly):**

```python
for i in range(5):
    print(i)
```

**Example (incorrect usage - ERROR!):**

```python
define = 25          # Invalid. 'def' is a keyword.
```


***

## 3. What is Indentation in Python?

**Definition**:
**Indentation** is the **space at the beginning of a code line**. Where many languages use curly braces `{}` to define scope (like loops, functions, etc.), Python uses indentation for this purpose.

**Why is Indentation Important?**

- It defines code blocks (where a function, loop, if/else, etc. starts and ends).
- **Incorrect indentation leads to errors** (usually `IndentationError`).

**Standard Practice:**

- Use **4 spaces** per indentation level (tabs are allowed but spaces are preferred for consistency).
- Mixing tabs and spaces can cause errors.

**Good Indentation Example:**

```python
def greet(name):
    if name:
        print("Hello,", name)
    else:
        print("Hello, Guest!")

greet("Alice")
```

**Output:**

```
Hello, Alice
```

**Bad Indentation Example (causes error):**

```python
def bad_indent():
    print("This will not cause an error")   # ERROR! Not indented inside the function
```

*Python will show: `IndentationError: expected an indented block`*

**Multiple Blocks Example:**

```python
for i in range(3):
    print("Inside loop,", i)
print("Outside loop")
```

**Output:**

```
Inside loop, 0
Inside loop, 1
Inside loop, 2
Outside loop
```


***

### **Summary Table**

| Concept | Function | Examples | Errors To Avoid |
| :-- | :-- | :-- | :-- |
| Identifier | Names for variables/functions | age, user_name, total_1 | 1stvar, class, my-var |
| Keyword | Reserved words (special meaning) | if, for, def, import, return, True, False | Using as variable names |
| Indentation | Defines code block structure | 4 spaces under `def`, `for`, `if` | Missing or inconsistent indent |


***

### **Beginner Tips**

- Always use descriptive identifiers.
- Never use reserved keywords as variable or function names.
- Indentation *is not optional* in Python—pay careful attention from the start!

Start practicing by writing code with clear identifiers and consistent indentation—you’ll avoid the most common beginner errors!


### **Identifiers, Keywords, and Indentation in Python – Video Tutorials**

- **[Master Python Keywords \& Identifiers in 2024: Complete Guide](https://www.youtube.com/watch?v=BCXwfkZJfTM)**
    - A comprehensive and up-to-date guide, covering case sensitivity, reserved words, identifier rules, and beginner-friendly naming conventions. Also includes common pitfalls and clean coding habits.[^8][^9][^10][^11][^12][^13][^14][^15][^16][^17]
- **[Python Tutorial \#2 - Python Keywords and Identifiers](https://www.youtube.com/watch?v=UIFhLzyxU_I)**
    - Specifically for beginners; explains keywords, identifiers, naming rules, and gives practical variable naming demonstrations in Python code.[^9]
- **[Python Identifiers, Keywords, Indentations and Multi-line statements (Beginner)](https://www.youtube.com/watch?v=_sLmgF8p1OI)**
    - Covers all three essentials — identifiers, keywords, and proper indentation — with demonstrations and beginner tips.[^10]
- **[Keywords and Identifiers in Python](https://www.youtube.com/watch?v=QmSL27U7RDc)**
    - Short, beginner-focused explanation of the role of keywords and identifiers in Python, with examples.[^11]
- **[Python Indentation (Python Beginner Tutorial)](https://www.youtube.com/watch?v=l4CdyZPDYE4)**
    - Dedicated tutorial on Python’s indentation, showing why it matters, common errors, and correct usage for functions, loops, and conditionals.[^12]
- **[Keywords, Identifiers, Functions, Indentation in PYTHON (Lecture)](https://www.youtube.com/watch?v=qnAzpwFdJU8)**
    - A class-style explanation of everything from identifiers and keywords to indentation, making it easy for new learners to follow.[^13]

***

Watching a few of these videos alongside your written practice will help reinforce your understanding and help identify and avoid common beginner errors.
<span style="display:none">[^17][^14][^15][^16]</span>

<div style="text-align: center">⁂</div>

[^8]: https://www.youtube.com/watch?v=BCXwfkZJfTM

[^9]: https://www.youtube.com/watch?v=UIFhLzyxU_I

[^10]: https://www.youtube.com/watch?v=_sLmgF8p1OI

[^11]: https://www.youtube.com/watch?v=QmSL27U7RDc

[^12]: https://www.youtube.com/watch?v=l4CdyZPDYE4

[^13]: https://www.youtube.com/watch?v=qnAzpwFdJU8

[^14]: https://www.youtube.com/watch?v=wwfvaAQZGbQ

[^15]: https://www.youtube.com/watch?v=JvMwnGY2EjU

[^16]: https://www.scaler.com/topics/python/python-keywords-and-identifiers/

[^17]: https://www.youtube.com/watch?v=tpML8LT_Op8


## Comments and document interlude in Python

Writing clear, maintainable code is essential in programming. In Python, **comments** and **docstrings** (documentation strings) are tools that let you explain what your code does, both for yourself and for others who may read your code later. As a beginner, learning the difference between comments and docstrings and knowing how to use each one will greatly improve the readability and usability of your Python programs.[^18][^19][^20][^21]

***

### 1. Comments in Python

**What are comments?**
Comments are simple notes in your source code. Python ignores them—they aren't executed, but they help explain what's going on for anyone reading the code (including you, later!).

#### How to Write Comments

- **Single-line comment:** Start with a `#`
- **Inline comment:** Write after code on the same line

**Example:**

```python
# This is a single-line comment
print("Hello, World!")  # This is an inline comment
```


#### Multi-line Comments

Python does not have a specific way for block comments, but you can write several lines each starting with `#`:

```python
# This is a comment
# that goes over
# several lines
```

You might also see triple-quoted strings used as block comments, but technically these are ignored string literals, not comments:

```python
"""
This is often used as a 'multiline comment'
but is actually a string not assigned to a variable.
"""
```

It's better to stick to `#` for real comments.[^19][^20][^22][^18]

***

### 2. Docstrings (Documentation Strings)

**What are docstrings?**
Docstrings are special strings used to document Python modules, functions, classes, and methods. They're written right after the `def` or `class` line, inside triple quotes (`"""`).
Unlike regular comments, docstrings are accessible at runtime using tools like the `help()` function.[^20][^21][^23][^19]

#### How to Write a Docstring

- Start and end with triple quotes
- Place directly under the object you are documenting

**Basic Function Example:**

```python
def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b
```

You can view this docstring with:

```python
help(add)
```

**Output:**

```
Help on function add in module __main__:

add(a, b)
    Add two numbers and return the result.
```


#### Multi-line Docstrings

For more complex objects, multi-line docstrings describe parameters, returns, errors, and more:

```python
def divide(a, b):
    """
    Divide two numbers and return the result.
    
    Parameters:
    a (float): Numerator
    b (float): Denominator
    
    Returns:
    float: The division result
    
    Raises:
    ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
```

This is the format recommended by Python’s style guide (PEP 257), and it's the standard for many big Python projects.[^21][^23]

***

### 3. Comments vs Docstrings (Key Differences)

| Feature | Comments | Docstrings |
| :-- | :-- | :-- |
| Syntax | `#` | `"""Docstring"""` (triple quotes) |
| Purpose | Explanatory notes for developer | Document functions, classes, modules |
| Accessible at runtime? | No | Yes (with help() or `__doc__`) |
| Scope | Anywhere in source code | First line in function/class/module |
| Good for | Why/how details, TODOs | What the thing does, usage docs |


***

### 4. Examples

**Single-line Comment:**

```python
# Calculate the area of a circle
area = 3.14 * (radius ** 2)
```

**Inline Comment:**

```python
x = y + 2  # Add 2 to y
```

**Function with Docstring and Comments:**

```python
def greet(name):
    """
    Print a greeting message to the user.
    """
    # Create the greeting message
    message = f"Hello, {name}!"
    print(message)
```

**Accessing Docstring:**

```python
print(greet.__doc__)
# Output: Print a greeting message to the user.
```


***

### 5. Best Practices

- Use **comments** for explanations about sections of code, especially tricky or non-obvious parts.
- Use **docstrings** for documenting the purpose, parameters, and outputs of functions, methods, and classes.
- Keep comments clear and concise. Avoid obvious comments.
- Write docstrings so they can be easily used by documentation tools or other developers.[^23][^18][^19]

***

## Learn More (Good YouTube Videos)

- ["How to Write Clear Python Code: Comments and Docstrings"](https://www.youtube.com/watch?v=uDBGMjaSJAY) – covers comments and docstrings for beginners, with practical examples.[^24]
- ["Python comments vs. docstrings: What, how, and why"](https://www.youtube.com/watch?v=wI1hZHjddwk) – compares comments and docstrings, and when to use each.[^25]

***

## Additional References

- [GeeksforGeeks - Python Docstrings][^26]
- [W3Schools - Python Comments][^18]
- [Beginner's Guide to Python Docstrings - ZeroToMastery][^19]
- [Real Python - Documenting Python Code][^27][^22]
- [Dataquest - Documenting with Docstrings][^23]
- [Programiz - Python Docstrings][^20]
- [TutorialsPoint - Python Docstrings][^21]

All these resources offer great, beginner-friendly learning materials on comments and documentation in Python.

***

Recognizing when and why to use comments versus docstrings will improve both your understanding of your own code and your ability to communicate with others in the Python community. Happy coding!
<span style="display:none">[^28][^29][^30][^31]</span>

<div style="text-align: center">⁂</div>

[^18]: https://www.w3schools.com/python/python_comments.asp

[^19]: https://zerotomastery.io/blog/python-docstring/

[^20]: https://www.programiz.com/python-programming/docstrings

[^21]: https://www.tutorialspoint.com/python/python_docstrings.htm

[^22]: https://realpython.com/python-comments-guide/

[^23]: https://www.dataquest.io/blog/documenting-in-python-with-docstrings/

[^24]: https://www.youtube.com/watch?v=uDBGMjaSJAY

[^25]: https://www.youtube.com/watch?v=wI1hZHjddwk

[^26]: https://www.geeksforgeeks.org/python/python-docstrings/

[^27]: https://realpython.com/documenting-python-code/

[^28]: https://stackoverflow.com/questions/19074745/docstrings-vs-comments

[^29]: https://www.coursera.org/tutorials/python-comment

[^30]: https://www.machinelearningmastery.com/comments-docstrings-and-type-hints-in-python-code/

[^31]: https://pandas.pydata.org/docs/development/contributing_docstring.html


## Command Line Arguments and User Input in Python

Understanding how to get input from users is a crucial building block for interactive Python programs. Python offers two primary ways to receive input:

1. **Command Line Arguments** (when running the script)
2. **User Input** during program execution (with `input()`)

Below, you'll find beginner-friendly explanations, code examples, and video resources for both methods.

***

## 1. Command Line Arguments

### What Are Command Line Arguments?

Command line arguments are **values provided to your program when you run it from a terminal or command prompt**. They allow users to control your script’s behavior without changing its code.[^32][^33][^34]

### How to Access Command Line Arguments

You can access command line arguments in Python using the `sys` module. The arguments are stored as a list in `sys.argv`:

- `sys.argv` is always the script name.
- `sys.argv[1:]` are the actual arguments passed by the user.

**Example 1: Print All Command Line Arguments**

```python
import sys

print("Script name:", sys.argv)
print("Arguments:", sys.argv[1:])
```

Run from the terminal:

```
python myscript.py apple banana orange
```

Output:

```
Script name: myscript.py
Arguments: ['apple', 'banana', 'orange']
```

**Example 2: Adding Numbers from Command Line Arguments**

```python
import sys

# Skip script name, get numbers
numbers = sys.argv[1:]

# Convert strings to integers and sum them
total = sum(int(num) for num in numbers)
print("The sum is", total)
```

Running `python add.py 5 9 10` will print:

```
The sum is 24
```


### Advanced: Using argparse

For advanced use, such as named or optional arguments, use the `argparse` module.

```python
import argparse

parser = argparse.ArgumentParser(description="Add numbers.")
parser.add_argument("numbers", nargs="+", type=int, help="Numbers to add")
args = parser.parse_args()

print("Sum:", sum(args.numbers))
```


***

## 2. Getting User Input (`input()` Function)

### What Is User Input?

Sometimes you want to ask users for data while your program is running. This is done using the built-in `input()` function.[^35][^36]

**Example 1: Simple User Input**

```python
name = input("Enter your name: ")
print("Hello,", name)
```

When run, the program waits for the user to type their name.

**Example 2: Numeric Input and Data Conversion**

By default, `input()` always returns a string. To use numbers, convert the input:

```python
age = int(input("Enter your age: "))
print("Next year you’ll be", age + 1)
```

**Example 3: Repeated Prompt Until Valid Input**

```python
while True:
    user_input = input("Enter an integer: ")
    if user_input.isdigit():
        num = int(user_input)
        print("You entered:", num)
        break
    else:
        print("Invalid input! Please enter a valid integer.")
```


***

## 3. Command Line Arguments vs. User Input

| Feature | Command Line Arguments | User Input (`input()`) |
| :-- | :-- | :-- |
| When Provided? | When starting the script | During program execution |
| How Provided? | As part of the command | In response to a prompt |
| Usage | `sys.argv`, `argparse` | `input()` |
| Typical Use Case | Batch scripts, automation | Interactive programs/questions |
| Returns | Strings (need conversion often) | Strings (need conversion often) |


***

## 4. YouTube Video Tutorials

- [Python Command Line Arguments tutorial for Beginners (YouTube)](https://www.youtube.com/watch?v=mZbRRQMJ7Ew)[^37]
- [Python User Input \& Control Flow | Python tutorial (YouTube)](https://www.youtube.com/watch?v=N94vSNBF-EI)[^38]
- [Accessing command line arguments in Python (YouTube)](https://www.youtube.com/watch?v=TOxsbFX2PJc)[^39]

***

## 5. Further Learning \& References

- [GeeksforGeeks – Command Line Arguments in Python][^32]
- [DigitalOcean – How to Receive User Input in Python][^35]
- [TutorialsPoint – Python Command-Line Arguments][^33]
- [W3Schools – Python User Input][^36]
- [StackOverflow – User input and command line arguments][^40]
- [Real Python – Build Command-Line Interfaces With argparse][^41]

Explore these to deepen your understanding!

***

With these tools, you can make your Python programs interactive and flexible, allowing users to provide data either before the program runs (arguments) or during its run (input prompts).
<span style="display:none">[^42]</span>

<div style="text-align: center">⁂</div>

[^32]: https://www.geeksforgeeks.org/python/command-line-arguments-in-python/

[^33]: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

[^34]: https://www.digitalocean.com/community/tutorials/python-command-line-arguments

[^35]: https://www.digitalocean.com/community/tutorials/how-to-receive-user-input-python

[^36]: https://www.w3schools.com/python/python_user_input.asp

[^37]: https://www.youtube.com/watch?v=mZbRRQMJ7Ew

[^38]: https://www.youtube.com/watch?v=N94vSNBF-EI

[^39]: https://www.youtube.com/watch?v=TOxsbFX2PJc

[^40]: https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments

[^41]: https://realpython.com/command-line-interfaces-python-argparse/

[^42]: https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments

## Python Basic Data Types and Variables

## **What are Data Types and Variables? — Analogy**

**Analogy:**
Imagine you have a set of labeled boxes of different shapes and sizes. You use these boxes to store different things — apples, your age on a piece of paper, a yes/no answer written on a card, etc. The **type** of the box (big, small, transparent, etc.) tells you what’s inside and how to handle it. The **label** on the box is the variable name you use to refer to it.

- **Variable:** The label on a box that allows you to find and use what’s inside.
- **Data Type:** The kind of thing you store in the box (number, word, true/false, etc.).

***

## **Basic Data Types in Python**

| Type | What it represents | Example value | Analogy |
| :-- | :-- | :-- | :-- |
| int | Whole numbers | 5, -3, 42 | Box for marbles (can’t cut in half) |
| float | Decimal/real numbers | 5.7, -0.2, 3.1415 | Box for sand (can have fractions) |
| str (string) | Text (letters, words, sentences) | "hello", "42" | Box for letters/notes |
| bool | True or False (Yes or No) | True, False | Box with a switch (on or off) |


***

## **How to Create Variables and Assign Data Types**

**In Python, you don’t declare the type in advance—the box is smart! Python looks at what you put inside and figures it out for you.**

```python
# Integer variable (whole number)
age = 25

# Float variable (number with decimal)
height = 5.9

# String variable (text)
name = "Arun"

# Boolean variable (True/False)
is_student = True
```

*The variables (age, height, name, is_student) are labels for the boxes. The type of what’s inside each box is decided when you assign a value.*

***

### **More Beginner Analogies**

- Think of a **variable** as giving a name to a box—if you say `name`, you’re asking Python to bring you the box labeled "name."
- A **string** is like a sentence written on paper.
- An **int** is counting apples.
- A **float** is measuring the weight of apples on a scale (e.g., 1.5 kg).
- **Boolean** is a YES/NO checkbox.

***

### **How to Check Types**

You can ask Python: “What’s inside this box?”

```python
print(type(age))        # Output: <class 'int'>
print(type(height))     # Output: <class 'float'>
print(type(name))       # Output: <class 'str'>
print(type(is_student)) # Output: <class 'bool'>
```


***

### **Why Do Types Matter?**

- If you try to put apples in a box made for water, it might spill (type errors).
- Operations depend on type: You can add numbers, but you *join* strings.

**Example:**

```python
x = 10
y = "10"
print(x + x)  # 20 (int + int)
print(y + y)  # "1010" (str + str)
```

- Here, `x` is a number; adding gives math. `y` is text; adding joins the text.

***

### **Type Conversion (Changing Box Types)**

You can tell Python to change the box, like pouring water into a measuring cup.

```python
num_str = "123"
num = int(num_str)     # Converts string to integer: 123
height_str = str(height)  # float to string: "5.9"
```


***

## **In Summary:**

- **Variables** are labels for storage in memory.
- **Data types** decide *what* can be stored and *what* you can do with it.
- Python’s main basic types for beginners: **int**, **float**, **str**, **bool**.

**Programming in Python is about creating and using these labeled boxes to process and keep track of your data. Once you master this, you’re well on your way to coding!**

***

**Example for beginner practice:**

```python
your_name = "Priya"
your_age = 18
has_pets = False
gpa = 8.7

print("Name:", your_name)
print("Age:", your_age)
print("Has pets?", has_pets)
print("GPA:", gpa)
```


***

**Tip:**
Always use meaningful names for your variables (like labels on boxes) so you always know what’s inside!Here’s a simple analogy and a beginner’s guide to **Python Basic Data Types and Variables**:

***

## Analogy for Beginners

Imagine your **computer’s memory is a series of labeled jars** on a shelf.

- The **label** on the jar is your variable name (like `age` or `username`).
- What you put in the jar is your **data** (like the number 25 or the word "Priya").
- The **kind** of stuff allowed in a jar is its **data type** (e.g. only marbles (=numbers), only sand (=decimals), only notes (=words), only YES/NO sticker (=True/False)).

Python automatically picks the right jar for the stuff you want to store!

***

## Basic Data Types in Python

| Data Type | Real-life Analogy | Example in Python | Notes |
| :-- | :-- | :-- | :-- |
| int | Counting marbles in a jar | `a = 7` | Whole numbers like 0, -5, 24 |
| float | Weight of sugar on a scale | `b = 2.5` | Decimal numbers like 5.0, -0.75, 3.14 |
| str | A sticky note with words | `c = "hello"` | Text, like "python", "21", "hello world" |
| bool | Switch for ON/OFF or YES/NO | `d = True` | Either `True` or `False` (notice capitalization) |


***

## Creating Variables and Assigning Data Types

You don’t tell Python the type — Python figures it out for you by what you put in!

```python
# Integer variable (whole number)
age = 18

# Float variable (number with decimals)
GPA = 9.45

# String variable (text)
name = "Priya"

# Boolean variable (True/False)
has_pet = False
```


***

## Checking Types

You can ask Python what type your variable is using `type(variable)`:

```python
print(type(age))      # <class 'int'>
print(type(GPA))      # <class 'float'>
print(type(name))     # <class 'str'>
print(type(has_pet))  # <class 'bool'>
```


***

## Why Data Types Matter

- **Numbers** can be added, subtracted, etc.:
`print(age + 2)`  \# 20
- **Strings** can be joined together:
`print(name + " rocks!")`  \# Priya rocks!
- **Booleans** can control logic:
`if has_pet: print("You have a pet!")`

If you mix them, you get an error!

```python
print(age + name)     # ERROR! Can't add int and str
```


***

## Changing (Converting) Types

Sometimes you need to change a jar’s type:

```python
num_str = "100"
num_int = int(num_str)   # Converts string to integer (100)
print(num_int + 2)       # 102

float_str = "3.14"
num_float = float(float_str)  # Converts to float (3.14)
```


***

## Beginner Practice Example

```python
player = "Alex"
score = 12
is_winner = True
points = 12.5

print("Player:", player)
print("Score:", score)
print("Winner?", is_winner)
print("Bonus points:", points)
```


***

**Summary:**

- **Variables** are like jars with labels.
- **Data types** decide what each jar can hold.
- Let your variable’s name describe what’s inside!

If you remember the labeled-jar analogy, you’ll understand variables and types easily—just like sorting foods in your kitchen!

Here are some excellent **YouTube videos and references** for beginners on "Python Basic Data Types and Variables," each featuring analogies, code examples, and step-by-step explanations:

***

### YouTube Videos for Beginners

- **[Learn Python Variables \& Data Types with Code Examples - Python Simplified (2025)](https://www.youtube.com/watch?v=KeA39II7AO8)**
    - Features a real-life analogy: variables as labeled boxes for your data, and breaks down int, float, string, and boolean types with lots of easy-to-follow examples. Covers how to name variables, convert types, and why type matters for different operations.[^43]
- **[Variables and Data Types in Python are Easy - Quoc Dat Phung (2024)](https://www.youtube.com/watch?v=t1KIazbIlzk)**
    - A friendly explainer going over the four core types (int, float, str, bool) with variable naming, type checking, and beginner common mistakes—with relatable analogies for kids and adults alike.[^44]
- **[Data Types in Python | Python for Beginners - Alex The Analyst (2022)](https://www.youtube.com/watch?v=ppsCxnNm-JI)**
    - A beginner’s video showing each type (integer, float, string, boolean) in Python, with on-screen live coding and result outputs. Also shows what kind of operations you can do on each type.[^45]
- **[Python variables for beginners (2022)](https://www.youtube.com/watch?v=LKFrQXaoSMQ)**
    - Explains what variables are, the four basic types, and how to display and combine variables in print statements. Great for absolute beginners.[^46]
- **[Variables \& Data Types In Python - Edureka (2023)](https://www.youtube.com/watch?v=WbPf4MCIo_U)**
    - Covers all the core types, plus briefly introduces more advanced types like lists and dictionaries for extra curiosity.[^47]
- **[Python Full Course❤ | Variables \& Data Types | Lecture 1 (2024)](https://www.youtube.com/watch?v=t2_Q2BRzeEE)**
    - Start-to-finish run-through with detailed examples and easy language, ideal if you want both quick intro and in-depth explanations together.[^48]

***

### Written References

- **Real Python Beginners Guide:**
Learn the basics of Python variables, data types, and type conversion with friendly explanation:
[https://realpython.com/python-data-types/](https://realpython.com/python-data-types/)
- **w3schools Python Data Types Chapter:**
Simple explanations and live code test console:
[https://www.w3schools.com/python/python_datatypes.asp](https://www.w3schools.com/python/python_datatypes.asp)

***

These video links and references will help you understand Python variables and data types with easy analogies and code demonstrations—the perfect combo for absolute beginners!
<span style="display:none">[^49][^50][^51][^52]</span>

<div style="text-align: center">⁂</div>

[^43]: https://www.youtube.com/watch?v=KeA39II7AO8

[^44]: https://www.youtube.com/watch?v=t1KIazbIlzk

[^45]: https://www.youtube.com/watch?v=ppsCxnNm-JI

[^46]: https://www.youtube.com/watch?v=LKFrQXaoSMQ

[^47]: https://www.youtube.com/watch?v=WbPf4MCIo_U

[^48]: https://www.youtube.com/watch?v=t2_Q2BRzeEE

[^49]: https://www.youtube.com/watch?v=INGJh9DEaBM

[^50]: https://www.youtube.com/watch?v=TTepNRy0wj8

[^51]: https://www.youtube.com/watch?v=wUSDVGivd-8

[^52]: https://www.youtube.com/watch?v=ORCuz7s5cCY