---
title: "[Solution] C errno 16 EBUSY — Device or resource busy"
description: "Fix C errno 16 EBUSY (Device or resource busy) by unmounting the device, stopping processes using it, or waiting for release."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["ebusy", "errno-16", "device", "busy", "mount"]
weight: 5
---

# [Solution] C errno 16 EBUSY — Device or resource busy

Device or resource busy occurs when a system call fails and sets `errno` to 16. This error indicates that the requested operation cannot be performed due to the specific condition described by EBUSY.

## Common Causes

- Trying to unmount a device that is still in use.
- Attempting to rename or delete a file that is currently open by another process.
- Trying to mount a device that is already mounted.
- Attempting to write to a block device that is in use.

## How to Fix

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    FILE *fp = fopen("/dev/sda1", "w");
    if (fp == NULL) {
        fprintf(stderr, "fopen failed: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    fclose(fp);
    return 0;
}
```

## Examples

```c
#include <sys/mount.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    if (umount("/mnt/data") == -1) {
        perror("umount");  // "umount: Device or resource busy"
    }
    return 0;
}
```

## Related Errors

- [errno-16 EBUSY]({{< relref "/languages/c/errno-16" >}}) — device or resource busy (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-30 EROFS]({{< relref "/languages/c/errno-30" >}}) — read-only file system.
