---
title: "[Solution] Linux: disk-filesystem-corrupt — disk filesystem corrupted"
description: "Fix Linux disk-filesystem-corrupt errors. disk filesystem corrupted with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: Corrupt Filesystem

Filesystem corruption occurs when on-disk data structures become damaged. This can prevent mounting, cause data loss, or produce kernel error messages.

## Common Causes

- Unclean shutdown or power loss during write operations
- Failing hardware (bad sectors, memory corruption, cable issues)
- Filesystem bugs or driver issues in the kernel
- Improper unmounting of removable media
- Disk full while writing critical filesystem metadata

## How to Fix

### 1. Identify the Corrupt Filesystem

```bash
dmesg | grep -iE "corrupt|journal|superblock|inode" | tail -20
journalctl -k -p err | grep -iE "ext4|xfs|btrfs"
```

### 2. Unmount the Filesystem

```bash
sudo umount /dev/sdX
# If busy
sudo fuser -vm /mount/point
```

### 3. Run fsck

```bash
sudo fsck -f /dev/sdX
# Specific types
sudo fsck.ext4 -f /dev/sdX
sudo xfs_repair /dev/sdX
sudo btrfs check --repair /dev/sdX
```

### 4. Use Backup Superblock (ext4)

```bash
sudo mke2fs -n /dev/sdX
sudo mount -t ext4 -o sb=32768 /dev/sdX /mnt
```

## Examples

```bash
$ dmesg | grep corrupt
[ 1234.567] EXT4-fs (sda1): ext4_find_entry: deleting previous entry

$ sudo fsck -f /dev/sda1
e2fsck 1.46.5 (30-Dec-2021)
/dev/sda1: recovering journal
/dev/sda1: ***** FILE SYSTEM WAS MODIFIED *****
/dev/sda1: 12345/1000000 files (0.5% non-contiguous), 456789/4000000 blocks
```
