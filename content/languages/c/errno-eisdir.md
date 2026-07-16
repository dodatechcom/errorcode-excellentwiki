---
title: "[Solution] C errno EISDIR — Is a directory Fix"
description: "Fix C EISDIR (Is a directory) by checking file types before read/write operations and handling directories correctly."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eisdir", "is-a-directory", "file-type", "open-directory"]
weight: 5
---

# [Solution] C errno EISDIR — Is a directory Fix

When a process attempts to open a directory for reading or writing as if it were a regular file, the system call fails and sets `errno` to `EISDIR`. This error indicates that the path refers to a directory, not a regular file.

## Common Causes

- Calling `open()` with `O_WRONLY` or `O_RDWR` on a directory path.
- Attempting `write()` or `fwrite()` to a directory descriptor.
- Using `mmap()` on a directory file descriptor.
- Passing a directory path to functions that expect regular files (e.g., `fopen()` with "w" mode).

## How to Fix

Check whether the path is a directory before opening it for writing. Use `opendir()`/`readdir()` for directory traversal, or open directories read-only with `O_RDONLY`.

```c
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    struct stat st;
    if (stat("/tmp", &st) == -1) {
        fprintf(stderr, "stat failed: %s\n", strerror(errno));
        return 1;
    }
    if (S_ISDIR(st.st_mode)) {
        fprintf(stderr, "/tmp is a directory — cannot open for writing\n");
        return 1;
    }
    // Safe to open for writing
    return 0;
}
```

## Examples

Trying to open a directory for writing:

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fd = open("/tmp", O_WRONLY);
    if (fd == -1) {
        perror("open");  // "open: Is a directory"
        fprintf(stderr, "errno: %d (EISDIR)\n", errno);
    }
    return 0;
}
```

Writing to a directory descriptor:

```c
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fd = open("/tmp", O_RDONLY | O_DIRECTORY);
    if (fd == -1) { perror("open"); return 1; }
    ssize_t n = write(fd, "data", 4);
    if (n == -1) {
        perror("write");  // "write: Is a directory"
        fprintf(stderr, "errno: %d (EISDIR)\n", errno);
    }
    close(fd);
    return 0;
}
```

## Related Errors

- [errno-20 ENOTDIR](/languages/c/errno-eisdir/) — not a directory (opposite case).
- [errno-13 EPERM](/languages/c/errno-eisdir/) — operation not permitted.
- [errno-13 EACCES]({{< relref "/languages/c/errno-eacces" >}}) — permission denied.
