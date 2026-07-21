---
title: "[Solution] Ubuntu Server: grub-entry-not-found"
description: "Fix Ubuntu grub-entry-not-found. GRUB cannot find the specified boot menu entry."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# GRUB Entry Not Found

GRUB shows an error that the specified boot entry does not exist.

## Common Causes
- grub.cfg regenerated without expected entry
- Custom menu entry file removed
- Kernel entry not generated
- BTRFS subvolume layout changed

## How to Fix
1. List available GRUB entries
```bash
grep menuentry /boot/grub/grub.cfg
```
2. Edit GRUB to boot manually
```bash
set root=(hd0,gpt2)
linux /boot/vmlinuz-<version> root=/dev/sda2
initrd /boot/initrd.img-<version>
boot
```
3. Regenerate configuration
```bash
sudo update-grub
```

## Examples
```bash
$ grep menuentry /boot/grub/grub.cfg
menuentry 'Ubuntu' --class ubuntu {
menuentry 'Ubuntu, with Linux 5.15.0-25-generic' {
```
