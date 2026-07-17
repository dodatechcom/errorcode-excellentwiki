---
title: "[Solution] C No such file or directory: ENOENT"
description: "Fix C no such file or directory (ENOENT). Verify file paths before opening."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# No such file or directory: ENOENT

ENOENT occurs when you try to open, access, or stat a file that does not exist. The path may be wrong, the file may have been deleted, or the directory doesn't exist.

## Common Causes

```c
// Cause 1: File doesn't exist
int fd = open("nonexistent.txt", O_RDONLY); // ENOENT

// Cause 2: Wrong path
int fd = open("data/file.txt", O_RDONLY); // ENOENT if dir doesn't exist

// Cause 3: Typo in filename
int fd = open("conifg.json", O_RDONLY); // ENOENT — typo
```

## How to Fix

### Fix 1: Verify path exists

```c
#include <sys/stat.h>

struct stat st;
if (stat("file.txt", &st) == -1) {
    if (errno == ENOENT) {
        fprintf(stderr, "File not found: file.txt\n");
    }
}
```

### Fix 2: Check directory first

```c
DIR *dir = opendir("data");
if (dir) {
    closedir(dir);
    int fd = open("data/file.txt", O_RDONLY);
}
```

### Fix 3: Use absolute path

```c
int fd = open("/home/user/data/file.txt", O_RDONLY);
```

## Related Errors

- [Permission denied]({{< relref "/languages/c/permission-denied-file" >}}) — EACCES.
- [Not a directory]({{< relref "/languages/c/not-a-directory" >}}) — ENOTDIR.
- [Is a directory]({{< relref "/languages/c/is-a-directory" >}}) — EISDIR.
