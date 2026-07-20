---
title: "[Solution] Linux: disk-raid-error — disk RAID array error"
description: "Fix Linux disk-raid-error errors. disk RAID array error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 12
---
# Linux: RAID Array Error

RAID errors indicate problems with software RAID arrays managed by mdadm. These can prevent the array from assembling or operating.

## Common Causes

- One or more member disks failing or disconnected
- Superblock mismatch between array members
- Array assembly order incorrect or disks detected out of order
- Write-intent bitmap corrupted after unclean shutdown
- Kernel md driver issue

## How to Fix

### 1. Check RAID Status

```bash
cat /proc/mdstat
sudo mdadm --detail /dev/md0
```

### 2. Examine Member Disks

```bash
sudo mdadm --examine /dev/sdX1
sudo mdadm --examine /dev/sdY1
```

### 3. Stop and Reassemble

```bash
sudo mdadm --stop /dev/md0
sudo mdadm --assemble --scan
sudo mdadm --assemble /dev/md0 /dev/sdX1 /dev/sdY1
```

### 4. Force Assembly

```bash
sudo mdadm --assemble --force /dev/md0
```

## Examples

```bash
$ cat /proc/mdstat
Personalities : [raid1]
md0 : active raid1 sdb1[1] sda1[0]
      976762584 blocks super 1.2 [2/2] [UU]

$ sudo mdadm --detail /dev/md0
/dev/md0:
        Version : 1.2
  Raid Level : raid1
  Array Size : 976762584 (931.51 GiB)
  State : clean
 Active Devices : 2
Working Devices : 2
 Failed Devices : 0
```
