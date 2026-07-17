---
title: "[Solution] Time Machine Backup Disk Not Found Error on Mac"
description: "Fix Time Machine errors when backup disk is not found, backup fails to start, or Time Machine cannot connect to backup destination."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
tags: ["time-machine", "backup", "disk", "network", "nas", "macos"]
weight: 5
---

# Time Machine Backup Disk Not Found Error on Mac

Time Machine cannot find or connect to backup disk, shows "Backup disk not available", or fails to start backup.

## What This Error Means

Time Machine backup disk errors occur when macOS cannot locate, mount, or authenticate with the backup destination. This can be due to disk formatting issues, network connectivity problems, or disk corruption.

## Common Causes

- External disk not properly connected
- Disk formatted with incompatible file system
- Network backup destination unreachable
- Disk full or corrupted
- Time Machine preferences corrupted
- APFS/HFS+ formatting mismatch

## How to Fix

### Verify Disk Connection

```bash
# List connected disks
diskutil list

# Check disk mounting
diskutil info <disk-identifier>

# Mount disk if unmounted
diskutil mount <disk-identifier>
```

### Check Disk Format

```bash
# Time Machine requires:
# - HFS+ (Mac OS Extended) for local backups
# - APFS (for newer macOS)
# - SMB network share

# Reformat disk (WARNING: erases all data)
diskutil eraseDisk JHFS+ "BackupDisk" GPTFormat /dev/disk2
```

### Reset Time Machine

```bash
# Remove old Time Machine preferences
defaults delete com.apple.TimeMachine

# Restart Time Machine daemon
sudo tmutil stopbackup
sudo tmutil startbackup
```

### Fix Network Backup

```bash
# Test SMB connection
smbutil statshares -a

# Re-add network backup destination
tmutil setdestination -a smb://user@server/backup
```

### Check Disk Health

```bash
# Check SMART status
diskutil info disk2 | grep SMART

# Verify disk integrity
diskutil verifyVolume disk2s1

# Repair if needed
diskutil repairVolume disk2s1
```

### Create New Backup

```bash
# Delete old backup sparsebundle
sudo tmutil delete /Volumes/BackupDisk/Backup.backupdb

# Start fresh backup
tmutil startbackup
```

## Related Errors

- [SSD Error]({{< relref "/os/macos/macos-ssd-error-v2" >}}) — Storage issues
- [USB Error]({{< relref "/os/macos/macos-usb-error-v2" >}}) — USB connectivity
- [SIP Error]({{< relref "/os/macos/macos-sip-error-v2" >}}) — System protection
