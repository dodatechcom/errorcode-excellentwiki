---
title: "[Solution] Ubuntu Server: system-mount-error"
description: "Fix Ubuntu system-mount-error. systemd mount unit fails to mount filesystem."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Mount Error

A systemd mount unit fails to mount a filesystem.

## Common Causes
- Mount unit configuration incorrect
- Device not available at mount time
- fstab entry missing or wrong
- Filesystem type not supported

## How to Fix
1. Check mount unit status
```bash
sudo systemctl status <mount>.mount
systemctl list-units --type=mount
```
2. Verify mount configuration
```bash
sudo systemctl cat <mount>.mount
```
3. Test mount manually
```bash
sudo mount /dev/sdb1 /mnt/data
```

## Examples
```bash
$ sudo systemctl status data.mount
● data.mount - /mnt/data
   Loaded: loaded
   Active: failed (Result: exit-code)

$ sudo systemctl cat data.mount
[Mount]
What=/dev/sdb1
Where=/mnt/data
Type=ext4
```
