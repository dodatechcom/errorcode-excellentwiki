---
title: "[Solution] Linux GRUB 'unknown filesystem' — Boot Rescue Fix"
description: "Fix Linux GRUB 'unknown filesystem' and GRUB rescue errors. Reinstall GRUB, fix boot configuration, and recover unbootable systems."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
tags: ["grub", "unknown-filesystem", "rescue", "boot", "grub-install"]
weight: 5
---

# Linux: GRUB rescue - unknown filesystem

The `GRUB rescue: unknown filesystem` error means the GRUB bootloader cannot find or read the filesystem containing the Linux kernel. This typically happens after a Windows update overwrites the bootloader, a disk partition was resized or moved, the GRUB configuration was corrupted, or the boot partition was damaged. The system drops to a minimal GRUB shell and cannot boot.

## Common Causes

- Windows update overwrote GRUB MBR
- Partition table changed (resize, move, new OS install)
- GRUB configuration file (`grub.cfg`) corrupted
- Boot partition (`/boot`) formatted to an unsupported filesystem
- UEFI boot entry removed or corrupted
- Filesystem corruption on the boot partition

## How to Fix

### 1. Identify Available Partitions in GRUB Rescue

```bash
# In the GRUB rescue shell, list available partitions
grub> ls

# Check each partition for a Linux filesystem
grub> ls (hd0,msdos1)/
grub> ls (hd0,msdos2)/

# Look for /boot/grub or /boot/vmlinuz
grub> ls (hd0,msdos2)/boot/grub
```

### 2. Manually Boot from GRUB Rescue

If you can find the correct partition:

```bash
# Set the root partition
grub> set root=(hd0,msdos2)

# Set the prefix (where GRUB config is)
grub> set prefix=(hd0,msdos2)/boot/grub

# Load the normal module
grub> insmod normal

# Boot normally
grub> normal
```

### 3. Boot from Live USB and Reinstall GRUB

```bash
# Boot from a live USB, then:
sudo mount /dev/sda2 /mnt        # Root partition
sudo mount /dev/sda1 /mnt/boot   # Boot partition (if separate)

# For UEFI systems
sudo mount /dev/sda1 /mnt/boot/efi

# Chroot into the installed system
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

### 4. Fix GRUB Configuration

```bash
# After chrooting into the system:
grub-mkconfig -o /boot/grub/grub.cfg

# Or for older systems:
update-grub
```

### 5. Fix EFI Boot Entries (UEFI Systems)

```bash
# Check current boot entries
efibootmgr -v

# Add GRUB back to boot entries
sudo efibootmgr -c -d /dev/sda -p 1 -l \\EFI\\ubuntu\\grubx64.efi -L "Ubuntu"

# Set GRUB as the default boot entry
sudo efibootmgr -n XXXX   # Set boot number
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

### 7. Use Boot-Repair (Easiest Method)

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
(hd0) (hd0,msdos2) (hd0,msdos1)

grub> ls (hd0,msdos2)/
error: unknown filesystem

grub> ls (hd0,msdos1)/
boot/  grub/  vmlinuz  initrd.img

grub> set root=(hd0,msdos1)
grub> insmod normal
grub> normal
# System boots into GRUB menu
```

## Related Errors

- [Kernel panic]({{< relref "/os/linux/kernel-panic2" >}}) — System crash after successful boot
- [Disk I/O error]({{< relref "/os/linux/disk-full2" >}}) — Hardware failure preventing boot
- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — Boot partition corruption
