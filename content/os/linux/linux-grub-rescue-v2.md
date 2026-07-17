---
title: "[Solution] Linux GRUB Rescue — unknown filesystem"
description: "Fix Linux GRUB rescue 'error: unknown filesystem' errors. Recover boot from GRUB rescue when the filesystem cannot be identified."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
weight: 5
---

# Linux: GRUB rescue — unknown filesystem

The `error: unknown filesystem` error in GRUB rescue means GRUB cannot identify the filesystem type on the partition it is trying to read. This typically happens when GRUB's filesystem modules are missing, the partition table is corrupted, or GRUB was installed for a different disk layout.

## What This Error Means

GRUB relies on filesystem modules (`ext2.mod`, `xfs.mod`, etc.) to read the boot partition and load the kernel. When GRUB enters rescue mode and reports `unknown filesystem`, it means the embedded core image (`core.img`) does not contain the correct filesystem module for the partition, or the filesystem itself has been damaged.

## Common Causes

- GRUB installed with wrong filesystem modules (e.g., missing ext4 or xfs module)
- Partition table changed after GRUB installation (GPT vs MBR mismatch)
- Filesystem converted or reformatted (e.g., ext3 to ext4 without GRUB update)
- Disk reordered by BIOS/UEFI, changing partition references
- Corrupted GRUB core image
- Btrfs or LVM partition without proper GRUB support modules

## How to Fix

### 1. Identify Available Partitions

```bash
grub rescue> ls

# Try each partition to find one with a readable filesystem
grub rescue> ls (hd0,msdos1)/
grub rescue> ls (hd0,msdos2)/

# For GPT:
grub rescue> ls (hd0,gpt1)/
```

### 2. Load the Correct Filesystem Module

```bash
# If partition is ext2/3/4:
grub rescue> insmod ext2

# If partition is xfs:
grub rescue> insmod xfs

# If partition is btrfs:
grub rescue> insmod btrfs

# Then try listing the partition again
grub rescue> ls (hd0,msdos2)/
```

### 3. Set Root and Boot Manually

```bash
# After finding the correct partition:
grub rescue> set root=(hd0,msdos2)
grub rescue> set prefix=(hd0,msdos2)/boot/grub

# Load normal module
grub rescue> insmod normal
grub rescue> normal
```

### 4. Reinstall GRUB from Live USB

```bash
# Boot from a live USB/CD
sudo mount /dev/sda2 /mnt
sudo mount /dev/sda1 /mnt/boot

# For UEFI systems
sudo mount /dev/sda1 /mnt/boot/efi

# Bind system directories
sudo mount --bind /dev /mnt/dev
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
sudo mount --bind /sys/firmware/efi/efivars /mnt/sys/firmware/efi/efivars

# Chroot into the system
sudo chroot /mnt

# Reinstall GRUB
grub-install /dev/sda
update-grub

# For UEFI
grub-install --target=x86_64-efi --efi-directory=/boot/efi
update-grub
```

### 5. Fix GRUB Core Image

```bash
# From live USB chroot
sudo chroot /mnt

# Regenerate GRUB configuration
grub-mkimage -O x86_64-efi -o /boot/efi/EFI/ubuntu/grubx64.efi \
  -p /boot/grub \
  ext2 normal part_msdos part_gpt biosdisk

# Or use grub-install which rebuilds core.img automatically
grub-install --target=x86_64-efi --efi-directory=/boot/efi --recheck
```

### 6. Check and Repair Filesystem

```bash
# From live USB, check filesystem integrity
sudo fsck /dev/sda2
sudo fsck -y /dev/sda1

# If filesystem is severely damaged
sudo e2fsck -f /dev/sda2    # For ext2/3/4
sudo xfs_repair /dev/sda2   # For XFS
```

## Examples

```bash
grub rescue> ls
(hd0) (hd0,msdos2) (hd0,msdos1)

grub rescue> ls (hd0,msdos2)/
error: unknown filesystem.

grub rescue> insmod ext2
grub rescue> ls (hd0,msdos2)/
lost+found/ boot/ etc/ home/ ...

grub rescue> set root=(hd0,msdos2)
grub rescue> set prefix=(hd0,msdos2)/boot/grub
grub rescue> insmod normal
grub rescue> normal
# Full GRUB menu loads
```

## Related Errors

- [GRUB error]({{< relref "/os/linux/grub-error" >}}) — General GRUB errors
- [GRUB rescue minimal]({{< relref "/os/linux/linux-grub-rescue" >}}) — GRUB minimal shell
- [Kernel panic]({{< relref "/os/linux/linux-kernel-panic" >}}) — Kernel boot failures
