---
title: "[Solution] Ubuntu Server: grub-bios-mbr-corruption"
description: "Fix Ubuntu grub-bios-mbr-corruption. Master Boot Record containing GRUB is corrupted."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB BIOS MBR Corruption

The MBR containing GRUB boot code is corrupted.

## Common Causes
- Windows installation overwrote MBR
- Malware or disk tool modified MBR
- Disk utility wrote to MBR
- Failed GRUB installation

## How to Fix
1. Boot from live USB
```bash
sudo mount /dev/sda2 /mnt
sudo grub-install --root-directory=/mnt /dev/sda
```
2. Restore GRUB from chroot
```bash
sudo mount /dev/sda2 /mnt
sudo mount /dev/sda1 /mnt/boot
sudo chroot /mnt
grub-install /dev/sda
update-grub
```

## Examples
```bash
$ sudo grub-install /dev/sda
Installing for i386-pc platform.
Installation finished. No error reported.
```
