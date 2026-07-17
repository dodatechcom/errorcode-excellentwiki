---
title: "[Solution] C errno 20 ENOTDIR — Not a directory"
description: "Fix C errno 20 ENOTDIR (Not a directory) by verifying path components are directories and using correct path separators."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 20 ENOTDIR — Not a directory

Not a directory occurs when a system call fails and sets `errno` to 20. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOTDIR.

## Common Causes

- Trying to open a file using a path where a component is not a directory.
- Attempting to change directory to a regular file.
- Using a file path in a function that expects a directory (e.g., readdir).
- Trying to access a directory entry inside a non-directory.

## How to Fix

```c
#include <dirent.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    DIR *dir = opendir("/etc/hosts");
    if (dir == NULL) {
        fprintf(stderr, "opendir failed: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    closedir(dir);
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
    if (stat("/etc/hosts", &st) == -1) {
        perror("stat");
        return 1;
    }
    if (!S_ISDIR(st.st_mode)) {
        fprintf(stderr, "Not a directory: /etc/hosts\n");
    }
    return 0;
}
```

## Related Errors

- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-20 ENOTDIR]({{< relref "/languages/c/errno-20" >}}) — not a directory (self).
- [errno-21 EISDIR]({{< relref "/languages/c/errno-21" >}}) — is a directory.
