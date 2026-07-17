---
title: "[Solution] Python IsADirectoryError — Tried to Open Directory as File Fix"
description: "Fix Python IsADirectoryError when trying to open a directory as a file. Check path with os.path.isdir() and fix path construction."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 60
---

# IsADirectoryError — Tried to Open Directory as File Fix

An `IsADirectoryError` is raised when you try to open, read, or write a path that is a directory, not a file. It's a subclass of `OSError`.

## Description

This error occurs when Python expects a file but receives a directory path. The path exists and is accessible, but it's a directory. This is common when path construction goes wrong or when a variable contains a directory instead of a file.

Common scenarios:

- **Forgetting to append filename** — `open("/home/user")` instead of `open("/home/user/file.txt")`.
- **Path concatenation error** — missing separator or filename.
- **Variable holds directory** — `filepath` is actually a directory path.
- **Trailing slash issues** — inconsistent path handling.
- **Extracting from archive** — entry is a directory, not a file.

## Common Causes

```python
# Cause 1: Forgetting to append filename
directory = "/home/user/documents"
with open(directory, "r") as f:  # IsADirectoryError

# Cause 2: Path concatenation error
base = "/home/user"
filename = ""
filepath = f"{base}/{filename}"  # Results in "/home/user/"
with open(filepath, "r") as f:  # IsADirectoryError

# Cause 3: Variable holds directory instead of file
import os
path = "/tmp"
if os.path.exists(path):
    with open(path, "r") as f:  # /tmp is a directory

# Cause 4: Glob returning directories
import glob
for path in glob.glob("/home/user/*"):
    with open(path, "r") as f:  # Some matches are directories

# Cause 5: Incorrect basename extraction
full_path = "/home/user/documents"
dirname = os.path.dirname(full_path)  # "/home/user"
basename = os.path.basename(full_path)  # "documents"
# Mixing up dirname and basename
with open(dirname, "r") as f:  # IsADirectoryError
```

## Solutions

### Fix 1: Check if path is a directory before opening

```python
import os

# Wrong
filepath = "/home/user/documents"
with open(filepath, "r") as f:
    content = f.read()

# Correct
filepath = "/home/user/documents"
if not os.path.isdir(filepath):
    with open(filepath, "r") as f:
        content = f.read()
else:
    print(f"Error: {filepath} is a directory, not a file")
```

### Fix 2: Use os.path.isfile() for validation

```python
import os
from pathlib import Path

# Wrong
path = get_user_path()
with open(path, "r") as f:
    data = f.read()

# Correct
path = get_user_path()
if os.path.isfile(path):
    with open(path, "r") as f:
        data = f.read()
else:
    raise ValueError(f"Expected a file, got: {path}")
```

### Fix 3: Properly construct file paths

```python
import os
from pathlib import Path

# Wrong
directory = "/home/user/documents"
with open(directory, "r") as f:

# Correct — append the filename
directory = "/home/user/documents"
filename = "report.txt"
filepath = os.path.join(directory, filename)
with open(filepath, "r") as f:

# Better — use pathlib
directory = Path("/home/user/documents")
filepath = directory / "report.txt"
with open(filepath, "r") as f:
```

### Fix 4: Filter directories when iterating paths

```python
import os
import glob

# Wrong — tries to open directories
for path in glob.glob("/home/user/*"):
    with open(path, "r") as f:
        print(f.read())

# Correct — skip directories
for path in glob.glob("/home/user/*"):
    if os.path.isfile(path):
        with open(path, "r") as f:
            print(f.read())
```

### Fix 5: Validate path before extraction from archives

```python
import zipfile

# Wrong
with zipfile.ZipFile("archive.zip", "r") as zf:
    for entry in zf.namelist():
        with zf.open(entry) as f:  # IsADirectoryError for directory entries

# Correct
with zipfile.ZipFile("archive.zip", "r") as zf:
    for entry in zf.namelist():
        if not entry.endswith("/"):
            with zf.open(entry) as f:
                print(f.read())
```

## Related Errors

- [FileNotFoundError](../filenotfounderror) — path doesn't exist.
- [NotADirectoryError](#) — expected directory but got file.
- [PermissionError](#) — no access to the path.
