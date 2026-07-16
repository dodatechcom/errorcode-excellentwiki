---
title: "[Solution] Python FileNotFoundError: [Errno 2] No such file or directory (Path Fix)"
description: "Fix Python FileNotFoundError [Errno 2] No such file or directory. Verify file paths, check working directory, and handle missing files gracefully."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["filenotfounderror", "errno-2", "no-such-file", "path", "directory"]
weight: 5
---

# FileNotFoundError: [Errno 2] No such file or directory

A `FileNotFoundError` with `[Errno 2] No such file or directory` is raised when Python tries to access a file or directory at a path that does not exist. This is the most common file I/O error and often results from incorrect paths, wrong working directory, or missing files.

## Description

This error is the Python 3 replacement for the old `IOError`. The `[Errno 2]` corresponds to the POSIX `ENOENT` error code. It occurs whenever an OS-level file operation fails because the target path doesn't resolve to an existing filesystem entry.

Common patterns:

- **Wrong working directory** — script is run from a different location than expected.
- **Missing file after build** — file hasn't been generated yet.
- **Hardcoded absolute path** — path doesn't exist on the current machine.
- **Typo in filename** — case sensitivity, extension mismatch.

## Common Causes

```python
# Cause 1: Running script from wrong directory
# File is at /home/user/project/data.csv
# But you're running from /home/user
open("data.csv")  # FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'

# Cause 2: Missing file extension
open("config")  # Actual file is config.json

# Cause 3: File hasn't been created yet
with open("output/results.csv", "w") as f:
    f.write("data")  # FileNotFoundError: directory "output" doesn't exist

# Cause 4: Symlink pointing to deleted target
os.symlink("/deleted/file.txt", "/tmp/link.txt")
open("/tmp/link.txt")  # FileNotFoundError
```

## How to Fix

### Fix 1: Use absolute paths or resolve relative to script

```python
from pathlib import Path

# Wrong
open("data.csv")

# Correct — resolve relative to the script's directory
script_dir = Path(__file__).parent
data_path = script_dir / "data.csv"
with open(data_path) as f:
    content = f.read()
```

### Fix 2: Create parent directories before writing

```python
from pathlib import Path

# Wrong
with open("output/results.csv", "w") as f:
    f.write("data")

# Correct
output_dir = Path("output")
output_dir.mkdir(parents=True, exist_ok=True)
with open(output_dir / "results.csv", "w") as f:
    f.write("data")
```

### Fix 3: Check file existence before opening

```python
from pathlib import Path

filepath = Path("data.csv")
if filepath.exists():
    with open(filepath) as f:
        content = f.read()
else:
    print(f"File not found: {filepath.absolute()}")
```

### Fix 4: Print the actual path in error messages

```python
import os

filepath = "data.csv"
abs_path = os.path.abspath(filepath)
if not os.path.exists(filepath):
    raise FileNotFoundError(
        f"[Errno 2] No such file or directory: '{filepath}'\n"
        f"  Looking in: {os.getcwd()}\n"
        f"  Absolute path: {abs_path}"
    )
```

## Examples

This error commonly occurs when:

- Running a Python script from the project root instead of the script's directory
- After `git clone`, forgetting to generate config files from templates
- In Docker containers where file paths are different than on the host
- After `os.rename()` moved a file that subsequent code expects in the old location

## Related Errors

- [PermissionError](permissionerror) — file exists but you don't have access
- [IsADirectoryError](#) — path is a directory when a file was expected
- [OSError](#) — parent error class for file I/O errors
