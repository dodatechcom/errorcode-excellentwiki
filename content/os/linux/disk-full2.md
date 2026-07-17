---
title: "[Solution] Linux Disk I/O Error — Fix Hardware and Filesystem Issues"
description: "Fix Linux 'disk I/O error' messages. Diagnose failing hard drives, filesystem corruption, and bad sectors with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
weight: 5
---

# Linux: Disk I/O Error

A `disk I/O error` indicates a problem communicating with a storage device. This can mean a failing hard drive, bad sectors, loose cables, filesystem corruption, or the kernel having trouble reading/writing to the disk. This is a critical error because data loss or further hardware degradation may occur if the underlying disk is failing.

## Common Causes

- Failing or degraded hard drive / SSD
- Bad sectors on the disk
- Loose or faulty SATA/NVMe cables
- Filesystem corruption from power loss or improper shutdown
- Disk reaching end of life (SMART warnings)

## How to Fix

### 1. Check System Logs

Review kernel messages for disk-related errors:

```bash
dmesg | grep -iE 'error|i/o|disk|ata|scsi|nvme'
```

Look for lines mentioning `I/O error`, `reset`, `timeout`, or `bad sector`.

### 2. Check SMART Health

Use `smartctl` to inspect the disk's health status:

```bash
# Install smartmontools if needed
sudo apt install smartmontools    # Debian/Ubuntu
sudo dnf install smartmontools    # RHEL/CentOS/Fedora

# Check overall health
sudo smartctl -H /dev/sda

# Full SMART attributes
sudo smartctl -A /dev/sda

# Run a short self-test
sudo smartctl -t short /dev/sda

# View test results
sudo smartctl -l selftest /dev/sda
```

If `SMART overall-health` shows `FAILED`, the disk is failing and should be replaced immediately.

### 3. Check and Repair Filesystem

Run `fsck` on unmounted partitions. **Never run fsck on a mounted filesystem.**

```bash
# Check filesystem status
sudo tune2fs -l /dev/sda1 | grep "Filesystem state"

# For root filesystem, boot from a live USB or use:
sudo fsck -f /dev/sda1

# For non-root filesystems, unmount first
sudo umount /dev/sdb1
sudo fsck -f /dev/sdb1
```

### 4. Check Cables and Connections

For physical servers or desktops:

```bash
# Check if the disk is detected by the system
lsblk
sudo hdparm -I /dev/sda | grep -i model

# Test read speed (a failing disk will show errors or very low speeds)
sudo hdparm -t /dev/sda
```

### 5. Monitor Disk Health Over Time

Set up ongoing SMART monitoring:

```bash
# Enable SMART on the disk
sudo smartctl -s on /dev/sda

# Run a long self-test
sudo smartctl -t long /dev/sda

# Check results after test completes
sudo smartctl -l selftest /dev/sda
```

### 6. Replace the Disk if Necessary

If SMART reports failures or `dmesg` shows repeated I/O errors:

```bash
# Clone the failing disk to a new one (if still readable)
sudo dd if=/dev/sda of=/dev/sdb bs=4M status=progress

# Or use rsync for file-level backup
sudo rsync -avhP --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*"} / /mnt/backup/
```

## Examples

```bash
$ dmesg | grep -i "i/o error"
[  123.456789] ata1.00: status: { DRDY ERR }
[  123.456790] ata1.00: error: { UNC }
[  123.456791] ata1.00: failed command: READ FPDMA QUEUED

$ sudo smartctl -H /dev/sda
=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: FAILED!
```

## Related Errors

- [No space left on device]({{< relref "/os/linux/no-space-left" >}}) — Disk full
- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — Filesystem remounted read-only after errors
- [Kernel panic]({{< relref "/os/linux/kernel-panic2" >}}) — System crash due to critical failure
