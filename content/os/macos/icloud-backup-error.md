---
title: "[Solution] macOS iCloud Backup Error — Mac Data Not Backing Up"
description: "Fix macOS iCloud backup failure: cannot back up Mac data to iCloud, backup stalls or shows error, iCloud backup not completing."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 118
---

# iCloud Backup Error — Mac Data Not Backing Up

Fix macOS iCloud backup failure: cannot back up Mac data to iCloud, backup stalls or shows error, iCloud backup not completing.

## Common Causes

- iCloud storage full preventing backup from completing
- Slow or intermittent internet connection during backup
- Large backup files causing timeout during upload
- Backup daemon experiencing authentication or permission issue

## How to Fix

### 1. Check iCloud Backup Status

```bash
# System Settings → Apple ID → iCloud
log show --predicate 'process == "bird"' --last 1h | grep -i backup | head -10
```

### 2. Free Up iCloud Storage

```bash
# System Settings → Apple ID → iCloud → Manage Account Storage
# Delete old iCloud backups from other devices
```

### 3. Reduce Backup Size

```bash
du -sh ~/Library/Mobile\ Documents/
# Disable backing up large unnecessary apps
```

### 4. Retry Backup on Stable Connection

```bash
networkquality
# Connect via Ethernet for faster upload
# Disable VPN if active
```

## Common Scenarios

This error commonly occurs when:

- iCloud backup shows 'Waiting to Upload' indefinitely
- Backup fails partway through with 'Backup Failed' message
- iCloud backup for Mac does not appear in storage management
- Backup stalls at same percentage when uploading large photo libraries

## Prevent It

- Maintain sufficient iCloud storage ahead of scheduled backups
- Keep Mac connected to power and internet during backup hours
- Regularly review and delete old device backups from iCloud
- Use 'Optimize Mac Storage' to reduce local file size
