---
title: "GRUB Installed to Wrong Drive"
description: "GRUB boot code written to incorrect disk device"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# GRUB Installed to Wrong Drive

GRUB boot code written to incorrect disk device

## Common Causes

- Multiple disks causing device confusion
- GRUB installed to /dev/sdb instead of /dev/sda
- UEFI boot entry points to wrong disk
- BIOS boot order does not match GRUB installation

## How to Fix

1. Identify correct boot disk: `lsblk`
2. Reinstall GRUB to correct disk: `sudo grub-install /dev/sdX`
3. Update BIOS/UEFI boot order
4. For UEFI: reinstall GRUB EFI binary to correct ESP

## Examples

```bash
# Identify disks and partitions
lsblk -f

# Reinstall GRUB to specific disk
sudo grub-install /dev/sda

# For UEFI systems
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi
```
