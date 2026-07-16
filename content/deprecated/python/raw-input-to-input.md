---
title: "[Solution] Python raw_input() Deprecated — Use input() Instead"
description: "Replace deprecated raw_input() with input() in Python 3. Migration guide for Python 2 to 3 input handling."
deprecated_function: "raw_input"
replacement_function: "input"
languages: ["python"]
deprecated_since: "Python 3.0"
removed_in: "Python 3.0"
error_message: "NameError: name 'raw_input' is not defined"
tags: ["raw_input", "input", "python2", "python3"]
weight: 70
---

# [Solution] Python raw_input() Deprecated — Use input() Instead

In Python 2, there were two input functions: `raw_input()` (which returned a string) and `input()` (which called `eval()` on the input). Python 3 removed `raw_input()` entirely and renamed it to `input()`. The old `input()` behavior was removed entirely for security reasons.

## What You'll See

If you run Python 2 code with `raw_input()` under Python 3:

```python
name = raw_input("Enter your name: ")
```

You get:

```
NameError: name 'raw_input' is not defined
```

## Why Deprecated

The change was made to eliminate a dangerous confusion:

- **Python 2 `raw_input()`**: Read input as a string. This is what most developers wanted.
- **Python 2 `input()`**: Read input, then passed it through `eval()`. This meant a user could enter arbitrary Python expressions, which is a serious security vulnerability.
- **Python 3 `input()`**: Always reads input as a string, equivalent to Python 2's `raw_input()`.
- **Python 3 `eval(input())`**: Explicitly used when you actually want to evaluate the input (rare and dangerous).

The rename made the safe behavior the default and forced developers to be explicit about evaluating input.

## Old Code (Python 2)

```python
# Read a string
name = raw_input("Enter your name: ")
print "Hello, " + name

# Read a number and convert
age = int(raw_input("Enter your age: "))

# Read with a prompt
choice = raw_input("Do you want to continue? (y/n): ")

# The dangerous Python 2 input() — do NOT use this
secret = input("Enter a Python expression: ")
# User could type: __import__('os').system('rm -rf /')
```

## New Code (Python 3)

```python
# Read a string — direct replacement
name = input("Enter your name: ")
print("Hello, " + name)

# Read a number and convert
age = int(input("Enter your age: "))

# Read with a prompt
choice = input("Do you want to continue? (y/n): ")

# If you actually need to evaluate input (use with extreme caution)
secret = eval(input("Enter a Python expression: "))
# Better: use ast.literal_eval for safe evaluation of literals
import ast
safe_value = ast.literal_eval(input("Enter a value: "))
```

## Migration Using 2to3

The `2to3` tool handles this conversion automatically:

```bash
# Preview changes
2to3 -f raw_input -d script.py

# Apply changes
2foraw_input -w script.py
```

The tool will replace all `raw_input()` calls with `input()` and all `input()` calls with `eval(input())` (which is correct but should be reviewed for security).

## Python 2/3 Compatibility

If you need code that runs under both Python 2 and Python 3:

```python
import sys

if sys.version_info[0] >= 3:
    input_func = input
else:
    input_func = raw_input

# Use input_func throughout your code
name = input_func("Enter your name: ")
```

Or simpler, using the `six` library:

```python
from six.moves import input

name = input("Enter your name: ")
```

## Migration Steps

1. **Find all raw_input() calls**:

```bash
grep -rn "raw_input" --include="*.py" /path/to/project/
```

2. **Replace every `raw_input()` with `input()`**. This is a direct rename with no behavior change.

3. **Find all `input()` calls** and determine if they rely on the Python 2 `eval()` behavior. Replace those with `eval(input())` or better yet, `ast.literal_eval(input())`.

4. **Run 2to3** if you have many files:

```bash
2to3 -f raw_input -w /path/to/project/
```

5. **Test all user input paths** in your application to verify prompts and data handling still work correctly.

6. **Search for other Python 2 patterns** that may also need migration:

```bash
grep -rn "print " --include="*.py" /path/to/project/
grep -rn "has_key\|except.*," --include="*.py" /path/to/project/
```
