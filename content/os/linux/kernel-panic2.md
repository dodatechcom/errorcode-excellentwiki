---
title: "[Solution] Linux Kernel Panic — Not Syncing Fix"
description: "Fix Linux 'Kernel panic - not syncing' errors. Diagnose boot failures, driver issues, and corrupted kernels with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
weight: 5
---

# Linux: Kernel panic - not syncing

A `Kernel panic - not syncing` is a fatal, unrecoverable error in the Linux kernel. When the kernel encounters a critical error from which it cannot safely continue (such as a corrupted filesystem, missing root filesystem, driver bug, or hardware failure), it halts all operations and displays this message. The system must be rebooted, and the underlying cause must be fixed to prevent recurrence.

## Common Causes

- Corrupted root filesystem or missing initramfs
- Incompatible or buggy kernel module (driver)
- Failed kernel update or corrupted kernel image
- Hardware failure (bad RAM, failing disk)
- Bootloader misconfiguration (wrong kernel or root device)
- Filesystem corruption from power loss

## How to Fix

### 1. Boot with a Previous Kernel

If the panic started after a kernel update, boot into the previous version:

```bash
# At GRUB menu, select "Advanced options for Ubuntu"
# Choose a previous kernel version

# Or from a live USB, chroot and reinstall
sudo mount /dev/sda1 /mnt
sudo mount --bind /dev /mnt/dev
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
sudo chroot /mnt

# Reinstall the kernel
apt reinstall linux-image-$(uname -r)
update-grub
exit
```

### 2. Boot into Recovery Mode

```bash
# At GRUB menu, select "Advanced options" → "recovery mode"
# From the recovery menu:
# 1. Try "fsck" to check filesystem
# 2. Try "root" to get a root shell
# 3. Try "clean" to free disk space
```

### 3. Check Filesystem from Live USB

```bash
# Boot from a live USB, then:
sudo fsck -f /dev/sda1
sudo e2fsck -f -y /dev/sda1   # For ext4
```

### 4. Check Kernel Messages from Previous Boot

If you can boot at all, check what caused the panic:

```bash
# Check last kernel messages
sudo journalctl -b -1 -k

# Or check the kernel log
dmesg | grep -i "panic\|oops\|bug\|error"
```

### 5. Disable Faulty Kernel Module

If a specific module is causing the panic:

```bash
# At boot, pass init=/bin/sh to get a shell
# Then blacklist the module
echo "blacklist faulty_module" >> /etc/modprobe.d/blacklist.conf

# Or pass module=off at the GRUB boot line
```

Edit GRUB to add boot parameters:

```bash
sudo nano /etc/default/grub
# Add to GRUB_CMDLINE_LINUX: "modprobe.blacklist=faulty_module"
sudo update-grub
```

### 6. Rebuild initramfs

A corrupted initramfs can cause boot-time panics:

```bash
# From a live USB chroot:
sudo chroot /mnt
update-initramfs -u -k all
update-grub
```

### 7. Test Hardware

```bash
# Test memory
sudo memtester 1G 1

# Check disk health
sudo smartctl -H /dev/sda
sudo smartctl -A /dev/sda

# Check dmesg for hardware errors (when system boots)
dmesg | grep -iE 'error|fault|bug|hardware'
```

### 8. Reinstall the Kernel

```bash
# From a live USB chroot:
sudo chroot /mnt
apt install --reinstall linux-image-$(uname -r)
update-grub
```

## Examples

```
Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)
```

This means the kernel cannot find the root filesystem — check GRUB configuration and disk partitions.

```
Kernel panic - not syncing: Attempted to kill init!
```

This means the init process (PID 1) crashed — the initramfs or root filesystem may be corrupted.

## Related Errors

- [Disk I/O error]({{< relref "/os/linux/disk-full2" >}}) — Hardware-level disk failure
- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — Filesystem corruption fallback
- [GRUB errors]({{< relref "/os/linux/grub-error" >}}) — Bootloader problems
