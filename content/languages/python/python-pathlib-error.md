---
title: "[Solution] Python pathlib Error — Path Manipulation and File System Errors"
description: "Fix Python pathlib errors including FileNotFoundError, NotADirectoryError, symlink errors, permission errors, and PurePath issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 229
---

# Python pathlib Error — Path Manipulation and File System Errors

The `pathlib` module provides object-oriented filesystem paths. Errors involve missing files, directory confusion, symlink resolution, permission issues, and PurePath manipulation.

## Common Causes

```python
from pathlib import Path

# Error: Reading a file that doesn't exist
p = Path("nonexistent.txt")
p.read_text()
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
```

```python
from pathlib import Path

# Error: Treating a file as a directory
p = Path("file.txt")
list(p.iterdir())
# NotADirectoryError: [Errno 20] Not a directory: 'file.txt'
```

```python
from pathlib import Path

# Error: Resolving a broken symlink
p = Path("broken_link")
p.resolve()
# FileNotFoundError: [Errno 2] No such file or directory
```

```python
from pathlib import Path

# Error: Permission denied on restricted path
p = Path("/root/secret.txt")
p.read_text()
# PermissionError: [Errno 13] Permission denied
```

```python
from pathlib import Path

# Error: Creating parent directories without exist_ok
p = Path("/tmp/new/dir/file.txt")
p.parent.mkdir(exist_ok=False)
# FileExistsError: [Errno 17] File exists
```

## How to Fix

### Fix 1: Check File Existence Before Operations

```python
from pathlib import Path

p = Path("data.txt")

# Method 1: Check existence
if p.exists():
    content = p.read_text()
else:
    print(f"File not found: {p}")

# Method 2: Use try/except
try:
    content = p.read_text()
except FileNotFoundError:
    print(f"File not found: {p}")
```

### Fix 2: Check Is a Directory Before Listing

```python
from pathlib import Path

p = Path("some_path")

if p.is_dir():
    for item in p.iterdir():
        print(item)
elif p.is_file():
    print(f"{p} is a file, not a directory")
else:
    print(f"{p} does not exist")
```

### Fix 3: Handle Symlinks Safely

```python
from pathlib import Path

p = Path("my_link")

# Check if it's a symlink
if p.is_symlink():
    target = p.resolve()
    if target.exists():
        print(f"Link points to: {target}")
    else:
        print(f"Broken symlink: {p} -> {target}")
elif p.exists():
    print(f"Regular path: {p}")
else:
    print(f"Path does not exist: {p}")
```

### Fix 4: Create Directories Recursively

```python
from pathlib import Path

p = Path("/tmp/new/deep/dir/file.txt")

# Create all parent directories safely
p.parent.mkdir(parents=True, exist_ok=True)

# Write the file
p.write_text("Hello, World!")
```

## Examples

```python
from pathlib import Path

# Safe file operations with pathlib
def process_files(directory):
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    results = []
    for p in dir_path.glob("**/*.txt"):
        try:
            content = p.read_text()
            results.append({"path": p, "lines": len(content.splitlines())})
        except (PermissionError, OSError) as e:
            print(f"Skipping {p}: {e}")
    return results

# Path manipulation
config = Path.home() / ".config" / "myapp" / "settings.json"
config.parent.mkdir(parents=True, exist_ok=True)
config.write_text('{"theme": "dark"}')
```

## Related Errors

- [Python FileNotFoundError](/languages/python/python-filenotfounderror/)
- [Python PermissionError](/languages/python/python-permissionerror/)
- [Python NotADirectoryError](/languages/python/python-notadirectoryerror/)
