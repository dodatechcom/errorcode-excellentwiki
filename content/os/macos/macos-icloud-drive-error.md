---
title: "[Solution] macOS iCloud Drive Error -- iCloud Drive Files Not Appearing"
description: "Fix macOS iCloud Drive error when files are missing or not downloading from iCloud Drive. Resolve iCloud Drive issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS iCloud Drive Error -- iCloud Drive Files Not Appearing

iCloud Drive syncs your Desktop, Documents, and other folders across devices. When it fails, files may be missing, not downloading, or stuck in a syncing state.

## Common Causes
- iCloud storage is full and cannot store new files
- Network connection is slow or intermittent
- iCloud Drive is not enabled in System Preferences
- File conflicts between local and cloud versions
- iCloud Drive daemon is stuck or crashed

## How to Fix
1. Check iCloud storage and free up space
2. Ensure iCloud Drive is enabled in System Preferences > Apple ID > iCloud
3. Sign out of iCloud and sign back in to force a re-sync
4. Check the iCloud Drive folder for stuck files
5. Restart the iCloud drive daemon from terminal

```bash
# Check iCloud Drive status
ls -la ~/Library/Mobile\ Documents/

# Restart iCloud services
killall bird
killall cloudd
```

## Examples

```bash
# Check iCloud storage usage
du -sh ~/Library/Mobile\ Documents/
```

This error is common when iCloud storage is full, when the network connection drops during a large file upload, or when the iCloud Drive daemon crashes and needs a restart.
