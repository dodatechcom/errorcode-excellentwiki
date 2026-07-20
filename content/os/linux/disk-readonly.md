---
title: "[Solution] Linux: disk-readonly — disk read-only error"
description: "Fix Linux disk-readonly errors. disk read-only error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: Read-Only Filesystem Error

A read-only filesystem error occurs when the kernel remounts a filesystem as read-only after detecting write failures. This protects against further data corruption.

## Common Causes

- Filesystem errors detected during write operations triggering safety remount
- Disk I/O errors from failing hardware causing the kernel to force read-only
- Corrupted superblock or journal preventing write operations
- Filesystem reaching maximum mount count without fsck
- Hardware RAID controller marking LUN as read-only

## How to Fix

### 1. Check Kernel Messages

```bash
dmesg | grep -iE "read-only|re-mounted|remount" | tail -20
journalctl -k -p err | grep -i "remount"
```

### 2. Check Filesystem Status

```bash
mount | grep "ro,"
cat /proc/mounts | grep "ro "
```

### 3. Attempt Safe Remount Read-Write

```bash
sudo mount -o remount,rw /mount/point
```

### 4. Run Filesystem Check

```bash
sudo fsck -f /dev/sdX
```

### 5. Force Remount

```bash
sudo mount -o remount,rw,force /mount/point
```

## Examples

```bash
$ mount | grep "/ "
/dev/sda1 on / type ext4 (ro,relatime,errors=remount-ro)

$ sudo mount -o remount,rw /
mount: /: cannot remount /dev/sda1 read-write

$ sudo fsck -f /dev/sda1
/dev/sda1: clean, 123456/1000000 files, 987654/4000000 blocks

$ sudo mount -o remount,rw /
# Now succeeds
```
