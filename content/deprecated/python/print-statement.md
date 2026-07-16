---
title: "[Solution] Python print Statement Deprecated — Use print() Function"
description: "Replace Python 2 print statement with Python 3 print() function. Migration guide with 2to3 tool and manual conversion steps."
deprecated_function: "print statement"
replacement_function: "print()"
languages: ["python"]
deprecated_since: "Python 3.0"
removed_in: "Python 3.0"
error_message: "SyntaxError: Missing parentheses in call to 'print'"
tags: ["print", "python2", "python3", "2to3"]
weight: 60
---

# [Solution] Python print Statement Deprecated — Use print() Function

The `print` statement was the most visible change in Python 3. The statement syntax (`print "hello"`) was replaced with a function call (`print("hello")`). This change unified the language syntax and made `print` consistent with other built-in functions. If you are migrating code from Python 2, this is almost always the first change you need to make.

## What You'll See

In Python 3, if you use the old print statement:

```python
print "Hello, World!"
```

You get:

```
File "script.py", line 1
    print "Hello, World!"
          ^
SyntaxError: Missing parentheses in call to 'print'
```

If you see this error, you are running Python 2 syntax under Python 3.

## Why Deprecated

The `print` statement was changed to a function in Python 3 for several reasons:

- **Consistency**: Functions are first-class objects; a statement is not. Making `print` a function allowed it to be used in lambdas, `map()`, `filter()`, and as a callback.
- **Extensibility**: As a function, `print()` accepts keyword arguments like `sep`, `end`, `file`, and `flush`, which were awkward to implement as statement modifiers.
- **Reduced syntax confusion**: The statement syntax required special parsing rules (e.g., trailing comma for no newline) that were inconsistent with the rest of the language.

## Old Code (Python 2 Statement)

```python
# Simple print
print "Hello, World"

# Print with no newline (trailing comma)
print "Hello",

# Print to stderr
import sys
print >> sys.stderr, "Error occurred"

# Print multiple values
print "Name:", "Alice", "Age:", 30

# Print a variable
x = 42
print x

# Print with formatting
name = "Alice"
print "Hello, %s!" % name
```

## New Code (Python 3 Function)

```python
# Simple print — add parentheses
print("Hello, World")

# Print with no newline — use end keyword
print("Hello", end="")

# Print to stderr — use file keyword
import sys
print("Error occurred", file=sys.stderr)

# Print multiple values — use sep keyword
print("Name:", "Alice", "Age:", 30)
# With custom separator
print("Name:", "Alice", "Age:", 30, sep=" ")

# Print a variable
x = 42
print(x)

# Print with formatting
name = "Alice"
print(f"Hello, {name}!")  # f-string (Python 3.6+)
print("Hello, {}!".format(name))  # .format() method
```

## Migration Using the 2to3 Tool

Python ships with an automated conversion tool called `2to3`. It handles the print statement conversion and many other Python 2 to 3 changes:

```bash
# Preview changes without modifying files
2to3 -w -n script.py

# Convert an entire directory
2to3 -w -n /path/to/project/

# Preview changes only for the print fixer
2to3 -f print -w -n script.py
```

The `-w` flag writes changes to files. The `-n` flag skips creating backup files. Always review the diff after conversion.

## Migration Using __future__ for Python 2/3 Compatibility

If you need code that runs under both Python 2 and Python 3, use the `__future__` import at the top of every file:

```python
from __future__ import print_function

# Now this works in both Python 2 and Python 3
print("Hello, World")

# Also enables the keyword arguments
print("Hello", end=" ")
print("World")
```

Place the `from __future__` import as the first statement in the file (after any module docstrings and comments).

## Migration Steps

1. **Run 2to3 in preview mode** to see all changes:

```bash
2to3 -l  # List all available fixers
2to3 -d script.py  # Show diff of proposed changes
```

2. **Apply the print fixer** to convert all print statements:

```bash
2to3 -f print -w script.py
```

3. **Manually review** cases where the trailing comma was used for suppressing newlines. Convert `print "x",` to `print("x", end="")`.

4. **Replace `%` string formatting** with f-strings or `.format()` for modern Python 3 code.

5. **Search for any remaining print statements**:

```bash
grep -rn "^[[:space:]]*print " --include="*.py" /path/to/project/
```

6. **Run your test suite** under Python 3 to verify all output is correct.
