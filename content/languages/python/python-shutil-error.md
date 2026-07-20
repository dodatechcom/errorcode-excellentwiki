---
title: "[Solution] Python shutil Error — Shell Utility Operations Errors"
description: "Fix Python shutil errors including copytree, rmtree, move, disk_usage, make_archive, and permission denied. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 232
---

# Python shutil Error — Shell Utility Operations Errors

The `shutil` module provides high-level file operations. Errors involve missing directories, permission issues, disk space, and archive creation failures.

## Common Causes

```python
import shutil

# Error: copytree destination already exists
shutil.copytree("/src", "/dest")
# shutil.Error: '/dest' already exists
```

```python
import shutil

# Error: rmtree on non-existent directory
shutil.rmtree("/nonexistent")
# FileNotFoundError: [Errno 2] No such file or directory
```

```python
import shutil

# Error: move to non-existent destination directory
shutil.move("/tmp/file.txt", "/nonexistent/dir/")
# shutil.Error: ...
```

```python
import shutil

# Error: disk_usage on non-existent path
shutil.disk_usage("/nonexistent")
# FileNotFoundError
```

```python
import shutil

# Error: make_archive with invalid format
shutil.make_archive("/tmp/archive", "invalid_format", "/tmp")
# ValueError: bad format 'invalid_format'
```

## How to Fix

### Fix 1: Handle Existing Destination in copytree

```python
import shutil
import os

# Python 3.8+: use dirs_exist_ok
shutil.copytree("/src", "/dest", dirs_exist_ok=True)

# Older Python: remove or rename destination first
dest = "/dest"
if os.path.exists(dest):
    shutil.rmtree(dest)
shutil.copytree("/src", dest)
```

### Fix 2: Check Directory Exists Before rmtree

```python
import shutil
import os

def safe_rmtree(path):
    if not os.path.exists(path):
        print(f"Directory does not exist: {path}")
        return
    if not os.path.isdir(path):
        print(f"Not a directory: {path}")
        return
    shutil.rmtree(path)

safe_rmtree("/tmp/mydir")
```

### Fix 3: Ensure Parent Directory Exists for move

```python
import shutil
import os

def safe_move(src, dest):
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source does not exist: {src}")
    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)
    shutil.move(src, dest)
```

### Fix 4: Check Disk Space Before Operations

```python
import shutil

def safe_copy_with_space(src, dest):
    usage = shutil.disk_usage("/")
    src_size = os.path.getsize(src) if os.path.isfile(src) else sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, dn, fn in os.walk(src)
        for f in fn
    )
    if src_size > usage.free:
        raise OSError(f"Not enough disk space: need {src_size}, have {usage.free}")
    shutil.copy2(src, dest)
```

## Examples

```python
import shutil
import os

# Safe backup of directory
def backup(src, backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    dest_name = os.path.basename(src)
    dest = os.path.join(backup_dir, dest_name)

    if os.path.exists(dest):
        backup_num = 1
        while os.path.exists(f"{dest}.{backup_num}"):
            backup_num += 1
        dest = f"{dest}.{backup_num}"

    shutil.copytree(src, dest)
    return dest

# Archive and extract
shutil.make_archive("/tmp/project_backup", "zip", "/home/user/project")

# Get disk usage info
total, used, free = shutil.disk_usage("/")
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")
```

## Related Errors

- [Python FileNotFoundError](/languages/python/python-filenotfounderror/)
- [Python PermissionError](/languages/python/python-permissionerror/)
- [Python OSError](/languages/python/python-oserror/)
