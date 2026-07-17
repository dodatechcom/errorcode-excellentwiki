---
title: "[Solution] Python TabError — Inconsistent Tabs and Spaces Fix"
description: "Fix Python TabError caused by mixing tabs and spaces. Configure editor for 4 spaces, use autopep8, or convert tabs to spaces."
languages: ["python"]
severities: ["error"]
error_types: ["syntax"]
weight: 55
---

# TabError — Inconsistent Tabs and Spaces Fix

A `TabError` is raised when a Python file contains inconsistent use of tabs and spaces for indentation. Python 3 does not allow mixing tabs and spaces in the same block.

## Description

In Python 3, indentation is significant — it defines code blocks. The language specification forbids mixing tabs and spaces. If your file uses tabs in some places and spaces in others (within the same logical block), Python raises `TabError`. Python 2 was more lenient, treating a tab as equivalent to 8 spaces.

Common scenarios:

- **Mixed editor settings** — one editor uses tabs, another uses spaces.
- **Copy-pasting code** — source uses different indentation.
- **Collaborative editing** — team members with different editor configs.
- **Converted files** — files converted from other languages with different conventions.
- **Invisible characters** — tabs and spaces look similar but are different bytes.

## Common Causes

```python
# Cause 1: Mixed tabs and spaces in same block
def process():
→   x = 1      # Tab
    y = 2      # 4 spaces
    if x == 1:
→       z = 3  # Tab + spaces
        w = 4  # 4 spaces

# Cause 2: Tab at start, spaces in continuation
def calculate():
→   result = (1 +
    2 +         # Spaces after tab
    3)

# Cause 3: Copy-pasted code with different indentation
def function_a():
→   do_something()  # Tab-indented

def function_b():
    do_something()  # Space-indented

# Both are fine separately, but mixing in one file causes issues

# Cause 4: Editor configured with tabs but some lines auto-converted
def mixed():
→   x = 1
    y = 2  # Editor auto-converted this line
→   z = 3
```

## Solutions

### Fix 1: Configure your editor to use spaces consistently

```python
# In VS Code, add to settings.json:
# {
#     "editor.insertSpaces": true,
#     "editor.tabSize": 4,
#     "files.trimTrailingWhitespace": true
# }

# In Vim, add to .vimrc:
# set expandtab
# set tabstop=4
# set shiftwidth=4

# In Sublime Text, add to Preferences.sublime-settings:
# "tab_size": 4,
# "translate_tabs_to_spaces": true
```

### Fix 2: Convert all tabs to spaces with expand command

```bash
# Wrong — file has mixed tabs and spaces
cat -A myfile.py  # Shows ^I for tabs

# Correct — convert tabs to spaces
expand -t 4 myfile.py > fixed.py
mv fixed.py myfile.py
```

### Fix 3: Use autopep8 to fix automatically

```python
# Install autopep8
# pip install autopep8

# Run on file
# autopep8 --in-place myfile.py

# Or in Python
import autopep8
with open("myfile.py", "r") as f:
    code = f.read()
fixed = autopep8.fix_code(code)
with open("myfile.py", "w") as f:
    f.write(fixed)
```

### Fix 4: Use Python's tabnanny module to detect issues

```python
import tabnanny

# Check a file for indentation issues
filename = "myfile.py"
try:
    tabnanny.check(filename)
    print("No indentation issues found")
except tabnanny.NannyNag as e:
    print(f"Indentation error: {e}")

# Or use it from command line
# python -m tabnanny myfile.py
```

### Fix 5: Normalize with tokenize module

```python
import tokenize
import io

# Detect mixed indentation
with open("myfile.py", "rb") as f:
    try:
        tokens = tokenize.tokenize(f.readline)
        for token in tokens:
            pass
        print("File tokenizes successfully — no TabError")
    except tokenize.TokenError as e:
        print(f"Token error: {e}")
```

### Fix 6: Use .editorconfig for team consistency

```ini
# .editorconfig file in project root
root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

## Related Errors

- [IndentationError](../indentationerror) — incorrect indentation level (not mixed tabs/spaces).
- [SyntaxError](../syntaxerror) — general syntax error.
- [SyntaxError](../syntaxerror) — invalid Python syntax.
