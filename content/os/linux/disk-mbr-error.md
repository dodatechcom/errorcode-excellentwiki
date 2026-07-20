---
title: "[Solution] Linux: disk-mbr-error — MBR partition table error"
description: "Fix Linux disk-mbr-error errors. MBR partition table error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: MBR Disk Error

The Master Boot Record (MBR) is the first 512 bytes of a disk containing boot code and partition entries. MBR errors cause boot failures with messages like "Missing operating system" or drops to a "grub rescue>" prompt.

## Common Causes

- MBR overwritten by installing another OS bootloader (Windows, etc.)
- Bad sectors on the first sector of the disk damaging the MBR
- Partition table entries accidentally deleted with dd, fdisk, or parted
- Improper shutdown causing incomplete writes to the boot sector
- Disk exceeds 2TB limit with MBR instead of GPT

## How to Fix

### 1. Boot from Live Media

Boot from a Linux live USB/DVD to access the system and repair the MBR.

### 2. Backup Current MBR

```bash
sudo dd if=/dev/sda of=/tmp/mbr_backup.bin bs=512 count=1
sudo dd if=/dev/sda of=/tmp/ptable.bin bs=1 skip=446 count=64
```

### 3. Reinstall GRUB

```bash
# For BIOS/legacy boot
sudo mount /dev/sda1 /mnt
sudo grub-install --root-directory=/mnt /dev/sda

# For UEFI
sudo mount /dev/sda2 /mnt/boot/efi
sudo grub-install --target=x86_64-efi --efi-directory=/mnt/boot/efi --boot-directory=/mnt/boot
```

### 4. Repair Partition Table with TestDisk

```bash
sudo testdisk /dev/sda
# Select: [Intel/PC Partition] -> [Analyse] -> [Quick Search]
```

### 5. Restore from Backup

```bash
sudo dd if=/tmp/mbr_backup.bin of=/dev/sda bs=512 count=1
```

## Examples

```bash
$ sudo fdisk -l /dev/sda
Disk /dev/sda: 500 GB, 500107862016 bytes
Invalid partition table - signature 0x0000

$ sudo grub-install --root-directory=/mnt /dev/sda
Installing for i386-pc platform.
Installation finished. No error reported.
```
