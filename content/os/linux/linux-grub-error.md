---
title: "[Solution] Linux GRUB Error — No Such Partition Boot Fix"
description: "Fix Linux GRUB 'error: no such partition' and boot errors. Reinstall GRUB, fix partition references, and recover unbootable systems."
platforms: ["linux"]
severities: ["critical"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: GRUB: error no such partition

The `GRUB: error: no such partition` error means the GRUB bootloader cannot find the partition it was configured to boot from. The GRUB configuration references a partition (e.g., `(hd0,msdos2)`) that no longer exists or has a different identifier. This typically happens after disk operations, partition table changes, or incorrect GRUB configuration.

## What This Error Means

GRUB stores references to partitions by disk and partition number. When you see "no such partition," GRUB has tried to load its configuration or kernel from a partition that doesn't exist at the expected location. The system will drop to a rescue shell or fail to boot entirely.

## Common Causes

- Partition table modified (resize, delete, create new partition)
- Disk order changed in BIOS/UEFI
- GRUB configuration references wrong partition UUID or number
- Dual-boot installation altered partition layout
- Disk controller mode changed (AHCI vs RAID vs IDE)
- GPT/MBR mismatch after conversion

## How to Fix

### 1. Identify Available Partitions

```bash
# In GRUB rescue shell, list partitions
grub> ls

# Check each partition for Linux filesystem
grub> ls (hd0,msdos1)/
grub> ls (hd0,msdos2)/

# Look for /boot/grub directory
grub> ls (hd0,msdos2)/boot/grub
```

### 2. Manually Boot from GRUB Rescue

```bash
# Set the correct root partition
grub> set root=(hd0,msdos2)

# Set the prefix
grub> set prefix=(hd0,msdos2)/boot/grub

# Load the normal module
grub> insmod normal
grub> normal
```

### 3. Boot from Live USB and Reinstall GRUB

```bash
# Boot from a live USB, then:
sudo mount /dev/sda2 /mnt        # Root partition
sudo mount /dev/sda1 /mnt/boot   # Boot partition (if separate)

# For UEFI systems
sudo mount /dev/sda1 /mnt/boot/efi

# Bind system directories
sudo mount --bind /dev /mnt/dev
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
sudo mount --bind /sys/firmware/efi/efivars /mnt/sys/firmware/efi/efivars
sudo chroot /mnt

# Reinstall GRUB
grub-install /dev/sda              # BIOS
grub-install --target=x86_64-efi --efi-directory=/boot/efi  # UEFI

# Update GRUB configuration
update-grub
```

### 4. Fix GRUB Configuration File

```bash
# After chrooting:
# Check grub.cfg for incorrect partition references
grep 'set root=' /boot/grub/grub.cfg

# Regenerate GRUB configuration
grub-mkconfig -o /boot/grub/grub.cfg
update-grub
```

### 5. Fix UEFI Boot Entries

```bash
# Check current boot entries
efibootmgr -v

# Create new GRUB entry if missing
sudo efibootmgr -c -d /dev/sda -p 1 -l \\EFI\\ubuntu\\grubx64.efi -L "Ubuntu"

# Set boot order
sudo efibootmgr -o 0000,0001
```

### 6. Fix Corrupted /boot Partition

```bash
# From a live USB:
sudo fsck -f /dev/sda1    # The boot partition

# Verify kernel images exist
ls /mnt/boot/vmlinuz*
ls /mnt/boot/initrd*

# If missing, reinstall the kernel
sudo chroot /mnt
apt install --reinstall linux-image-$(uname -r)
update-grub
```

### 7. Use Boot-Repair Tool

```bash
# Boot from a live USB with internet access
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt update
sudo apt install boot-repair
boot-repair

# Click "Recommended Repair" to automatically fix GRUB
```

## Examples

```
GRUB rescue> ls
(hd0) (hd0,msdos3) (hd0,msdos2) (hd0,msdos1)

error: no such partition
GRUB rescue> ls (hd0,msdos2)/
error: unknown filesystem

GRUB rescue> ls (hd0,msdos1)/
boot/  grub/  vmlinuz  initrd.img

GRUB rescue> set root=(hd0,msdos1)
GRUB rescue> insmod normal
GRUB rescue> normal
# GRUB menu appears
```

## Related Errors

- [GRUB rescue mode]({{< relref "/os/linux/linux-grub-rescue" >}}) — GRUB minimal shell recovery
- [Kernel panic]({{< relref "/os/linux/kernel-panic2" >}}) — Kernel boot failures
- [/etc/fstab mount failed]({{< relref "/os/linux/linux-fstab-error" >}}) — Filesystem mount issues
- [initramfs error]({{< relref "/os/linux/linux-initramfs-error" >}}) — Initramfs issues
