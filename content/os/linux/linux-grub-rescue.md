---
title: "[Solution] Linux GRUB Rescue Mode — Minimal Shell Fix"
description: "Fix Linux GRUB rescue 'error: no such partition' and minimal BASH-like shell errors. Recover boot from the GRUB command line."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
tags: ["grub-rescue", "minimal-shell", "no-such-partition", "boot", "recovery"]
weight: 5
---

# Linux: GRUB rescue — minimal BASH-like shell

`GRUB rescue` is the most basic GRUB shell. It appears when GRUB cannot find its normal configuration files (`grub.cfg`) or the boot partition. The prompt is `grub rescue>` and only a limited set of commands is available.

## Common Causes

- Partition table changed after disk operations
- GRUB configuration file deleted or corrupted
- Boot partition deleted or formatted
- Disk controller mode changed (AHCI vs RAID vs IDE)
- Hard drive disconnected or renumbered
- Dual-boot: Windows overwrote the MBR
- UEFI boot entries corrupted

## How to Fix

### 1. Identify Available Partitions

```bash
grub rescue> ls

# Typical output:
# (hd0) (hd0,msdos3) (hd0,msdos2) (hd0,msdos1)
```

### 2. Find the Boot Partition

```bash
# Probe each partition
grub rescue> ls (hd0,msdos1)/
grub rescue> ls (hd0,msdos2)/

# Look for /boot/grub or /grub directory
grub rescue> ls (hd0,msdos2)/boot/grub
```

### 3. Set Root and Prefix Manually

```bash
# Once you find the partition with /boot/grub:
grub rescue> set root=(hd0,msdos2)
grub rescue> set prefix=(hd0,msdos2)/boot/grub

# Or for /boot on a separate partition:
grub rescue> set root=(hd0,msdos1)
grub rescue> set prefix=(hd0,msdos1)/grub
```

### 4. Load the Normal Module and Boot

```bash
grub rescue> insmod normal
grub rescue> normal
```

This should load the full GRUB menu. If `insmod normal` fails:

```bash
# Try loading Linux kernel directly
grub rescue> insmod linux
grub rescue> linux (hd0,msdos2)/boot/vmlinuz-<version> root=/dev/sda2
grub rescue> initrd (hd0,msdos2)/boot/initrd.img-<version>
grub rescue> boot
```

### 5. Reinstall GRUB from Live USB

```bash
# Boot from a live USB
sudo mount /dev/sda2 /mnt        # Root partition
sudo mount /dev/sda1 /mnt/boot   # Boot partition (if separate)

# For UEFI
sudo mount /dev/sda1 /mnt/boot/efi

# Bind system directories
sudo mount --bind /dev /mnt/dev
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys

# Chroot
sudo chroot /mnt

# Reinstall GRUB
grub-install /dev/sda              # BIOS
grub-install --target=x86_64-efi --efi-directory=/boot/efi  # UEFI

# Update GRUB
update-grub
```

### 6. Fix UEFI Boot Entries

```bash
# Check current boot entries
efibootmgr -v

# Create new GRUB entry
sudo efibootmgr -c -d /dev/sda -p 1 -l \\EFI\\ubuntu\\grubx64.efi -L "Ubuntu"

# Set boot order
sudo efibootmgr -o 0000,0001
```

### 7. Use Boot-Repair Tool

```bash
# From live USB
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt update
sudo apt install boot-repair
boot-repair

# Select "Recommended repair"
```

## Examples

```
grub rescue> ls
(hd0) (hd0,msdos2) (hd0,msdos1)

grub rescue> ls (hd0,msdos1)/
error: unknown filesystem.

grub rescue> ls (hd0,msdos2)/
lost+found/ boot/ etc/ home/ ...

grub rescue> set root=(hd0,msdos2)
grub rescue> set prefix=(hd0,msdos2)/boot/grub
grub rescue> insmod normal
grub rescue> normal
# GRUB menu appears
```

## Related Errors

- [GRUB error]({{< relref "/os/linux/grub-error" >}}) — General GRUB errors
- [Kernel panic]({{< relref "/os/linux/kernel-panic2" >}}) — Kernel boot failures
- [initramfs error]({{< relref "/os/linux/linux-initramfs-error" >}}) — Initramfs issues
