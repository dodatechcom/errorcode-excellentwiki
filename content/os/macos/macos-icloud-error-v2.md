---
title: "[Solution] iCloud Sync Conflict Error on Mac"
description: "Fix iCloud sync errors on macOS when documents conflict, files don't sync, or iCloud Drive shows sync conflicts."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# iCloud Sync Conflict Error on Mac

iCloud shows sync conflicts, documents don't update across devices, or "conflict" copies appear in Finder.

## What This Error Means

iCloud sync conflicts occur when the same document is edited on multiple devices simultaneously, or when sync fails due to network issues, storage limits, or account problems. Conflicting versions are saved as separate files.

## Common Causes

- Same document edited offline on multiple devices
- Network connectivity during sync
- iCloud storage full
- iCloud account signed out on one device
- Third-party apps not iCloud-aware
- Date/time mismatch between devices

## How to Fix

### Check iCloud Storage

```bash
# Check iCloud storage usage
du -sh ~/Library/Mobile\ Documents/

# Or via System Settings > Apple ID > iCloud
# Free up space if near limit
```

### Resolve Conflicts Manually

```bash
# Find conflict files
find ~/Library/Mobile\ Documents -name "*conflict*"

# Conflict files are usually named:
# DocumentName (Conflicted copy date).ext
# Compare and merge manually
```

### Force iCloud Sync

```bash
# Reset iCloud sync daemon
killall bird

# Reset iCloud Drive sync
brctl log --wait --shorten 2>&1 | head -100

# Monitor sync activity
brctl status
```

### Check Account Status

```bash
# Verify iCloud sign-in
defaults read MobileMeAccounts 2>/dev/null | grep -A 5 AccountID

# Sign out and back in if needed
# System Settings > Apple ID > Sign Out (keep data)
# Then sign back in
```

### Clear iCloud Cache

```bash
# Reset iCloud document cache
rm -rf ~/Library/Caches/CloudKit/*

# Reset iCloud Drive cache
rm -rf ~/Library/Mobile\ Documents/.DS_Store
```

### Check Date and Time

```bash
# Sync conflicts can occur with time mismatches
sudo systemsetup -setusingnetworktime on
sudo sntp -sS time.apple.com
```

## Related Errors

- [Apple ID Error]({{< relref "/os/macos/macos-apple-id-error-v2" >}}) — Account issues
- [Time Machine Error]({{< relref "/os/macos/macos-timemachine-error-v2" >}}) — Backup issues
- [Wi-Fi Error]({{< relref "/os/macos/macos-wifi-error-v2" >}}) — Network issues
