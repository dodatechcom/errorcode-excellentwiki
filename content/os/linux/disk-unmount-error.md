---
title: "[Solution] Linux: disk-unmount-error — disk unmount error"
description: "Fix Linux disk-unmount-error errors. disk unmount error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 6
---
# Linux: Disk Unmount Error

An unmount error occurs when a filesystem cannot be detached because processes or the kernel are using it.

## Common Causes

- Processes have open files on the filesystem
- Processes have their working directory on the filesystem
- Kernel threads or swap files using the filesystem
- Filesystem has mount --bind creating additional references
- NFS exports still active on the filesystem

## How to Fix

### 1. Find Processes Using the Filesystem

```bash
sudo fuser -vm /mount/point
sudo lsof | grep /mount/point
```

### 2. Kill Processes or Wait

```bash
sudo fuser -km /mount/point
```

### 3. Force Unmount

```bash
# Lazy unmount
sudo umount -l /mount/point
# Force unmount (NFS)
sudo umount -f /mount/point
```

### 4. Use systemd

```bash
sudo systemctl stop <mountpoint>.mount
```

## Examples

```bash
$ sudo umount /mnt
umount: /mnt: target is busy.

$ sudo fuser -vm /mnt
                     USER        PID ACCESS COMMAND
/mnt:                jdoe       4567 cwd
                     jdoe      19876 .c.. bash

$ sudo umount -l /mnt
# Filesystem detached
```
