---
title: "[Solution] macOS Time Machine Backup Failed — Error Fix"
description: "Fix macOS Time Machine backup failed errors. Resolve 'backup disk not available,' 'unable to backup,' and 'sparsebundle' errors on Mac."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# Time Machine Backup Failed

A Time Machine backup error occurs when macOS cannot complete a backup to the designated backup disk. Common errors include "Backup disk not available," "Unable to backup," "The backup disk image could not be mounted," and sparsebundle corruption errors.

## Description

Time Machine creates incremental backups using sparse disk images (for network drives) or APFS/HFS+ snapshots (for local drives). Errors occur at any stage of this process.

Common error messages:

- `Time Machine couldn't back up to "BackupDisk".`
- `The backup disk image could not be mounted.`
- `The backup is older than the contents of your computer.`
- `An error occurred while copying files to the backup disk.`
- `Sparsebundle is corrupted or incomplete.`

## Common Causes

- Backup disk is disconnected, full, or has file system errors
- Network backup destination is unreliable (NAS, shared drive)
- Sparsebundle image is corrupted from interrupted backup
- macOS upgrade changed the backup format
- Backup disk permissions don't match the Mac

## How to Fix Time Machine Errors

### 1. Check Backup Disk Status

```bash
# List available backup destinations
tmutil destinationinfo

# Check if the disk is mounted
diskutil list | grep -A5 "BackupDisk"

# Verify disk has space
df -h /Volumes/BackupDisk
```

### 2. Verify and Repair Backup Disk

```bash
# From Disk Utility or terminal
diskutil verifyVolume /Volumes/BackupDisk
diskutil repairVolume /Volumes/BackupDisk

# If the disk is an APFS volume
diskutil apfs verifyVolume disk2s1
```

### 3. Delete Old Backups and Start Fresh

```bash
# Stop Time Machine
tmutil stopbackup

# Delete old backups (THIS ERASES ALL BACKUP HISTORY)
sudo tmutil delete /Volumes/BackupDisk/Backups.backupdb

# Start a new backup
tmutil startbackup
```

### 4. Fix Sparsebundle Corruption (Network Backup)

```bash
# Mount the sparsebundle
hdiutil attach /Volumes/NetworkDrive/MyMac.sparsebundle

# Verify the image
hdiutil verify /Volumes/NetworkDrive/MyMac.sparsebundle

# If corrupted, try to repair
hdiutil repair /Volumes/NetworkDrive/MyMac.sparsebundle
```

### 5. Reset Time Machine

```bash
# Stop current backup
tmutil stopbackup

# Remove old backup destination
tmutil removedestination <destination-id>

# Add the destination again
tmutil setdestination -a /Volumes/BackupDisk

# Start a new initial backup
tmutil startbackup --block
```

### 6. Fix Exclusive Access Error

```bash
# If another process is using the backup disk
lsof | grep BackupDisk

# Kill processes holding the disk
lsof -t /Volumes/BackupDisk | xargs kill

# Restart Time Machine
tmutil startbackup
```

## Examples

This error commonly occurs when:

- A network backup (NAS) loses connection during an incremental backup
- The backup disk runs out of space and Time Machine can't prune old backups
- After a macOS upgrade, the backup format is incompatible
- An interrupted backup leaves a corrupted sparsebundle

## Related Errors

- [Disk Utility Error](disk-utility-error) — disk corruption preventing backups
- [iCloud Error](icloud-error) — Time Machine backs up iCloud Drive data too
- [Kernel Panic](kernel-panic) — system crashes during backup may corrupt the sparsebundle
