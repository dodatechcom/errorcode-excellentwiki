---
title: "[Solution] Linux: disk-raid-rebuild-error — disk RAID rebuild error"
description: "Fix Linux disk-raid-rebuild-error errors. disk RAID rebuild error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 10
---
# Linux: RAID Rebuild Error

RAID rebuild errors occur when a degraded array cannot successfully reconstruct data onto a replacement disk.

## Common Causes

- Replacement disk smaller than the original member
- Read errors on the remaining good disk preventing reconstruction
- Disk timeout or disconnect during the rebuild process
- Incompatible disk geometry or sector size
- Power loss during rebuild process

## How to Fix

### 1. Stop and Assess

```bash
cat /proc/mdstat
sudo mdadm --detail /dev/md0
dmesg | tail -30
```

### 2. Check All Disks for Errors

```bash
sudo smartctl -A /dev/sdX | grep -E "Reallocated|Pending|Uncorrectable"
```

### 3. Force Rebuild

```bash
# If one disk has issues, try force assemble
sudo mdadm --assemble --force /dev/md0 /dev/sdX1 /dev/sdY1
```

### 4. Ensure Replacement Disk is Large Enough

```bash
sudo fdisk -l /dev/sdY1
sudo blockdev --getsize64 /dev/sdY1
```

## Examples

```bash
$ cat /proc/mdstat
md0 : active raid1 sdc1[2] sdb1[1] sda1[0]
      976762584 blocks super 1.2 [2/3] [U_U]
      resync=DELAYED

$ dmesg | tail -3
[ 5432.123] md/raid1:md0: Disk failure on sdb1, disabling device.
[ 5432.123] md: md0: recovery interrupted
```
