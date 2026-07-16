---
title: "[Solution] C errno 28 ENOSPC — No space left on device"
description: "Fix C errno 28 ENOSPC (No space left on device) by freeing disk space, checking quotas, or using smaller writes."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enospc", "errno-28", "disk-full", "no-space", "storage"]
weight: 5
---

# [Solution] C errno 28 ENOSPC — No space left on device

No space left on device occurs when a system call fails and sets `errno` to 28. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOSPC.

## Common Causes

- Disk partition is full.
- User quota has been exceeded.
- Inode limit reached (no free inodes).
- Trying to write to a read-only file system.

## How to Fix

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    FILE *fp = fopen("/tmp/test.txt", "w");
    if (fp == NULL) {
        fprintf(stderr, "fopen failed: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    // Write until disk full
    char buffer[1024] = {0};
    while (fwrite(buffer, 1, sizeof(buffer), fp) > 0) {}
    fclose(fp);
    return 0;
}
```

## Examples

```c
#include <sys/statvfs.h>
#include <stdio.h>

int main(void) {
    struct statvfs stat;
    if (statvfs("/", &stat) == 0) {
        unsigned long free_blocks = stat.f_bavail;
        printf("Free blocks: %lu\n", free_blocks);
    }
    return 0;
}
```

## Related Errors

- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
- [errno-28 ENOSPC]({{< relref "/languages/c/errno-28" >}}) — no space left on device (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
