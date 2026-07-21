---
title: "[Solution] Ubuntu Server: kernel-update-initramfs-fail"
description: "Fix Ubuntu kernel-update-initramfs-fail. initramfs update fails during kernel installation."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Update Initramfs Fail

The initramfs image fails to build during a kernel update.

## Common Causes
- Out of disk space in /boot partition
- Missing or broken kernel modules
- Conflicting custom initramfs hooks
- update-initramfs tool failure

## How to Fix
1. Check /boot space
```bash
df -h /boot
```
2. Remove old kernels to free space
```bash
sudo apt autoremove --purge
```
3. Manually rebuild initramfs
```bash
sudo update-initramfs -u -k all
```

## Examples
```bash
$ sudo update-initramfs -u
update-initramfs: Generating /boot/initrd.img-5.15.0-25-generic
E: /etc/initramfs-tools/hooks/drm failed with exit 1.

$ df -h /boot
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       512M  510M     2M 100% /boot
```
