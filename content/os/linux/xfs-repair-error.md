---
title: "[Solution] Linux: xfs-repair-error — XFS repair failed"
description: "Fix Linux xfs-repair-error errors. XFS repair failed with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["filesystem-error"]
weight: 12
---

# Linux: XFS Repair Error Error

XFS repair error errors occur when the XFS high-performance journaling filesystem encounters issues.

## Common Causes

- Filesystem metadata corruption from hardware failure
- Dirty journal requiring log replay
- Allocation group header damage
- Superblock inconsistency
- Storage subsystem write ordering issues

## How to Fix

### 1. Check XFS Status

```bash
sudo xfs_info /mount/point 2>/dev/null
sudo dmesg | grep -i "xfs" | tail -20
```

### 2. Check Filesystem

```bash
sudo umount /mount/point
sudo xfs_repair -n /dev/sda1 2>&1 | head -30
```

### 3. Repair

```bash
sudo xfs_repair /dev/sda1
```

### 4. Force Log Replay

```bash
sudo mount -o force /dev/sda1 /mount/point
```

## Examples

```bash
$ sudo dmesg | grep -i xfs | tail -5
[12345.678] XFS (sda1): Metadata corruption detected at xfs_repair-error

$ sudo xfs_repair /dev/sda1
Phase 1 - find and verify superblock...
Phase 2 - using internal log
Phase 3 - checking AG structures...
Phase 4 - checking inodes...
Phase 5 - rebuilding AG headers...
Phase 6 - checking link counts...
```
