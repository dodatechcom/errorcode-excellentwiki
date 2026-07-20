---
title: "[Solution] Python tempfile Error — Temporary File and Directory Errors"
description: "Fix Python tempfile errors including NamedTemporaryFile, SpooledTemporaryFile, TemporaryDirectory cleanup, and permission denied. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 230
---

# Python tempfile Error — Temporary File and Directory Errors

The `tempfile` module creates temporary files and directories. Errors involve cleanup failures, permission issues, file locking on Windows, and improper resource management.

## Common Causes

```python
import tempfile

# Error: NamedTemporaryFile cannot be opened by name on Windows
with tempfile.NamedTemporaryFile() as f:
    f.write(b"data")
    open(f.name, "rb")  # PermissionError on Windows
```

```python
import tempfile

# Error: TemporaryDirectory cleanup fails if files are still open
td = tempfile.TemporaryDirectory()
f = open(f"{td.name}/file.txt", "w")
f.write("data")
td.cleanup()
# PermissionError or OSError: [WinError 32] on Windows
```

```python
import tempfile

# Error: SpooledTemporaryFile exceeds max_size unexpectedly
stf = tempfile.SpooledTemporaryFile(max_size=1024)
stf.write(b"x" * 2048)  # Rolls to disk, may cause issues
```

```python
import tempfile

# Error: Forgetting to clean up temporary files
def process():
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(b"data")
    # File remains if not explicitly deleted
    # On some systems, many open temp files cause ResourceWarning
```

```python
import tempfile

# Error: Invalid mode for temporary file
f = tempfile.TemporaryFile(mode="x")  # x mode creates, but may conflict
```

## How to Fix

### Fix 1: Use NamedTemporaryFile Properly

```python
import tempfile

# Use delete=True (default) for automatic cleanup
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as f:
    f.write("Hello, World!")
    f.flush()
    # File is deleted when exiting the context

# If you need to access the file by name on all platforms
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    name = f.name
    f.write("data")
try:
    # Process the file
    with open(name, "r") as f:
        content = f.read()
finally:
    import os
    os.unlink(name)
```

### Fix 2: Use Context Manager for Automatic Cleanup

```python
import tempfile

# TemporaryDirectory with context manager
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Working in: {tmpdir}")
    # Create files
    for i in range(5):
        with open(f"{tmpdir}/file_{i}.txt", "w") as f:
            f.write(f"Content {i}")
# Directory and all files are automatically deleted
```

### Fix 3: Handle Cleanup Errors Gracefully

```python
import tempfile
import shutil

def safe_tempdir():
    tmpdir = tempfile.mkdtemp()
    try:
        yield tmpdir
    finally:
        try:
            shutil.rmtree(tmpdir, ignore_errors=True)
        except Exception:
            pass  # Log the error if needed

# Or use try/finally
tmpdir = tempfile.mkdtemp()
try:
    # do work
    pass
finally:
    shutil.rmtree(tmpdir, ignore_errors=True)
```

### Fix 4: Manage SpooledTemporaryFile Buffer Size

```python
import tempfile

# Use appropriate max_size to control when data goes to disk
# Small threshold = earlier disk usage
with tempfile.SpooledTemporaryFile(max_size=1024 * 1024) as stf:
    stf.write(b"data")
    stf.seek(0)
    data = stf.read()

# Check if it's still in memory or rolled to disk
stf = tempfile.SpooledTemporaryFile(max_size=100)
stf.write(b"x" * 200)
print(stf._rolled)  # True — rolled to disk
```

## Examples

```python
import tempfile
import os

# Process large file safely
def process_large_file(data):
    with tempfile.NamedTemporaryFile(mode="wb", suffix=".dat", delete=False) as f:
        f.write(data)
        tmpname = f.name
    try:
        # Simulate processing
        with open(tmpname, "rb") as f:
            result = f.read()
        return result
    finally:
        os.unlink(tmpname)

# Multiple temporary files
files = []
for i in range(3):
    f = tempfile.NamedTemporaryFile(mode="w", suffix=f"_{i}.txt")
    f.write(f"File {i}")
    f.flush()
    files.append(f)

# Process all files
for f in files:
    print(f"File: {f.name}")

# Clean up all
for f in files:
    f.close()
```

## Related Errors

- [Python PermissionError](/languages/python/python-permissionerror/)
- [Python OSError](/languages/python/python-oserror/)
- [Python ResourceWarning](/languages/python/python-resourcewarning/)
