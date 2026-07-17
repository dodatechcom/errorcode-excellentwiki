---
title: "[Solution] Python IndentationError — Indentation Fix"
description: "Fix Python IndentationError: unexpected indent or unindent. Understand Python's indentation rules and fix spacing issues."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
weight: 70
---

# IndentationError — Indentation Fix

An `IndentationError` is raised when Python encounters inconsistent or incorrect whitespace. Python uses indentation to define code blocks — every `if`, `for`, `while`, `def`, `class`, and `with` block requires indented code.

## Description

Python enforces indentation at the syntax level. Unlike most languages that use braces `{}` for blocks, Python uses leading whitespace. This makes indentation both structural and functional.

Common error messages:

- **`unexpected indent`** — code is indented when it shouldn't be.
- **`unindent does not match any outer indentation level`** — mixed tabs and spaces or inconsistent spacing.
- **`expected an indented block`** — a block header (`if`, `def`, etc.) is followed by no indented code.
- **`IndentationError: unindent may not match indentation level`** — tabs and spaces are mixed in confusing ways.

Python 3 does not allow mixing tabs and spaces. The standard convention is 4 spaces per indent level (PEP 8).

## Common Causes

```python
# Cause 1: Mixed tabs and spaces
def greet():
    name = "Alice"      # 4 spaces
    message = "Hello"   # 1 tab — ERROR

# Cause 2: Unexpected indent
x = 10
    y = 20  # IndentationError: unexpected indent

# Cause 3: Missing indented block after header
def calculate():
# IndentationError: expected an indented block after 'def'

# Cause 4: Inconsistent indent levels
if True:
    x = 1       # 4 spaces
      y = 2     # 6 spaces — ERROR

# Cause 5: Dedent to wrong level
def outer():
    def inner():
        x = 1
    return x  # ERROR — 'return' is at outer's indent level but references inner's variable
```

## Solutions

### Fix 1: Use consistent spaces everywhere (4 spaces per level)

```python
# Wrong — mixed tabs and spaces
def greet():
    name = "Alice"
	message = "Hello"

# Correct — all spaces, 4 per level
def greet():
    name = "Alice"
    message = "Hello"
```

### Fix 2: Configure your editor to use spaces

In most editors, set these options:

- **VS Code**: `"editor.insertSpaces": true, "editor.tabSize": 4`
- **PyCharm**: Settings > Editor > Code Style > Python > Tabs and Indents > set to 4 spaces
- **Sublime Text**: `"tab_size": 4, "translate_tabs_to_spaces": true`

### Fix 3: Don't indent code that isn't inside a block

```python
# Wrong
x = 10
    y = 20  # Nothing above this is a block header

# Correct
x = 10
y = 20
```

### Fix 4: Always provide a body after block headers

```python
# Wrong
def calculate():
print("doing nothing")

# Correct — either add a body or use 'pass'
def calculate():
    print("doing nothing")

# Or if you intentionally want an empty block:
def calculate():
    pass
```

### Fix 5: Fix dedent alignment

```python
# Wrong — return is at wrong level
def outer():
    def inner():
        x = 1
    return x  # Trying to return inner's x from outer

# Correct
def outer():
    def inner():
        x = 1
    return x  # This works because inner() is defined inside outer()
```

### Fix 6: Use autopep8 to fix indentation automatically

```bash
# Install autopep8
pip install autopep8

# Auto-fix indentation issues in a file
autopep8 --in-place myfile.py

# Or preview changes without writing
autopep8 --diff myfile.py
```

## Related Errors

- [SyntaxError](../syntaxerror) — broader category; `IndentationError` is a subclass of `SyntaxError`.
- [TabError](#) — specific to tab/space mixing (subclass of `SyntaxError` in Python 3).
- [TypeError](../typeerror) — runtime type mismatch, unrelated to whitespace.
