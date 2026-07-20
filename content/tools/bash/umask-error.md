---
title: "[Solution] Umask Command Error"
description: "Fix umask file creation mask errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Umask Command Error

The `umask` command has an invalid value or fails to set the mask.

### Common Causes
- Octal value is invalid (e.g., `umask 888`).
- Trying to set umask in restricted shell.
- Negative or non-octal values.

### How to Fix
```bash
# Set umask (octal, 0-777)
umask 022     # default: rwxr-xr-x
umask 077     # private: rwx------
umask 002     # group-writable: rwxrwxr-x

# Check current umask
umask
umask -S      # symbolic output

# Calculate permissions
# Files: 666 - umask = final permissions
# Dirs: 777 - umask = final permissions
umask 022
# file: 666 - 022 = 644 (rw-r--r--)
# dir:  777 - 022 = 755 (rwxr-xr-x)
```

### Example
```bash
# Broken
umask 088    # invalid octal digit

# Fixed
umask 022
```
