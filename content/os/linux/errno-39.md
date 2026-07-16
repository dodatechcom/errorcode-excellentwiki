---
title: "[Solution] Linux ENOTEMPTY (errno 39) — Directory Not Empty Fix"
description: "Fix Linux ENOTEMPTY (errno 39) Directory not empty error. Solutions for rmdir and directory removal issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enNOTEMPTY", "directory", "errno-39", "rmdir"]
weight: 5
---

# Linux ENOTEMPTY (errno 39) — Directory Not Empty

ENOTEMPTY (errno 39) means you tried to remove a directory that is not empty. This error occurs when calling `rmdir()` on a directory that still contains files or subdirectories. It is distinct from EISDIR (errno 21) because ENOTEMPTY specifically refers to a non-empty directory, not just any directory.

## Common Causes

- Attempting to `rmdir` a directory that contains files
- Hidden files (starting with `.`) are still present
- The directory contains subdirectories
- A file is locked or in use within the directory

## How to Fix ENOTEMPTY

### 1. List Directory Contents

Check what files remain in the directory:

```bash
ls -la /path/to/directory/
```

### 2. Remove Hidden Files

Hidden files are not shown by default:

```bash
ls -la /path/to/directory/ | grep "^\."
rm -rf /path/to/directory/.[!.]* /path/to/directory/..?*
```

### 3. Remove Everything Recursively

Use `rm -rf` to remove the directory and all contents:

```bash
rm -rf /path/to/directory/
```

### 4. Check for Locked Files

Find files that may be in use:

```bash
lsof +D /path/to/directory/
fuser -v /path/to/directory/
```

Kill any processes holding files open and retry:

```bash
fuser -k /path/to/directory/
rm -rf /path/to/directory/
```

## Verification

After removal, confirm the directory is gone:

```bash
ls -la /path/to/
```

## Related Error Codes

- [EISDIR (errno 21)](/os/linux/errno-21/) — Is a directory
- [ENOTDIR (errno 20)](/os/linux/errno-20/) — Not a directory
- [EBUSY (errno 16)](/os/linux/errno-16/) — Device or resource busy
