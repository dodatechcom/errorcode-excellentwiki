---
title: "[Solution] Ubuntu Server: ubuntu-raid-missing-disk"
description: "Fix Ubuntu ubuntu-raid-missing-disk. RAID array reports missing disk."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu RAID Missing Disk

RAID array reports a disk as missing or faulty.

## Common Causes
- Disk physically removed
- Disk not detected by kernel
- SATA/SAS cable issue

## How to Fix
1. Check array status
```bash
cat /proc/mdstat
```
2. Scan for disks
```bash
sudo mdadm --examine /dev/sd*
lsblk
```
3. Add missing disk back
```bash
sudo mdadm --add /dev/md0 /dev/sdb1
```

## Examples
```bash
$ cat /proc/mdstat
md0 : active raid1 sda1[0]
      1048576 blocks [2/1] [U_]
```