---
title: "[Solution] Ubuntu Server: kernel-ubuntu-panic-on-boot"
description: "Fix Ubuntu kernel-ubuntu-panic-on-boot. Kernel panic during boot prevents system startup."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Ubuntu Panic On Boot

System hits a kernel panic during the boot process.

## Common Causes
- Corrupted root filesystem
- Missing or corrupt initramfs image
- Incompatible kernel for hardware
- Storage driver missing from initramfs

## How to Fix
1. Boot from recovery mode or live USB
2. Check GRUB kernel parameters
```bash
cat /proc/cmdline
```
3. Regenerate initramfs
```bash
sudo update-initramfs -u
```
4. Rebuild GRUB
```bash
sudo grub-install /dev/sda
sudo update-grub
```

## Examples
```bash
$ dmesg | tail -20
[    1.234] Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)
[    1.234] CPU: 0 PID: 1 Comm: swapper/0 Not tainted 5.15.0-25-generic
```
