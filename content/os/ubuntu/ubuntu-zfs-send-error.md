---
title: "[Solution] Ubuntu Server: ubuntu-zfs-send-error"
description: "Fix Ubuntu ubuntu-zfs-send-error. ZFS send operation fails during backup."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu ZFS Send Error

ZFS send operation fails during snapshot backup.

## Common Causes
- Snapshot destroyed during send
- Network disconnect during remote send
- Destination pool full

## How to Fix
1. Check snapshot exists
```bash
sudo zfs list -t snapshot
```
2. Use verbose output
```bash
sudo zfs send -v <pool>@<snap> | ssh backup zfs recv <dest>
```
3. Resume interrupted send
```bash
sudo zfs send -t <resume-token> | ssh backup zfs recv <dest>
```

## Examples
```bash
$ sudo zfs list -t snapshot
NAME                    USED  REFER  MOUNTPOINT
tank/data@snap1          1G    500M  -
```