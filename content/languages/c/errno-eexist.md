---
title: "[Solution] C errno EEXIST — File exists Fix"
description: "Fix C EEXIST (File exists) by handling O_EXCL flags, checking for existing files, and using atomic creation patterns."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EEXIST — File exists Fix

When a process attempts to create a file that already exists using `O_CREAT | O_EXCL` flags, or attempts to create a hard link to an existing file, the system call fails and sets `errno` to `EEXIST`. This error is useful for implementing atomic file creation patterns.

## Common Causes

- Using `open()` with `O_CREAT | O_EXCL` when the file already exists.
- Calling `link()` where the target path already exists.
- Creating a directory with `mkdir()` where the directory already exists.
- Creating a Unix domain socket (`bind()`) when the socket file already exists.

## How to Fix

Use `O_CREAT | O_EXCL` for atomic creation and handle `EEXIST` to distinguish between "file doesn't exist" and "file already exists" cases.

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("lockfile.lock", O_CREAT | O_EXCL | O_WRONLY, 0644);
    if (fd == -1) {
        if (errno == EEXIST) {
            fprintf(stderr, "Another process is already running\n");
        } else {
            fprintf(stderr, "open failed: %s\n", strerror(errno));
        }
        return 1;
    }
    // Lock acquired — write PID, then close
    dprintf(fd, "%d\n", getpid());
    close(fd);
    return 0;
}
```

## Examples

Creating a directory that already exists:

```c
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    if (mkdir("/tmp/mydir", 0755) == -1) {
        if (errno == EEXIST) {
            printf("Directory already exists\n");
        } else {
            perror("mkdir");
        }
    }
    return 0;
}
```

Creating a hard link where the target exists:

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    if (link("existing.txt", "newlink.txt") == -1) {
        if (errno == EEXIST) {
            printf("Link target already exists\n");
        } else {
            perror("link");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-17 EEXIST](/languages/c/errno-eexist/) — file exists (numeric).
- [errno-2 ENOENT](/languages/c/errno-eexist/) — no such file or directory.
- [errno-20 ENOTDIR](/languages/c/errno-eexist/) — not a directory.
