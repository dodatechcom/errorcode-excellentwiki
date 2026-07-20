---
title: "[Solution] Linux: disk-raid-degraded — disk RAID array degraded"
description: "Fix Linux disk-raid-degraded errors. disk RAID array degraded with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 10
---
# Linux: Degraded RAID Array

A degraded RAID array has lost one or more member disks but continues operating with reduced redundancy. This requires immediate attention.

## Common Causes

- A member disk has physically failed or disconnected
- A disk developed bad sectors and was ejected from the array
- Cable or connection issue causing intermittent detection
- Disk timeout causing the kernel to mark it as failed
- Read errors on a disk causing it to be kicked out

## How to Fix

### 1. Check RAID Status

```bash
cat /proc/mdstat
sudo mdadm --detail /dev/md0
```

### 2. Identify the Failed Disk

```bash
sudo mdadm --detail /dev/md0 | grep -i "faulty\|removed\|failed"
dmesg | grep -i raid | tail -20
```

### 3. Replace the Failed Disk

```bash
# Mark as failed
sudo mdadm --manage /dev/md0 --fail /dev/sdX1

# Remove from array
sudo mdadm --manage /dev/md0 --remove /dev/sdX1

# Add replacement disk
sudo mdadm --manage /dev/md0 --add /dev/sdY1
```

### 4. Monitor Rebuild

```bash
watch -n 5 cat /proc/mdstat
```

## Examples

```bash
$ cat /proc/mdstat
Personalities : [raid1]
md0 : active raid1 sdb1[1]
      976762584 blocks super 1.2 [2/1] [_U]

$ sudo mdadm --detail /dev/md0 | grep -E "State|Failed"
    State : clean, degraded
   Failed Devices : 1
```
