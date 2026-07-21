---
title: "[Solution] Ubuntu Server: ubuntu-raid-shape-error"
description: "Fix Ubuntu ubuntu-raid-shape-error. RAID reshape operation fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu RAID Shape Error

RAID array reshape (e.g., RAID1 to RAID5) fails.

## Common Causes
- Reshape interrupted by crash
- Disk space insufficient
- Unsupported reshape operation

## How to Fix
1. Check array status
```bash
cat /proc/mdstat
```
2. Resume reshape if interrupted
```bash
sudo mdadm --reshape --continue /dev/md0
```
3. Monitor reshape progress
```bash
watch -n 5 cat /proc/mdstat
```

## Examples
```bash
$ cat /proc/mdstat
md0 : active raid5 sda1[0] sdb1[2] sdc1[1]
      reshape = 20.0% finish=30min speed=100000K/sec
```