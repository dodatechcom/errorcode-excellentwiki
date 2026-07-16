---
title: "[Solution] C errno 21 EISDIR — Is a directory"
description: "Fix C errno 21 EISDIR (Is a directory) by checking if path is a directory before opening for writing or reading as a file."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eisdir", "errno-21", "directory", "is-a-directory", "open"]
weight: 5
---

# [Solution] C errno 21 EISDIR — Is a directory

Is a directory occurs when a system call fails and sets `errno` to 21. This error indicates that the requested operation cannot be performed due to the specific condition described by EISDIR.

## Common Causes

- Trying to open a directory as a regular file for reading/writing.
- Attempting to write to a directory descriptor.
- Trying to read from a directory as if it were a file.
- Using functions like fread/fwrite on a directory.

## How to Fix

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/tmp", O_WRONLY);
    if (fd == -1) {
        fprintf(stderr, "open failed: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    close(fd);
    return 0;
}
```

## Examples

```c
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct stat st;
    if (stat("/tmp", &st) == -1) {
        perror("stat");
        return 1;
    }
    if (S_ISDIR(st.st_mode)) {
        printf("Path is a directory\n");
    }
    return 0;
}
```

## Related Errors

- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-20 ENOTDIR]({{< relref "/languages/c/errno-20" >}}) — not a directory.
- [errno-21 EISDIR]({{< relref "/languages/c/errno-21" >}}) — is a directory (self).
