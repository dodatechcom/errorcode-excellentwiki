---
title: "[Solution] Linux: device-busy — device or resource busy"
description: "Fix Linux device-busy errors. device or resource busy with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 6
---

# Linux: Device Busy Error

The device busy error occurs when trying to unmount, format, or modify a disk that is currently in use.

## Common Causes

- Filesystem mounted and in use by processes
- Swap enabled on the device
- LVM volume active
- MD RAID array member in use
- Filesystem check running on the device

## How to Fix

### 1. Identify Processes Using the Device

```bash
sudo lsof /dev/sda1
sudo fuser -v /mount/point
```

### 2. Check Mount Status

```bash
mount | grep sda1
df -h | grep sda1
```

### 3. Force Unmount

```bash
sudo umount -l /mount/point
sudo umount -f /mount/point
```

### 4. Kill Using Processes

```bash
sudo fuser -km /mount/point
```

## Examples

```bash
$ sudo umount /mnt/data
umount: /mnt/data: target is busy.
$ sudo lsof /mnt/data
COMMAND  PID USER   FD   TYPE DEVICE SIZE NODE NAME
bash    12345 root  cwd    DIR  8,1   4096    2 /mnt/data
$ kill 12345
$ sudo umount /mnt/data
# Now succeeds
```
