---
title: "[Solution] macOS iCloud Sync Error -- iCloud Data Not Syncing Between Devices"
description: "Fix macOS iCloud sync error when iCloud data stops syncing between Mac and other Apple devices. Resolve iCloud sync issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS iCloud Sync Error -- iCloud Data Not Syncing Between Devices

iCloud sync errors prevent your contacts, calendars, notes, and other data from staying up to date across all your Apple devices. Changes made on one device do not appear on others.

## Common Causes
- iCloud account needs to be re-authenticated
- iCloud storage is full and cannot sync new data
- Network connectivity issues preventing sync
- iCloud system status is experiencing outages
- Conflicting data on multiple devices causing merge failures

## How to Fix
1. Sign out of iCloud and sign back in
2. Check iCloud storage and free up space if needed
3. Ensure all devices are connected to the internet
4. Check Apple's iCloud system status page
5. Toggle the specific app's iCloud sync off and on

```bash
# Check iCloud account status
defaults read MobileMeAccounts

# Check iCloud storage
# System Preferences > Apple ID > iCloud
```

## Examples

```bash
# View iCloud sync errors in logs
log show --predicate 'process == "cloudd" or process == "ubd"' --last 10m
```

This error is common when iCloud storage is full, when the Apple ID session has expired, or when there are conflicting data entries that the sync engine cannot merge automatically.
