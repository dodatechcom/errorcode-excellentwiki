---
title: "[Solution] C No space left on device: ENOSPC"
description: "Fix C no space left on device (ENOSPC). Free disk space and handle allocation failures."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["enospc", "no-space-left", "disk-full", "quota", "errno"]
weight: 5
---

# No space left on device: ENOSPC

ENOSPC occurs when the disk is full, the inode limit is reached, or the user has exceeded their disk quota. Write operations fail.

## Common Causes

```c
// Cause 1: Disk is full
write(fd, data, len); // ENOSPC

// Cause 2: Inode limit reached
// Many small files consuming all inodes

// Cause 3: User quota exceeded
// User's disk quota reached
```

## How to Fix

### Fix 1: Check disk space

```bash
df -h
df -i  # check inodes
```

### Fix 2: Free disk space

```bash
du -sh * | sort -rh | head
rm -f large_file.log
```

### Fix 3: Check inode usage

```bash
df -i
find / -xdev -printf '%h\n' | sort | uniq -c | sort -rn | head
```

### Fix 4: Write to different location

```c
int fd = open("/tmp/file.txt", O_WRONLY | O_CREAT, 0644);
```

## Examples

```c
#include <stdio.h>
#include <errno.h>
#include <fcntl.h>

int main(void) {
    int fd = open("output.txt", O_WRONLY | O_CREAT, 0644);
    if (fd == -1) {
        if (errno == ENOSPC) {
            fprintf(stderr, "Disk full!\n");
        }
        perror("open");
        return 1;
    }
    
    ssize_t written = write(fd, "data", 4);
    if (written == -1 && errno == ENOSPC) {
        fprintf(stderr, "No space left\n");
    }
    
    close(fd);
    return 0;
}
```

## Related Errors

- [Too many links]({{< relref "/languages/c/too-many-links" >}}) — EMLINK.
- [Too many open files]({{< relref "/languages/c/too-many-open-files" >}}) — EMFILE.
- [Input/output error]({{< relref "/languages/c/input-output-error" >}}) — EIO.
