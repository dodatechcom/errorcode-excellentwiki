---
title: "[Solution] Linux: disk-device-not-found — disk device not found error"
description: "Fix Linux disk-device-not-found errors. disk device not found error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["disk"]
weight: 10
---
# Linux: Disk Device Not Found

A device not found error means the kernel cannot detect a storage device, preventing all access to it.

## Common Causes

- Drive not powered on or not connected properly
- SATA/SAS cable loose, damaged, or disconnected
- Faulty power supply cable not providing power
- USB storage device not detected (driver or port issue)
- Drive completely failed and not responding to bus

## How to Fix

### 1. Check Physical Connections

Verify power and data cables are properly seated.

### 2. Rescan SCSI/SATA Buses

```bash
echo "- - -" | sudo tee /sys/class/scsi_host/host*/scan
```

### 3. Check Kernel Detection

```bash
dmesg | grep -iE "ata|sata|usb|nvme|sd[a-z]" | tail -30
```

### 4. Check Hardware Listing

```bash
sudo lshw -class disk
lspci | grep -iE "sata|nvme|usb|sas"
```

## Examples

```bash
$ sudo lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 238.5G  0 disk
├─sda1   8:1    0   512M  0 part /boot/efi
└─sda2   8:2    0 238.0G  0 part /
# Second drive (sdb) is missing

$ echo "- - -" | sudo tee /sys/class/scsi_host/host2/scan
$ sudo lsblk
# sdb now appears
```
