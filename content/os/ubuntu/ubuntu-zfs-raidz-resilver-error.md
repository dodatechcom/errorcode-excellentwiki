---
title: "[Solution] Ubuntu Server: ubuntu-zfs-raidz-resilver-error"
description: "Fix Ubuntu ubuntu-zfs-raidz-resilver-error. ZFS RAIDZ resilver fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu ZFS RAIDZ Resilver Error

ZFS RAIDZ resilver operation fails or is extremely slow.

## Common Causes
- Disk replacement not properly added
- Scrub conflicting with resilver
- Insufficient free space for resilver

## How to Fix
1. Check resilver status
```bash
sudo zpool status tank
```
2. Wait for resilver to complete
```bash
watch -n 10 sudo zpool status tank
```
3. Cancel and retry if stuck
```bash
sudo zpool cancel tank
sudo zpool scrub tank
```

## Examples
```bash
$ sudo zpool status tank
  scan: resilver in progress since Mon Mar 15 10:00:00 2023
        50.0G scanned at 100M/s, 25.0G issued at 50M/s
        25.0G resilvered, 25.00% done
```