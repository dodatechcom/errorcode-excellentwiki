---
title: "[Solution] macOS iCloud Drive Error — Files Not Syncing"
description: "Fix macOS iCloud Drive error: files not syncing between devices, iCloud Drive folder empty or shows pending sync, documents stuck."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 116
---

# iCloud Drive Error — Files Not Syncing

Fix macOS iCloud Drive error: files not syncing between devices, iCloud Drive folder empty or shows pending sync, documents stuck.

## Common Causes

- iCloud Drive sync daemon (bird) stopped or crashed
- Network connection issues preventing cloud upload/download
- File conflict between multiple editing devices
- iCloud Drive folder permissions or quarantine issue

## How to Fix

### 1. Check iCloud Drive Sync Status

```bash
brctl status
brctl log --wait --shorten
ls -la ~/Library/Mobile\ Documents/com~apple~CloudDocs/
```

### 2. Restart iCloud Sync Daemon

```bash
killall bird
# Daemon will restart automatically and resume syncing
```

### 3. Rebuild iCloud Drive Local Cache

```bash
rm -rf ~/Library/Mobile\ Documents/com~apple~CloudDocs/.
rm -rf ~/Library/Caches/CloudKit/*
# Disable and re-enable iCloud Drive in System Settings
```

### 4. Fix File Conflicts and Permissions

```bash
find ~/Library/Mobile\ Documents/ -name '*conflict*' 2>/dev/null
# Resolve conflicts by choosing correct version
```

## Common Scenarios

This error commonly occurs when:

- iCloud Drive Desktop folder is empty on one Mac but full on another
- New files added to iCloud Drive show spinning sync indicator indefinitely
- Documents edited on iPhone do not appear on Mac iCloud Drive
- iCloud Drive shows 'Uploading' status for files that never complete

## Prevent It

- Ensure stable internet connection when syncing large files to iCloud Drive
- Avoid editing the same file simultaneously on multiple devices
- Monitor iCloud Drive sync status with 'brctl status' when issues arise
- Keep macOS updated for iCloud Drive improvements
