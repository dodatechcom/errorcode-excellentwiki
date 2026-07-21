---
title: "[Solution] Ubuntu Server: kernel-grub-rescue-mode"
description: "Fix Ubuntu kernel-grub-rescue-mode. System drops into GRUB rescue mode on boot."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Kernel Grub Rescue Mode

System drops into GRUB rescue mode because it cannot find the boot partition.

## Common Causes
- GRUB prefix set to wrong partition
- /boot partition UUID changed
- Partition table corruption
- Dual-boot configuration broken

## How to Fix
1. Identify available partitions
```bash
grub> ls
```
2. Set correct prefix and root
```bash
grub> set root=(hd0,msdos1)
grub> set prefix=(hd0,msdos1)/boot/grub
grub> insmod normal
grub> normal
```
3. Reinstall GRUB from live USB
```bash
sudo mount /dev/sda1 /mnt
sudo grub-install --root-directory=/mnt /dev/sda
```

## Examples
```bash
grub> ls
(hd0) (hd0,msdos2) (hd0,msdos1)
grub> set root=(hd0,msdos1)
grub> insmod normal
```
