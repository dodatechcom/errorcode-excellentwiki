---
title: "[Solution] Python FileNotFoundError — File Not Found Fix"
description: "Fix Python FileNotFoundError: No such file or directory. Check file paths, use os.path.exists(), and handle file operations safely."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 100
---

# FileNotFoundError — File Not Found Fix

A `FileNotFoundError` is raised when a file or directory requested by `open()`, `os.stat()`, or similar I/O functions does not exist. This is a subclass of `OSError` (which replaced the older `IOError` in Python 3.3+).

## Description

`FileNotFoundError` is the most common file I/O error in Python. It means the path you provided does not resolve to an existing file or directory.

Common scenarios:

- **Relative path from wrong working directory** — script is run from a different directory than expected.
- **Typo in filename** — `data.csv` vs `data.csv` vs `Data.csv`.
- **Case sensitivity on Linux** — `File.txt` and `file.txt` are different files.
- **Special characters in filename** — spaces, unicode, or shell metacharacters not quoted.
- **File was deleted or moved** — path was valid once but no longer is.

## Common Causes

```python
# Cause 1: Relative path from wrong working directory
# If you run "python scripts/process.py" from /home/user
with open("data.csv") as f:  # Looks for /home/user/data.csv
    content = f.read()

# Cause 2: Typo in filename
with open("config.json") as f:  # Actual file is "config.JSON" or "config.jsonc"
    data = f.read()

# Cause 3: Case sensitivity
with open("README.md") as f:  # File is actually "readme.md" on Linux
    content = f.read()

# Cause 4: Not using raw strings on Windows
with open("C:\new_folder\file.txt") as f:  # \n and \f are escape sequences
    content = f.read()

# Cause 5: File doesn't exist yet
import json
with open("output.json") as f:  # FileNotFoundError if output.json hasn't been created
    data = json.load(f)
```

## Solutions

### Fix 1: Use os.path.exists() to check before opening

```python
import os

# Wrong
with open("data.csv") as f:
    content = f.read()

# Correct
if os.path.exists("data.csv"):
    with open("data.csv") as f:
        content = f.read()
else:
    print("File not found: data.csv")
```

### Fix 2: Use pathlib for robust path handling

```python
from pathlib import Path

# Wrong — string concatenation for paths
filepath = "data" + "/" + "input.csv"

# Correct — pathlib handles separators automatically
filepath = Path("data") / "input.csv"

if filepath.exists():
    content = filepath.read_text()
else:
    print(f"File not found: {filepath}")
```

### Fix 3: Use absolute paths or resolve relative to script location

```python
from pathlib import Path

# Wrong — depends on current working directory
with open("config.json") as f:
    config = f.load(f)

# Correct — resolve relative to the script's directory
script_dir = Path(__file__).parent
config_path = script_dir / "config.json"
with open(config_path) as f:
    config = f.load(f)
```

### Fix 4: Use raw strings for Windows paths

```python
# Wrong — backslashes are escape sequences
path = "C:\Users\new\file.txt"  # \U and \n are interpreted

# Correct — raw string prefix
path = r"C:\Users\new\file.txt"

# Also correct — forward slashes work on Windows too
path = "C:/Users/new/file.txt"
```

### Fix 5: Create the file before reading from it

```python
import json

# Wrong — file doesn't exist yet
with open("output.json") as f:
    data = json.load(f)

# Correct — create the file first, then read it
output_path = Path("output.json")
if not output_path.exists():
    output_path.write_text("{}")

with open(output_path) as f:
    data = json.load(f)
```

### Fix 6: Use try/except for graceful error handling

```python
# Wrong — crashes without explanation
content = open("missing.txt").read()

# Correct — provides a helpful error message
try:
    with open("missing.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
    content = ""
```

## Related Errors

- [PermissionError](#) — file exists but you don't have read access.
- [IsADirectoryError](#) — you passed a directory path to `open()` where a file was expected.
- [OSError](#) — broader I/O error category (parent of `FileNotFoundError`).
