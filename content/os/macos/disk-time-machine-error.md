---
title: "[Solution] macOS Disk Time Machine Error — Backup Disk Format Corrupted"
description: "Fix macOS Time Machine disk error: backup disk not readable, Time Machine disk format corrupted, cannot mount backup volume."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 144
---

# Disk Time Machine Error — Backup Disk Format Corrupted

Fix macOS Time Machine disk error: backup disk not readable, Time Machine disk format corrupted, cannot mount backup volume.

## Common Causes

- Time Machine disk corruption from improper ejection
- File system errors on the backup disk
- Time Machine backup database corruption
- Disk hardware failure affecting backup data

## How to Fix

### 1. Check Time Machine Disk Status

```bash
diskutil list | grep -A 5 'Time Machine'
tmutil listbackups | head -5
```

### 2. Repair Time Machine Disk

```bash
# Recovery → Disk Utility → Select backup disk → First Aid
diskutil verifyVolume /Volumes/TimeMachine
```

### 3. Delete Corrupted Time Machine Backup

```bash
tmutil delete /Volumes/TimeMachine/Backups.backupdb/YYYY-MM-DD-HHMMSS
```

### 4. Reset Time Machine and Start Fresh

```bash
tmutil removedestination /Volumes/TimeMachine*
# Re-add backup disk in System Settings → Time Machine
```

## Common Scenarios

This error commonly occurs when:

- Time Machine shows 'Backup disk not readable' error
- Cannot mount Time Machine backup disk in Finder
- Time Machine backup database appears corrupted
- Backup disk works but Time Machine cannot write new backups

## Prevent It

- Always eject Time Machine disk properly before disconnecting
- Run Disk Utility First Aid on backup disk monthly
- Keep Time Machine backup disk health checked with SMART
- Replace aging backup disks before they fail completely
