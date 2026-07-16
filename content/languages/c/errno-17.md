---
title: "[Solution] C errno 17 EEXIST — File exists"
description: "Fix C errno 17 EEXIST (File exists) by using O_EXCL flag appropriately, removing existing file first, or checking existence before creation."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eexist", "errno-17", "file", "exists", "create"]
weight: 5
---

# [Solution] C errno 17 EEXIST — File exists

File exists occurs when a system call fails and sets `errno` to 17. This error indicates that the requested operation cannot be performed due to the specific condition described by EEXIST.

## Common Causes

- Trying to create a file that already exists without O_EXCL flag.
- Attempting to rename a file to a name that already exists.
- Trying to create a directory that already exists.
- Using open() with O_CREAT | O_EXCL on an existing file.

## How to Fix

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("existing.txt", O_CREAT | O_EXCL, 0644);
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
#include <stdio.h>
#include <errno.h>

int main(void) {
    FILE *fp = fopen("existing.txt", "r");
    if (fp == NULL && errno == EEXIST) {
        printf("File already exists\n");
    }
    return 0;
}
```

## Related Errors

- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-17 EEXIST]({{< relref "/languages/c/errno-17" >}}) — file exists (self).
- [errno-20 ENOTDIR]({{< relref "/languages/c/errno-20" >}}) — not a directory.
