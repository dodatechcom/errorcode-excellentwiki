---
title: "[Solution] Ubuntu Server: ubuntu-raid1-resync-error"
description: "Fix Ubuntu ubuntu-raid1-resync-error. RAID1 array resync fails or is too slow."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu RAID1 Resync Error

RAID1 array resync operation fails or is extremely slow.

## Common Causes
- Resync speed limit too low
- Disk I/O bottleneck during resync
- Resync was interrupted

## How to Fix
1. Check resync status
```bash
cat /proc/mdstat
```
2. Increase resync speed
```bash
echo 500000 | sudo tee /proc/sys/dev/raid/speed_limit_min
echo 2000000 | sudo tee /proc/sys/dev/raid/speed_limit_max
```
3. Force resync
```bash
sudo mdadm --zero-superblock /dev/sdb1
sudo mdadm --add /dev/md0 /dev/sdb1
```

## Examples
```bash
$ cat /proc/mdstat
md0 : active raid1 sda1[0] sdb1[1]
      1048576 blocks [2/2] [UU]
      [>..........]  recovery = 5.0% finish=10.0min speed=1000K/sec
```