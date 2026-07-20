---
title: "[Solution] Linux: disk-resize-error — disk resize error"
description: "Fix Linux disk-resize-error errors. disk resize error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: Disk Resize Error

Disk resize errors occur when expanding or shrinking a partition or filesystem fails due to constraints or improper procedure.

## Common Causes

- Partition cannot be resized because it is currently mounted
- Insufficient free space after the partition to extend into
- Filesystem does not support shrinking (XFS can only grow)
- Volume group has no free extents for LVM extension
- Partition type mismatch between partition table and filesystem

## How to Fix

### 1. Check Current Layout

```bash
lsblk
df -h
sudo fdisk -l /dev/sdX
```

### 2. Grow Filesystem

```bash
# ext4
sudo resize2fs /dev/sdX

# XFS (must be mounted)
sudo xfs_growfs /mount/point

# LVM with auto-resize
sudo lvextend -r -L +10G <vg_name>/<lv_name>
```

### 3. Resize Partition with parted

```bash
sudo parted /dev/sdX resizepart 1 100%
sudo growpart /dev/sdX 1
```

## Examples

```bash
$ sudo lvextend -r -L +10G vg01/root
  Size of logical volume vg01/root changed from 50.00 GiB to 60.00 GiB.
  File system ext4 at / has been resized.

$ sudo xfs_growfs /data
data blocks changed from 26214400 to 31457280
```
