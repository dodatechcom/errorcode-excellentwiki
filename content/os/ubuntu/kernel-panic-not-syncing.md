---
title: "Kernel Panic - Not Syncing"
description: "Kernel panic occurs with 'not syncing' message preventing system boot"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Kernel Panic - Not Syncing

Kernel panic occurs with 'not syncing' message preventing system boot

## Common Causes

- Root filesystem not found during boot
- Init process failed to execute
- Corrupted kernel image or initramfs
- Hardware failure preventing kernel initialization

## How to Fix

1. Boot from recovery mode or live USB
2. Check root UUID in /boot/grub/grub.cfg and /etc/fstab
3. Regenerate initramfs: `sudo update-initramfs -u`
4. Check disk health: `sudo smartctl -a /dev/sda`

## Examples

```bash
# From live USB, check root partition UUID
blkid /dev/sda1

# Verify fstab has correct UUID
sudo cat /mnt/etc/fstab

# Regenerate initramfs
sudo chroot /mnt update-initramfs -u
```
