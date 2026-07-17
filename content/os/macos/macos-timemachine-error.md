---
title: "[Solution] macOS Time Machine Backup Error"
description: "Fix Time Machine backup errors on Mac including 'backup not complete,' 'disk not available,' and backup verification failures."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["time-machine", "backup", "disk", "restore", "snapshot"]
weight: 5
---

# macOS Time Machine Backup Error Fix

Time Machine errors include backups failing to start, "Backup disk not available," incomplete backups, or "Unable to backup" messages. Time Machine is macOS's built-in backup solution.

## What This Error Means

Time Machine creates hourly snapshots and full backups to a designated disk. Failures occur when the backup disk is disconnected, the disk image is corrupt, or the backup database is damaged.

## Common Causes

- Backup disk disconnected or powered off during backup
- Backup disk full or running low on space
- Corrupt Time Machine backup database
- Network backup destination unreachable (NAS/network drive)
- File system corruption on backup disk
- macOS update changing Time Machine behavior

## How to Fix

### 1. Check backup disk status

```bash
# List connected disks
diskutil list

# Check if backup disk is mounted
ls /Volumes/

# Verify Time Machine backup disk
tmutil listbackups
```

### 2. Delete corrupt local snapshots

```bash
# List local snapshots
tmutil listlocalsnapshots /

# Delete specific snapshot
tmutil deletelocalsnapshots <date>

# Delete all local snapshots
for snapshot in $(tmutil listlocalsnapshots / | awk -F'.' '{print $NF}'); do
    tmutil deletelocalsnapshots $snapshot
done
```

### 3. Verify and repair the backup disk

```bash
# Verify the backup disk
diskutil verifyVolume /Volumes/BackupDisk

# Repair if needed
diskutil repairVolume /Volumes/BackupDisk
```

### 4. Reset Time Machine

```bash
# Stop Time Machine
tmutil disable

# Delete the backup database (CAUTION: this erases all backups)
sudo rm -rf /Volumes/BackupDisk/Backups.backupdb

# Re-enable and start fresh
tmutil enable
tmutil startbackup
```

## Related Errors

- [Disk Utility Error](disk-utility-error) — disk repair and verification errors
- [iCloud Error](macos-icloud-error) — cloud backup alternative issues
- [Finder Error](finder-error) — file system errors affecting backups
