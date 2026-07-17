---
title: "[Solution] C Read-only file system: EROFS"
description: "Fix C read-only file system (EROFS). Mount filesystem as read-write or use writable paths."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["erofs", "read-only-file-system", "mount", "filesystem", "errno"]
weight: 5
---

# Read-only file system: EROFS

EROFS occurs when you try to write to a filesystem mounted as read-only. This can happen on CD-ROMs, certain mount options, or when the filesystem has errors.

## Common Causes

```c
// Cause 1: Writing to read-only mount
int fd = open("/mnt/cdrom/file.txt", O_WRONLY); // EROFS

// Cause 2: Filesystem remounted read-only due to errors
// Linux remounts ext4 as read-only on corruption

// Cause 3: Writing to /boot or similar protected path
int fd = open("/boot/kernel", O_WRONLY); // EROFS
```

## How to Fix

### Fix 1: Remount as read-write

```bash
mount -o remount,rw /mnt/data
```

### Fix 2: Check filesystem errors

```bash
fsck /dev/sda1
```

### Fix 3: Use writable path

```c
// Write to /tmp instead
int fd = open("/tmp/file.txt", O_WRONLY | O_CREAT, 0644);
```

## Related Errors

- [Permission denied]({{< relref "/languages/c/permission-denied-file" >}}) — EACCES.
- [No space left]({{< relref "/languages/c/no-space-left" >}}) — ENOSPC.
- [Input/output error]({{< relref "/languages/c/input-output-error" >}}) — EIO.
