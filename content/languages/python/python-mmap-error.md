---
title: "[Solution] Python mmap Error — Memory-Mapped File Errors"
description: "Fix Python mmap errors including mmap.error, access modes, file size, seek errors, and memory mapping failures. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 233
---

# Python mmap Error — Memory-Mapped File Errors

The `mmap` module provides memory-mapped file support. Errors involve invalid access modes, file size mismatches, seek errors, and platform-specific failures.

## Common Causes

```python
import mmap

# Error: Mapping a zero-length file
f = open("/tmp/empty_file", "r+b")
m = mmap.mmap(f.fileno(), 0)
# ValueError: cannot mmap an empty file
```

```python
import mmap

# Error: Invalid access mode
m = mmap.mmap(-1, 1024, access=99)
# ValueError: invalid access mode
```

```python
import mmap

# Error: Seeking beyond the mapped region
f = open("/tmp/small_file", "r+b")
m = mmap.mmap(f.fileno(), 0)
m.seek(999999)
# OverflowError: seek out of range
```

```python
import mmap

# Error: Writing to a read-only mapping
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_READ)
m.write(b"data")
# TypeError: write not allowed on read-only mmap
```

```python
import mmap

# Error: Mapping with invalid file descriptor
m = mmap.mmap(-1, 1024)  # This creates anonymous mapping
# But using a bad fd:
f = open("/tmp/file", "rb")
f.close()
m = mmap.mmap(f.fileno(), 1024)
# ValueError: mmap length is greater than file size
```

## How to Fix

### Fix 1: Ensure File Has Content Before Mapping

```python
import mmap
import os

def safe_mmap(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    size = os.path.getsize(filepath)
    if size == 0:
        raise ValueError(f"Cannot mmap empty file: {filepath}")

    f = open(filepath, "r+b")
    try:
        m = mmap.mmap(f.fileno(), 0)
        return f, m
    except Exception:
        f.close()
        raise
```

### Fix 2: Use Correct Access Modes

```python
import mmap

# Available access modes:
# ACCESS_READ   - read-only
# ACCESS_WRITE  - writeable (private copy-on-write)
# ACCESS_COPY   - writeable (changes not written to file)

# Read-only
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_READ)

# Writeable
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_WRITE)

# Copy-on-write
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_COPY)
```

### Fix 3: Validate Size Before Mapping

```python
import mmap
import os

def safe_mmap_with_size(filepath, size=None):
    f = open(filepath, "r+b")
    file_size = os.path.getsize(filepath)

    if size is None:
        size = file_size
    elif size > file_size:
        f.close()
        raise ValueError(f"Requested size {size} > file size {file_size}")

    try:
        m = mmap.mmap(f.fileno(), size)
        return f, m
    except Exception:
        f.close()
        raise
```

### Fix 4: Handle Seek Errors

```python
import mmap

f = open("/tmp/data.bin", "r+b")
m = mmap.mmap(f.fileno(), 0)

try:
    position = m.tell()
    m.seek(0, mmap.SEEK_SET)  # Go to beginning
    m.seek(0, mmap.SEEK_END)  # Go to end

    # Safe seek within bounds
    target = 100
    if target < m.size():
        m.seek(target)
    else:
        m.seek(0, mmap.SEEK_END)
finally:
    m.close()
    f.close()
```

## Examples

```python
import mmap
import os

# Read large binary file efficiently
def read_mmap(filepath):
    with open(filepath, "rb") as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            # Find a pattern
            offset = m.find(b"HEADER")
            if offset != -1:
                m.seek(offset)
                return m.read(1024)
            return None

# Shared memory between processes
def create_shared_memory(name, size):
    import mmap as mmap_module
    # Create anonymous shared memory
    m = mmap.mmap(-1, size, tagname=name)
    m.write(b"shared data")
    m.seek(0)
    return m.read(size)
```

## Related Errors

- [Python ValueError](/languages/python/python-valueerror/)
- [Python OverflowError](/languages/python/python-overflowerror/)
- [Python OSError](/languages/python/python-oserror/)
