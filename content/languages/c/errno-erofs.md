---
title: "[Solution] C errno EROFS — Read-only file system Fix"
description: "Fix C EROFS (Read-only file system) by remounting filesystems read-write or avoiding writes to read-only mounts."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EROFS — Read-only file system Fix

When a process attempts to modify a file on a read-only filesystem, the system call fails and sets `errno` to `EROFS`. This error occurs when the filesystem is mounted read-only, either by configuration or due to filesystem corruption triggering a read-only remount.

## Common Causes

- The filesystem is mounted with the `ro` (read-only) option.
- The filesystem was remounted read-only after I/O errors (kernel protective measure).
- The root filesystem is read-only during early boot or in embedded systems.
- CD-ROM, DVD, or write-protected media is mounted.

## How to Fix

Remount the filesystem read-write if modification is needed, or avoid writing to read-only filesystems.

```bash
# Remount a filesystem as read-write
mount -o remount,rw /path/to/mount

# Check mount options
mount | grep " / "
```

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>

int main(void) {
    int fd = open("/readonly/data.txt", O_WRONLY | O_CREAT, 0644);
    if (fd == -1) {
        if (errno == EROFS) {
            fprintf(stderr, "Filesystem is read-only — cannot write\n");
        } else {
            fprintf(stderr, "open failed: %s\n", strerror(errno));
        }
        return 1;
    }
    close(fd);
    return 0;
}
```

## Examples

Writing to a read-only mounted filesystem:

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Suppose /mnt/rom is a read-only filesystem
    FILE *fp = fopen("/mnt/rom/test.txt", "w");
    if (fp == NULL) {
        perror("fopen");  // "fopen: Read-only file system"
        fprintf(stderr, "errno: %d (EROFS)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-30 EROFS](/languages/c/errno-erofs/) — read-only file system (numeric).
- [errno-13 EACCES]({{< relref "/languages/c/errno-eacces" >}}) — permission denied.
- [errno-13 EPERM](/languages/c/errno-erofs/) — operation not permitted.
