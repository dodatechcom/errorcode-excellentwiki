---
title: "[Solution] Linux EIO (errno 5) — Input/Output Error Fix"
description: "Fix Linux EIO (errno 5) Input/Output Error. Diagnose disk failures, filesystem corruption, and hardware issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
tags: ["eio", "errno-5", "io-error", "disk", "filesystem"]
weight: 50
---

# Linux EIO (errno 5) — Input/Output Error

EIO (errno 5) is a low-level error indicating that the kernel encountered an input/output failure during a system call. This typically means the storage hardware, device driver, or filesystem layer failed to read from or write to a storage device. Unlike higher-level errors, EIO often signals a serious hardware or deep filesystem problem that requires immediate attention.

## Common Causes

- Failing or dead hard drive or SSD
- Corrupted filesystem
- Faulty or loose SATA/NVMe cable
- Bad sectors on the disk
- USB drive failure or disconnection during I/O
- RAID array degradation
- NFS server unreachable
- Device driver bugs

## How to Fix EIO

### 1. Check Kernel Ring Buffer for Errors

The kernel log often reveals the root cause before you see EIO:

```bash
# Check kernel messages for disk and I/O errors
dmesg | grep -iE "error|fail|i/o|ata|scsi|nvme|usb"

# Check for specific disk errors
dmesg | grep -i "sda\|sdb\|nvme0"
```

Look for patterns like:

- `ata1.00: failed command: READ FPDMA QUEUED`
- `Buffer I/O error on dev sda1`
- `blk_update_request: I/O error`
- `USB disconnect` (for USB drives)

### 2. Check Disk Health with smartctl

S.M.A.R.T. data reveals the physical health of your drive:

```bash
# Install smartmontools if not present
sudo apt install smartmontools    # Debian/Ubuntu
sudo dnf install smartmontools    # RHEL/Fedora

# Check S.M.A.R.T. status for the entire disk
sudo smartctl -a /dev/sda

# Check only the health attributes
sudo smartctl -H /dev/sda

# For NVMe drives
sudo smartctl -a /dev/nvme0n1
```

Critical attributes to watch:

| Attribute | What It Means |
|-----------|---------------|
| Reallocated_Sector_Ct | Bad sectors remapped — high values mean failing disk |
| Current_Pending_Sector | Sectors waiting to be remapped |
| Offline_Uncorrectable | Sectors that cannot be read |
| UDMA_CRC_Error_Count | Cable or interface errors |

### 3. Test the Disk with dd

Perform a raw read test to verify the disk responds:

```bash
# Read the first 1GB from the disk (non-destructive)
sudo dd if=/dev/sda of=/dev/null bs=1M count=1024 status=progress

# For a specific partition
sudo dd if=/dev/sda1 of=/dev/null bs=1M count=100 status=progress
```

If `dd` fails with I/O errors, the disk or partition is likely failing.

### 4. Run Filesystem Check (fsck)

Filesystem corruption can cause EIO even on healthy hardware:

```bash
# Unmount the filesystem first (cannot check a mounted filesystem)
sudo umount /dev/sda1

# Run filesystem check (ext4)
sudo fsck -f /dev/sda1

# For XFS
sudo xfs_repair /dev/sda1

# For Btrfs
sudo btrfs check /dev/sda1
```

**Important:** Never run `fsck` on a mounted filesystem. Boot from a live USB if the filesystem is your root partition.

### 5. Check Cables and Connections

Physical connection issues are a common but overlooked cause:

- Reseat SATA data and power cables on both the drive and motherboard
- Try a different SATA port on the motherboard
- For NVMe, reseat the drive in its M.2 slot
- For external drives, try a different USB port or cable
- Check for physical damage on connectors

### 6. Verify Filesystem Mount Options

Incorrect mount options can cause I/O errors:

```bash
# Check current mount options
mount | grep " / "

# Check /etc/fstab for errors
cat /etc/fstab
```

Common issues in fstab:

- Referencing a UUID that no longer matches (after disk replacement)
- Filesystem type mismatch
- Missing `nofail` for optional drives

### 7. Check RAID Array Status

If the disk is part of a RAID array:

```bash
# Check Linux software RAID status
cat /proc/mdstat

# Check RAID details
sudo mdadm --detail /dev/md0

# Check for degraded arrays
sudo mdadm --detail --scan
```

### 8. Test with a Different Kernel or Live USB

Rule out driver issues by booting from a live USB:

```bash
# Boot from Ubuntu live USB
# Then check the disk
sudo smartctl -H /dev/sda
sudo fsck -f /dev/sda1
```

If the live environment also shows I/O errors, the problem is hardware.

### 9. Check dmesg After Removable Device Insertion

For USB drives, insert the drive and watch the logs:

```bash
# Clear the kernel ring buffer
sudo dmesg -C

# Insert the USB drive

# Check new messages
dmesg
```

Successful mounting shows device detection. Errors indicate hardware or driver problems.

## Urgent Actions

If EIO occurs on your root filesystem:

1. Back up data immediately to a different device
2. Boot from a live USB to perform diagnostics
3. Replace the disk if S.M.A.R.T. reports failures
4. Consider professional data recovery for critical data

## Related Error Codes

- [ENOSPC (errno 28)](/os/linux/errno-28/) — No space left on device
- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted
