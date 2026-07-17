---
title: "[Solution] Python PermissionError — Permission Denied Fix"
description: "Fix Python PermissionError when accessing files without proper permissions. Check file permissions, use sudo, chmod, or chown."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 70
---

# PermissionError — Permission Denied Fix

A `PermissionError` is raised when you try to open, read, write, or delete a file without the necessary operating system permissions. It's a subclass of `OSError`.

## Description

`PermissionError` is an OS-level error — the file exists, but your process doesn't have the right permissions. This differs from `FileNotFoundError` (file doesn't exist) and `IsADirectoryError` (path is a directory, not a file).

Common scenarios:

- **Reading a protected file** — `/etc/shadow` or system config files.
- **Writing to a read-only location** — `/usr/bin` without root.
- **Deleting a file you don't own** — without proper permissions.
- **Running scripts without execute permission** — script lacks `+x`.
- **File locked by another process** — Windows especially, but Linux too.

## Common Causes

```python
# Cause 1: Reading a protected system file
with open("/etc/shadow", "r") as f:
    content = f.read()  # PermissionError

# Cause 2: Writing to a directory you don't own
with open("/usr/bin/myfile.txt", "w") as f:
    f.write("data")  # PermissionError

# Cause 3: Deleting a file without write permission on parent directory
import os
os.remove("/root/important_file.txt")  # PermissionError

# Cause 4: Executing a script without execute permission
import subprocess
subprocess.run(["./myscript.sh"])  # PermissionError if not executable

# Cause 5: Opening a file opened exclusively by another process
with open("data.lock", "r") as f1:
    with open("data.lock", "r") as f2:  # May fail on Windows
        pass
```

## Solutions

### Fix 1: Check file permissions before accessing

```python
import os

# Wrong
with open("/etc/shadow", "r") as f:
    content = f.read()

# Correct
filepath = "/etc/shadow"
if os.access(filepath, os.R_OK):
    with open(filepath, "r") as f:
        content = f.read()
else:
    print(f"No read permission for {filepath}")
```

### Fix 2: Use try/except to handle permission errors gracefully

```python
# Wrong — crashes on permission error
with open("/protected/file.txt", "r") as f:
    data = f.read()

# Correct
try:
    with open("/protected/file.txt", "r") as f:
        data = f.read()
except PermissionError:
    print("Permission denied — check file permissions")
    data = None
```

### Fix 3: Change file permissions with os.chmod()

```python
import os
import stat

# Wrong — file is read-only
with open("config.txt", "w") as f:
    f.write("new content")

# Correct — make file writable first
filepath = "config.txt"
os.chmod(filepath, stat.S_IRUSR | stat.S_IWUSR)  # Owner read/write
with open(filepath, "w") as f:
    f.write("new content")
```

### Fix 4: Use sudo for system-level operations

```python
import subprocess

# Wrong — can't write to system directory
with open("/etc/myapp/config.conf", "w") as f:
    f.write("settings")

# Correct — use subprocess with sudo
subprocess.run([
    "sudo", "tee", "/etc/myapp/config.conf"
], input=b"settings", check=True)
```

### Fix 5: Create files in user-writable directories

```python
import os
from pathlib import Path

# Wrong — writing to system directory
with open("/var/log/myapp.log", "w") as f:
    f.write("log entry")

# Correct — use user's home directory or temp
log_dir = Path.home() / ".myapp"
log_dir.mkdir(exist_ok=True)
log_path = log_dir / "myapp.log"
with open(log_path, "w") as f:
    f.write("log entry")
```

### Fix 6: Check ownership and use os.chown() if needed

```python
import os

# Wrong — file owned by root, can't modify
with open("/var/data/output.csv", "w") as f:
    f.write("data")

# Correct — check ownership first
filepath = "/var/data/output.csv"
stat_info = os.stat(filepath)
print(f"Owner UID: {stat_info.st_uid}")
# If you need to change ownership (requires root):
# os.chown(filepath, uid=1000, gid=1000)
```

## Related Errors

- [FileNotFoundError](../filenotfounderror) — file doesn't exist.
- [IsADirectoryError](#) — path is a directory, not a file.
- [OSError](#) — generic OS-level error.
