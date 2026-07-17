---
title: "[Solution] Python IOError — Input/Output Error Fix"
description: "Fix Python IOError when file operations fail. This is an alias for OSError in Python 3. Handle file I/O errors, check paths, and use proper error handling."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IOError — Input/Output Error Fix

`IOError` is an alias for `OSError` in Python 3. It was a separate exception in Python 2 for I/O-related errors, but was merged into `OSError` for simplification. If you encounter `IOError`, it behaves identically to `OSError`.

## Description

In Python 2, `IOError` handled file and stream operation failures (like file not found, permission denied, disk full), while `OSError` handled other system-level errors. Since Python 3.3 ([PEP 3151](https://peps.python.org/pep-3151/)), these were unified under `OSError`. Modern code should catch `OSError` or its specific subclasses instead.

Common scenarios:

- **File not found** — now `FileNotFoundError` (subclass of `OSError`).
- **Permission denied** — now `PermissionError` (subclass of `OSError`).
- **Disk full** — `OSError` with `errno.ENOSPC`.
- **Broken pipe** — now `BrokenPipeError` (subclass of `OSError`).
- **Device not found** — `OSError` with `errno.ENXIO`.

## Common Causes

```python
# Cause 1: Reading from non-existent file
with open("nonexistent.txt", "r") as f:  # FileNotFoundError (IOError in Python 2)
    content = f.read()

# Cause 2: Writing to read-only location
with open("/usr/bin/output.txt", "w") as f:  # PermissionError (IOError in Python 2)
    f.write("data")

# Cause 3: Disk full
with open("/full/disk/file.txt", "w") as f:  # OSError: [Errno 28] No space left on device
    f.write("data" * 1000000)

# Cause 4: Reading from closed file
f = open("data.txt")
f.close()
f.read()  # ValueError: I/O operation on closed file

# Cause 5: Invalid file mode
f = open("data.txt", "x")  # FileExistsError if file exists
```

## Solutions

### Fix 1: Use OSError or specific subclasses instead of IOError

```python
# Wrong — IOError is deprecated as separate exception
try:
    with open("data.txt") as f:
        content = f.read()
except IOError:  # Works but not recommended
    print("I/O error")

# Correct — use OSError or specific subclasses
try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except OSError as e:
    print(f"OS error: {e}")
```

### Fix 2: Check file existence before opening

```python
import os
from pathlib import Path

# Wrong — assumes file exists
with open("data.txt") as f:
    content = f.read()

# Correct — verify before opening
filepath = Path("data.txt")
if filepath.exists() and filepath.is_file():
    with open(filepath) as f:
        content = f.read()
else:
    print(f"File not found: {filepath}")
```

### Fix 3: Handle file operations with context managers

```python
# Wrong — manual close may fail
f = open("data.txt", "r")
content = f.read()
f.close()  # May raise IOError if already closed

# Correct — context manager handles cleanup
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed, even on errors
```

### Fix 4: Use proper error handling for file operations

```python
import os

# Wrong — no error handling
with open("data.txt", "r") as f:
    content = f.read()

# Correct — comprehensive error handling
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found — creating default")
    content = "default data"
except PermissionError:
    print("Permission denied — check file permissions")
except OSError as e:
    print(f"File I/O error: {e}")
```

### Fix 5: Use pathlib for modern file operations

```python
from pathlib import Path

# Wrong — raw string paths
try:
    with open("/some/path/data.txt") as f:
        content = f.read()
except IOError:
    print("Error")

# Correct — pathlib provides cleaner API
path = Path("/some/path/data.txt")
try:
    content = path.read_text()
except OSError as e:
    print(f"Error reading {path}: {e}")
```

## Related Errors

- [OSError](../oserror) — the parent exception (same thing in Python 3).
- [FileNotFoundError](../filenotfounderror) — file does not exist.
- [PermissionError](../permissionerror) — insufficient permissions.
- [EnvironmentError](../environmenterror) — another alias for OSError.
