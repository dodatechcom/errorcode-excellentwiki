---
title: "[Solution] C errno ENAMETOOLONG — File name too long Fix"
description: "Fix C ENAMETOOLONG (File name too long) by shortening path components and checking NAME_MAX limits."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enametoolong", "file-name-too-long", "path-limit", "name-max"]
weight: 5
---

# [Solution] C errno ENAMETOOLONG — File name too long Fix

When a filename or path component exceeds the maximum allowed length, the system call fails and sets `errno` to `ENAMETOOLONG`. On Linux, the maximum filename length is 255 bytes (`NAME_MAX`), and the maximum path length is typically 4096 bytes (`PATH_MAX`).

## Common Causes

- The filename exceeds 255 characters (the `NAME_MAX` limit).
- The full path exceeds 4096 characters (the `PATH_MAX` limit).
- A path component in `mkdir()`, `open()`, or `rename()` is too long.
- User input generates unexpectedly long filenames without validation.

## How to Fix

Validate filename and path lengths before performing filesystem operations.

```c
#include <limits.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int main(void) {
    char longname[300];
    memset(longname, 'a', 256);
    longname[256] = '\0';

    if (mkdir(longname, 0755) == -1) {
        if (errno == ENAMETOOLONG) {
            fprintf(stderr, "Filename too long: %zu characters (max %d)\n",
                    strlen(longname), 255);
        } else {
            perror("mkdir");
        }
        return 1;
    }
    return 0;
}
```

## Examples

Creating a file with an excessively long name:

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char name[300];
    memset(name, 'x', 256);
    name[256] = '\0';

    int fd = open(name, O_CREAT | O_WRONLY, 0644);
    if (fd == -1) {
        perror("open");  // "open: File name too long"
        fprintf(stderr, "errno: %d (ENAMETOOLONG)\n", errno);
    }
    return 0;
}
```

Using a path that is too long:

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char longpath[5000];
    memset(longpath, 'a', 4097);
    longpath[4097] = '\0';

    if (access(longpath, F_OK) == -1) {
        if (errno == ENAMETOOLONG) {
            fprintf(stderr, "Path too long (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-36 ENAMETOOLONG](/languages/c/errno-eNAMETOOLONG/) — file name too long (numeric).
- [errno-2 ENOENT](/languages/c/errno-eNAMETOOLONG/) — no such file or directory.
- [errno-20 ENOTDIR](/languages/c/errno-eNAMETOOLONG/) — not a directory.
