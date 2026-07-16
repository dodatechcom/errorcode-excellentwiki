---
title: "[Solution] C errno 40 ELOOP — Too many symbolic links"
description: "Fix C errno 40 ELOOP (Too many symbolic links) by checking for circular symlinks, using realpath, or limiting symlink traversal depth."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eloop", "errno-40", "symbolic-link", "too-many-links", "symlink"]
weight: 5
---

# [Solution] C errno 40 ELOOP — Too many symbolic links

Too many symbolic links occurs when a system call fails and sets `errno` to 40. This error indicates that the requested operation cannot be performed due to the specific condition described by ELOOP.

## Common Causes

- Circular symbolic links (a symlink points to itself or a chain that loops).
- Excessive symlink depth in path resolution.
- A symlink points to a directory that contains another symlink back.
- Trying to open a file with a deeply nested symlink chain.

## How to Fix

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/tmp/circular_link", O_RDONLY);
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
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char resolved[PATH_MAX];
    if (realpath("/tmp/circular_link", resolved) == NULL) {
        perror("realpath");
        return 1;
    }
    printf("Resolved path: %s\n", resolved);
    return 0;
}
```

## Related Errors

- [errno-20 ENOTDIR]({{< relref "/languages/c/errno-20" >}}) — not a directory.
- [errno-40 ELOOP]({{< relref "/languages/c/errno-40" >}}) — too many symbolic links (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
