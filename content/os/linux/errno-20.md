---
title: "[Solution] Linux ENOTDIR (errno 20) — Not a Directory Fix"
description: "Fix Linux ENOTDIR (errno 20) Not a directory error. Solutions for path and file type issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enOTDIR", "directory", "errno-20", "path"]
weight: 5
---

# Linux ENOTDIR (errno 20) — Not a Directory

ENOTDIR (errno 20) means a component of the path used in an operation is not a directory when it was expected to be. This error occurs when you try to use a file as if it were a directory, such as listing its contents or creating a path through it. It is distinct from ENOENT (errno 2) because the file exists but is not a directory.

## Common Causes

- Using a file path where a directory path is expected (e.g., `cd /etc/hostname/subdir`)
- A symbolic link points to a file instead of a directory
- Incorrect path construction in scripts or programs
- A parent directory in the path has been replaced by a file

## How to Fix ENOTDIR

### 1. Verify Path Components

Check each component of the path to ensure they are directories:

```bash
file /path/to/parent
ls -ld /path/to/parent
```

### 2. Check Symbolic Links

Ensure symbolic links in the path point to directories:

```bash
ls -la /path/to/link
readlink -f /path/to/link
```

### 3. Correct the Path in Your Script

Fix any path construction errors:

```bash
# Wrong:
cd /etc/hostname/subdir

# Correct:
cd /etc/subdir
```

### 4. Use stat to Inspect Path

Get detailed information about each path component:

```bash
stat /path/to/component
```

## Verification

After correcting the path, confirm the operation succeeds:

```bash
ls /corrected/path/
```

## Related Error Codes

- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
- [EISDIR (errno 21)](/os/linux/errno-21/) — Is a directory
- [ENOTEMPTY (errno 39)](/os/linux/errno-39/) — Directory not empty
