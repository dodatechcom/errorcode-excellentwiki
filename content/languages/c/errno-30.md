---
title: "[Solution] C errno 30 EROFS — Read-only file system"
description: "Fix C errno 30 EROFS (Read-only file system) by mounting file system as read-write, checking mount options, or using read-only operations."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 30 EROFS — Read-only file system

Read-only file system occurs when a system call fails and sets `errno` to 30. This error indicates that the requested operation cannot be performed due to the specific condition described by EROFS.

## Common Causes

- Trying to write to a file system mounted as read-only.
- Attempting to create or modify files on a read-only media.
- Modifying system directories that are intentionally read-only.
- Trying to remount a file system without proper permissions.

## How to Fix

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/proc/sysrq-trigger", O_WRONLY);
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
#include <sys/vfs.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct statfs buf;
    if (statfs("/", &buf) == 0) {
        if (buf.f_flags & ST_RDONLY) {
            printf("Root file system is read-only\n");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-30 EROFS]({{< relref "/languages/c/errno-30" >}}) — read-only file system (self).
- [errno-28 ENOSPC]({{< relref "/languages/c/errno-28" >}}) — no space left on device.
