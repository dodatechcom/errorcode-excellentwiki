---
title: "[Solution] C errno ENOLINK — Link has been severed Fix"
description: "Fix C ENOLINK (Link has been severed) by handling broken symbolic links and NFS stale file handles."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENOLINK — Link has been severed Fix

When a process attempts to access a file through a symbolic link that no longer exists (the link target has been removed while the link remains), the system call fails and sets `errno` to `ENOLINK`. This error indicates a broken link in the path resolution chain.

## Common Causes

- A symbolic link points to a file that has been deleted.
- An NFS mount point is stale or the server is unreachable.
- A filesystem was unmounted while a process had an open file through a link.
- The link target was replaced or moved during path resolution.

## How to Fix

Check for broken links before accessing files. Use `lstat()` to verify link targets exist.

```c
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct stat st;
    if (lstat("/path/to/symlink", &st) == -1) {
        perror("lstat");
        return 1;
    }
    if (S_ISLNK(st.st_mode)) {
        // Follow the link and check if target exists
        if (stat("/path/to/symlink", &st) == -1) {
            if (errno == ENOLINK) {
                fprintf(stderr, "Symbolic link target does not exist\n");
            }
        }
    }
    return 0;
}
```

## Examples

Accessing a broken symbolic link:

```bash
# Create and then break a symlink
ln -s /tmp/target /tmp/link
rm /tmp/target
cat /tmp/link  # ENOLINK
```

Detecting broken links programmatically:

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    char resolved[PATH_MAX];
    if (realpath("/tmp/broken_link", resolved) == NULL) {
        if (errno == ENOLINK) {
            fprintf(stderr, "Broken link detected (errno %d)\n", errno);
        } else {
            perror("realpath");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-37 ENOLINK]({{< relref "/languages/c/errno-eNOLINK" >}}) — link has been severed (numeric).
- [errno-2 ENOENT](/languages/c/errno-eNOLINK/) — no such file or directory.
- [errno-116 ESTALE]({{< relref "/languages/c/errno-eSTALE" >}}) — stale file handle.
