---
title: "[Solution] Linux EISDIR (errno 21) — Is a Directory Fix"
description: "Fix Linux EISDIR (errno 21) Is a directory error. Solutions for file and directory type confusion issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EISDIR (errno 21) — Is a Directory

EISDIR (errno 21) means an operation attempted on a file actually refers to a directory. This error occurs when you try to read from, write to, or open a directory as if it were a regular file. It is distinct from ENOTDIR (errno 20) because EISDIR indicates the target is a directory when a file was expected, rather than a file where a directory was expected.

## Common Causes

- Attempting to open a directory with `open()` for reading or writing
- Using a command intended for files on a directory (e.g., `cat /etc`)
- A symbolic link points to a directory instead of a file
- Incorrect file path in a script or program

## How to Fix EISDIR

### 1. Verify the Target is a File

Check if the path points to a directory:

```bash
file /path/to/target
ls -ld /path/to/target
```

### 2. List Directory Contents Instead

If you want to examine a directory, list its contents:

```bash
ls -la /path/to/directory/
```

### 3. Check Symbolic Links

Ensure symlinks point to files rather than directories:

```bash
readlink -f /path/to/symlink
```

### 4. Fix the Path in Your Code

Correct any path construction errors in programs:

```c
struct stat st;
if (stat(path, &st) == 0 && S_ISDIR(st.st_mode)) {
    fprintf(stderr, "Error: path is a directory\n");
    return -1;
}
```

## Verification

After correcting the path, confirm the operation targets a file:

```bash
file /corrected/path/to/file
cat /corrected/path/to/file
```

## Related Error Codes

- [ENOTDIR (errno 20)](/os/linux/errno-20/) — Not a directory
- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
- [ENOTEMPTY (errno 39)](/os/linux/errno-39/) — Directory not empty
