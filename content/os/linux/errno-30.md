---
title: "[Solution] Linux EROFS (errno 30) — Read-only File System Fix"
description: "Fix Linux EROFS (errno 30) Read-only file system error. Solutions for read-only mount and filesystem issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EROFS (errno 30) — Read-only File System

EROFS (errno 30) means an operation was attempted on a filesystem mounted as read-only. This error occurs when you try to create, modify, or delete files on a read-only filesystem. It is distinct from EACCES (errno 13) because EROFS indicates the filesystem itself is read-only, not that the user lacks permissions.

## Common Causes

- The filesystem was mounted read-only with the `ro` option
- The filesystem was remounted read-only due to errors (e.g., after disk corruption)
- The filesystem is a CD-ROM, DVD, or other write-once medium
- A container or chroot environment has a read-only root filesystem

## How to Fix EROFS

### 1. Check Mount Options

Verify if the filesystem is mounted read-only:

```bash
mount | grep " / "
cat /proc/mounts | grep /dev/sda
```

### 2. Remount as Read-Write

Remount the filesystem with write access:

```bash
sudo mount -o remount,rw /
```

### 3. Fix Filesystem Errors

If the filesystem was remounted read-only due to errors, run a filesystem check:

```bash
sudo fsck /dev/sda1
```

### 4. Check for Hardware Issues

Ensure the storage medium is not write-protected:

```bash
sudo hdparm -r /dev/sda
sudo blockdev --setrw /dev/sda
```

## Verification

After remounting as read-write, confirm write access:

```bash
touch /test_write_access && rm /test_write_access && echo "Write access restored"
```

## Related Error Codes

- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [EROFS (errno 30)](/os/linux/errno-30/) — Read-only file system
