---
title: "[Solution] macOS Time Machine Error — Backup Failure"
description: "Fix macOS Time Machine backup failure: backups not completing, Time Machine shows error icon, backup disk not recognized."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 113
---

# Time Machine Error — Backup Failure

Fix macOS Time Machine backup failure: backups not completing, Time Machine shows error icon, backup disk not recognized.

## Common Causes

- Backup disk has insufficient free space for new backups
- Corrupted Time Machine snapshot or backup database
- Network connection issue for wireless Time Machine backup
- FileVault encryption preventing Time Machine access

## How to Fix

### 1. Check Time Machine Status and Logs

```bash
tmutil status
tmutil listbackups | tail -10
log show --predicate 'process == "backupd"' --last 1h | grep -i error | head -20
```

### 2. Fix Backup Disk Issues

```bash
df -h /Volumes/TimeMachine*
tmutil delete /Volumes/TimeMachine/Backups.backupdb/YYYY-MM-DD-HHMMSS
```

### 3. Delete Corrupted Local Snapshots

```bash
tmutil listlocalsnapshots /
tmutil deletelocalsnapshots /
tmutil startbackup
```

### 4. Reset Time Machine and Start Fresh

```bash
tmutil removedestination /Volumes/TimeMachine*
defaults delete com.apple.TimeMachine
# Re-add backup disk in System Settings → Time Machine
```

## Common Scenarios

This error commonly occurs when:

- Time Machine shows 'Backup Not Complete' error in menu bar
- Backup stalls at same percentage for hours without progressing
- Time Machine cannot find backup disk that is clearly connected
- Local snapshots consume excessive disk space without completing

## Prevent It

- Keep backup disk at least 20% free to accommodate growing backups
- Monitor Time Machine status regularly via menu bar icon
- Use a dedicated drive for Time Machine rather than shared storage
- Run Time Machine verification periodically with tmutil verifychecksums
