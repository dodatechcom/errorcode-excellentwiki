---
title: "[Solution] Ubuntu Server: grub-recovery-mode-fail"
description: "Fix Ubuntu grub-recovery-mode-fail. GRUB recovery mode fails to boot into a working shell."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB Recovery Mode Fail

GRUB recovery mode itself fails to boot.

## Common Causes
- Recovery partition or initrd missing
- Filesystem errors on /boot
- Incorrect GRUB menu entry for recovery
- core.img corrupted

## How to Fix
1. Use live USB to mount and repair
```bash
sudo mount /dev/sda1 /mnt
sudo mount --bind /dev /mnt/dev
sudo chroot /mnt
```
2. Reinstall GRUB
```bash
grub-install /dev/sda
update-grub
```
3. Rebuild initramfs
```bash
update-initramfs -u -k all
```

## Examples
```bash
$ sudo mount /dev/sda2 /mnt
$ sudo mount /dev/sda1 /mnt/boot
$ sudo chroot /mnt
$ update-grub
```
