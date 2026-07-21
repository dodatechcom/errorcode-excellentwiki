---
title: "[Solution] Ubuntu Server: kernel-boot-partition-full"
description: "Fix Ubuntu kernel-boot-partition-full. /boot partition full preventing kernel updates."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Boot Partition Full

The /boot partition has run out of space.

## Common Causes
- Too many old kernel images accumulated
- /boot partition too small
- Large initramfs images
- Large vmlinuz and System.map files

## How to Fix
1. Check current usage
```bash
df -h /boot
ls -lh /boot/
```
2. Remove old kernels
```bash
sudo apt autoremove --purge
```
3. Manually remove specific old kernel
```bash
sudo dpkg -l | grep linux-image
sudo apt remove linux-image-5.4.0-100-generic
```

## Examples
```bash
$ df -h /boot
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       477M  467M    0M 100% /boot
```
