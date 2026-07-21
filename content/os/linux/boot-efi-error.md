---
title: "[Solution] Linux: boot-efi-error -- EFI boot partition error"
description: "Fix Linux EFI boot partition errors. EFI System Partition missing or corrupt."
os: ["linux"]
error-types: ["boot-error"]
severities: ["error"]
---

# Linux: EFI Boot Partition Error

EFI boot partition errors prevent booting in UEFI mode.

## Common Causes

- EFI System Partition not formatted as FAT32
- /boot/efi mount point missing from fstab
- UEFI variables cleared after BIOS update
- GRUB EFI binary not installed to ESP
- Secure Boot key mismatch

## How to Fix

### 1. Check EFI Setup

```bash
ls /sys/firmware/efi
lsblk -o NAME,FSTYPE,MOUNTPOINT | grep -i efi
efibootmgr -v
```

### 2. Mount and Repair ESP

```bash
sudo mkdir -p /boot/efi
sudo mount /dev/sda1 /boot/efi
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi
```

### 3. Add fstab Entry

```bash
UUID=$(blkid -s UUID -o value /dev/sda1)
echo "UUID=$UUID /boot/efi vfat umask=0077 0 1" | sudo tee -a /etc/fstab
```

## Examples

```bash
$ ls /sys/firmware/efi
ls: cannot access /sys/firmware/efi: No such file or directory
$ efibootmgr -v
BootCurrent: 0000
Boot0000* ubuntu  HD(1,GPT,uuid)/EFI/ubuntu/shimx64.efi
```
