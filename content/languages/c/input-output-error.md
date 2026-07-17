---
title: "[Solution] C Input/output error: EIO"
description: "Fix C input/output error (EIO). Handle hardware and driver-level I/O failures."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["eio", "input-output-error", "hardware", "driver", "errno"]
weight: 5
---

# Input/output error: EIO

EIO is a generic I/O error indicating the kernel encountered a problem communicating with hardware or a driver. This is often unrecoverable.

## Common Causes

```c
// Cause 1: Disk hardware failure
read(fd, buf, 100); // EIO — bad disk sector

// Cause 2: Corrupted filesystem
read(fd, buf, 100); // EIO — filesystem damage

// Cause 3: Device driver error
read(fd, buf, 100); // EIO — driver problem
```

## How to Fix

### Fix 1: Check hardware

```bash
dmesg | grep -i error
smartctl -a /dev/sda
```

### Fix 2: Check filesystem

```bash
fsck /dev/sda1
# or
e2fsck -f /dev/sda1
```

### Fix 3: Retry the operation

```c
for (int i = 0; i < 3; i++) {
    ssize_t result = read(fd, buf, size);
    if (result >= 0) break;
    if (errno != EIO) break;
    usleep(1000 * (1 << i)); // exponential backoff
}
```

## Related Errors

- [Bad file descriptor]({{< relref "/languages/c/bad-file-descriptor" >}}) — EBADF.
- [Input/output error]({{< relref "/languages/c/input-output-error" >}}) — detailed analysis.
- [Read-only file system]({{< relref "/languages/c/read-only-file-system" >}}) — EROFS.
