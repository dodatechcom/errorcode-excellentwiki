---
title: "[Solution] Python tarfile Error — Tar Archive Module Errors"
description: "Fix Python tarfile errors including ReadError, CompressionError, InvalidHeaderError, tar format issues, and extraction errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 234
---

# Python tarfile Error — Tar Archive Module Errors

The `tarfile` module reads and writes tar archives. Errors involve invalid files, compression issues, header corruption, and extraction failures.

## Common Causes

```python
import tarfile

# Error: Opening a non-tar file
tarfile.open("/tmp/not_a_tar.txt")
# tarfile.ReadError: file could not be opened successfully
```

```python
import tarfile

# Error: Corrupt tar archive
tarfile.open("/tmp/corrupt.tar")
# tarfile.ReadError: invalid header
```

```python
import tarfile

# Error: Unsupported compression
tarfile.open("/tmp/archive.7z")
# tarfile.ReadError: bad compression
```

```python
import tarfile

# Error: Extracting absolute path (security risk)
t = tarfile.open("/tmp/archive.tar")
t.extractall("/")
# May extract to /etc/passwd if archive contains absolute paths
```

```python
import tarfile

# Error: Memory issue with very large tar
tarfile.open("/tmp/huge.tar")
# Could raise MemoryError for extremely large archives
```

## How to Fix

### Fix 1: Verify File Is a Valid Tar Archive

```python
import tarfile

def open_tar_safe(filepath):
    if not tarfile.is_tarfile(filepath):
        raise ValueError(f"Not a tar file: {filepath}")
    return tarfile.open(filepath, "r:*")  # auto-detect compression

try:
    tar = open_tar_safe("/tmp/archive.tar")
except (tarfile.TarError, ValueError) as e:
    print(f"Error: {e}")
```

### Fix 2: Handle Decompression Errors

```python
import tarfile

def extract_tar_safe(filepath, dest):
    try:
        tar = tarfile.open(filepath, "r:*")
        tar.extractall(dest)
        tar.close()
    except tarfile.CompressionError as e:
        print(f"Unsupported compression: {e}")
    except tarfile.ReadError as e:
        print(f"Corrupt archive: {e}")
    except tarfile.TarError as e:
        print(f"Tar error: {e}")
```

### Fix 3: Prevent Path Traversal Attacks

```python
import tarfile
import os

def safe_extract(tar_path, dest):
    with tarfile.open(tar_path, "r:*") as tar:
        for member in tar.getmembers():
            member_path = os.path.join(dest, member.name)
            abs_dest = os.path.abspath(dest)
            abs_member = os.path.abspath(member_path)
            if not abs_member.startswith(abs_dest):
                raise tarfile.TarError(f"Path traversal detected: {member.name}")
        tar.extractall(dest)
```

### Fix 4: Add Members Incrementally for Large Archives

```python
import tarfile

def create_tar_slow(filepath, files):
    with tarfile.open(filepath, "w") as tar:
        for f in files:
            try:
                tar.add(f)
            except FileNotFoundError:
                print(f"Skipping missing file: {f}")
            except OSError as e:
                print(f"Error adding {f}: {e}")
```

## Examples

```python
import tarfile
import os

# Create a tar.gz archive
with tarfile.open("/tmp/backup.tar.gz", "w:gz") as tar:
    tar.add("/home/user/documents")
    tar.add("/home/user/config")

# List archive contents
with tarfile.open("/tmp/backup.tar.gz", "r:*") as tar:
    for member in tar.getmembers():
        print(f"{member.name: {member.size:>10}} bytes")

# Extract with filtering
with tarfile.open("/tmp/backup.tar.gz", "r:*") as tar:
    tar.extractall("/tmp/restore", filter="data")
```

## Related Errors

- [Python OSError](/languages/python/python-oserror/)
- [Python ValueError](/languages/python/python-valueerror/)
- [Python EOFError](/languages/python/python-eoferror/)
