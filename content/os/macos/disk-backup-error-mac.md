---
title: "[Solution] macOS Disk Backup Error — External Backup Drive Failure"
description: "Fix macOS backup disk failure: external backup disk not recognized, backup drive fails during backup operation, backup disk crashes."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 145
---

# Disk Backup Error — External Backup Drive Failure

Fix macOS backup disk failure: external backup disk not recognized, backup drive fails during backup operation, backup disk crashes.

## Common Causes

- External backup disk hardware failure
- USB/Thunderbolt connection issue causing backup interruption
- Backup disk file system corruption
- Insufficient disk space on backup drive for new backups

## How to Fix

### 1. Check Backup Disk Health

```bash
diskutil info /Volumes/BackupDrive
diskutil verifyVolume /Volumes/BackupDrive
sudo smartctl -a /dev/disk2
```

### 2. Repair Backup Disk

```bash
# Recovery → Disk Utility → Select backup disk → First Aid
diskutil eraseDisk 'Journaled HFS+' BackupDisk disk2
```

### 3. Free Up Space on Backup Disk

```bash
tmutil delete /Volumes/BackupDrive/Backups.backupdb/YYYY-MM-DD-HHMMSS
df -h /Volumes/BackupDrive
```

### 4. Replace Failing Backup Disk

```bash
tmutil startbackup --auto
# Purchase new backup disk and reconfigure Time Machine
```

## Common Scenarios

This error commonly occurs when:

- External backup disk disconnects during Time Machine backup
- Backup disk not recognized after Mac wakes from sleep
- Time Machine backup fails with 'backup disk not available'
- Backup disk makes unusual noises indicating hardware failure

## Prevent It

- Monitor backup disk SMART status regularly for early failure signs
- Keep backup disk firmware updated if applicable
- Use powered external drives to prevent USB power-related disconnections
- Maintain at least two backup destinations for important data
