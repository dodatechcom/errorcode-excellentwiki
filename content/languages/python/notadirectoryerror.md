---
title: "[Solution] Python NotADirectoryError — Expected Directory Got File Fix"
description: "Fix Python NotADirectoryError when expecting a directory but finding a file. Check path, verify mount points, and use os.path.isfile()."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 58
---

# NotADirectoryError — Expected Directory Got File Fix

A `NotADirectoryError` is raised when you try to use a file path where a directory is expected. It's the opposite of `IsADirectoryError` and is a subclass of `OSError`.

## Description

This error occurs when an operation requires a directory (like listing contents, joining paths with `os.listdir()`, or changing directory with `os.chdir()`) but the path points to a file. It often appears in file traversal code or when paths are constructed incorrectly.

Common scenarios:

- **Using os.listdir() on a file** — path is a file, not a directory.
- **os.path.join() with wrong base** — base is a file instead of a directory.
- **Walking directory tree** — `os.walk()` receives a file path.
- **Chdir to a file** — `os.chdir()` with a file path.
- **Mount point issues** — expected mount directory doesn't exist.

## Common Causes

```python
import os

# Cause 1: os.listdir() on a file
filepath = "/home/user/report.txt"
files = os.listdir(filepath)  # NotADirectoryError

# Cause 2: os.path.join with file as base
base = "/home/user/report.txt"
full_path = os.path.join(base, "subdir")  # NotADirectoryError

# Cause 3: os.walk() on a file
for root, dirs, files in os.walk("/home/user/report.txt"):  # NotADirectoryError

# Cause 4: os.chdir() to a file
os.chdir("/home/user/report.txt")  # NotADirectoryError

# Cause 5: Path manipulation error
directory = "/home/user/documents"
filename = "report.txt"
filepath = os.path.join(directory, filename)
# Accidentally passing filepath where directory is expected
files = os.listdir(filepath)  # NotADirectoryError
```

## Solutions

### Fix 1: Verify path is a directory before listing

```python
import os

# Wrong
path = get_path()
files = os.listdir(path)

# Correct
path = get_path()
if os.path.isdir(path):
    files = os.listdir(path)
else:
    print(f"Error: {path} is not a directory")
    files = []
```

### Fix 2: Use os.path.isfile() to distinguish files from directories

```python
import os

# Wrong — assumes path is a directory
def process_path(path):
    for item in os.listdir(path):
        print(item)

# Correct — validate first
def process_path(path):
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        return
    if os.path.isfile(path):
        print(f"Path is a file: {path}")
        return
    for item in os.listdir(path):
        print(item)
```

### Fix 3: Use pathlib for safer path operations

```python
from pathlib import Path

# Wrong
path = Path("/home/user/report.txt")
for item in path.iterdir():  # NotADirectoryError

# Correct
path = Path("/home/user/report.txt")
if path.is_dir():
    for item in path.iterdir():
        print(item)
else:
    print(f"Not a directory: {path}")
```

### Fix 4: Fix path construction

```python
import os

# Wrong — filepath used as directory
base = "/home/user/report.txt"
subpath = os.path.join(base, "subdir")

# Correct — ensure base is a directory
base = "/home/user"
subpath = os.path.join(base, "subdir")
os.makedirs(subpath, exist_ok=True)
```

### Fix 5: Verify mount points before traversal

```python
import os

# Wrong — assumes mount point is a directory
mount = "/mnt/data"
for root, dirs, files in os.walk(mount):

# Correct — verify mount point exists and is a directory
mount = "/mnt/data"
if os.path.isdir(mount):
    for root, dirs, files in os.walk(mount):
        print(root)
else:
    print(f"Mount point {mount} is not accessible or not a directory")
```

### Fix 6: Safe directory walker

```python
import os
from pathlib import Path

def safe_walk(path):
    """Walk a directory tree safely, skipping non-directory paths."""
    path = Path(path)
    if not path.exists():
        print(f"Path does not exist: {path}")
        return
    if not path.is_dir():
        print(f"Path is not a directory: {path}")
        return
    for root, dirs, files in os.walk(path):
        yield root, dirs, files

for root, dirs, files in safe_walk("/home/user"):
    print(f"Directory: {root}")
```

## Related Errors

- [FileNotFoundError](../filenotfounderror) — path doesn't exist.
- [IsADirectoryError](#) — expected file but got directory.
- [PermissionError](#) — no access to the path.
