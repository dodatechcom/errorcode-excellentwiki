---
title: "[Solution] macOS Time Machine Error -- Time Machine Backup Failed"
description: "Fix macOS Time Machine error when Time Machine backup fails to complete or cannot connect to backup disk. Resolve Time Machine issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Time Machine Error -- Time Machine Backup Failed

Time Machine is macOS's built-in backup system. When it fails, backups may not complete, the backup disk may not be recognized, or old backups may be corrupted.

## Common Causes
- Backup disk is full and cannot accept new backups
- Network connection to the backup disk is unstable
- Backup disk has errors that need repair
- Time Machine preferences are corrupted
- APFS snapshot limit has been reached

## How to Fix
1. Check available space on the backup disk
2. Verify the network connection to the backup disk (for network backups)
3. Run Disk Utility First Aid on the backup disk
4. Delete old backups to free space
5. Reset Time Machine preferences and start a new backup

```bash
# Check Time Machine backup status
tmutil status

# List existing backups
tmutil listbackups

# Delete old backups to free space
tmutil delete /Volumes/BackupDisk/Backups.backupdb/2023-01-01-120000
```

## Examples

```bash
# Start a new backup manually
tmutil startbackup

# Stop a running backup
tmutil stopbackup
```

This error is common when the backup disk is full, when the network connection to a NAS drops during backup, or when the backup disk has filesystem errors.
