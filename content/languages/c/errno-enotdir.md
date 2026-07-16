---
title: "[Solution] C errno ENOTDIR — Not a directory Fix"
description: "Fix C ENOTDIR (Not a directory) by verifying path components are directories and checking file types before operations."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enotdir", "not-a-directory", "path-resolution", "file-type"]
weight: 5
---

# [Solution] C errno ENOTDIR — Not a directory Fix

When a path component that is expected to be a directory is actually not a directory, the system call fails and sets `errno` to `ENOTDIR`. This error typically occurs during path resolution when a non-directory file is encountered where a directory is required.

## Common Causes

- A component in the path is a regular file, not a directory (e.g., `open("file.txt/subdir", ...)`).
- Using `chdir()` on a path where an intermediate component is not a directory.
- Calling `opendir()` on a regular file instead of a directory.
- `execve()` or `readdir()` receives a path with a non-directory component.

## How to Fix

Verify that each path component is a directory before performing directory operations. Use `stat()` to check the file type.

```c
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    struct stat st;
    if (stat("some/path", &st) == -1) {
        fprintf(stderr, "stat failed: %s\n", strerror(errno));
        return 1;
    }
    if (!S_ISDIR(st.st_mode)) {
        fprintf(stderr, "some/path is not a directory\n");
        return 1;
    }
    // Safe to use as a directory
    return 0;
}
```

## Examples

Opening a path where an intermediate component is a file:

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Suppose "myfile" is a regular file, not a directory
    int fd = open("myfile/subfile.txt", O_RDONLY);
    if (fd == -1) {
        perror("open");  // "open: Not a directory"
        fprintf(stderr, "errno: %d (ENOTDIR)\n", errno);
    }
    return 0;
}
```

Calling `opendir()` on a regular file:

```c
#include <dirent.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    DIR *dir = opendir("/etc/hosts");
    if (dir == NULL) {
        perror("opendir");  // "opendir: Not a directory"
        fprintf(stderr, "errno: %d (ENOTDIR)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-20 ENOTDIR](/languages/c/errno-enotdir/) — not a directory (numeric).
- [errno-20 ENOTDIR](/languages/c/errno-enotdir/) — component in path is not a directory.
- [errno-2 ENOENT](/languages/c/errno-enotdir/) — no such file or directory.
