---
title: "[Solution] macOS Find My Error -- Find My Mac Not Working"
description: "Fix macOS Find My error when Find My Mac cannot locate the device. Resolve Find My Mac location and activation issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Find My Error -- Find My Mac Not Working

Find My Mac allows you to locate, lock, or erase your Mac remotely. When it fails, the Mac may not appear in the Find My app on your other devices, or the location may be incorrect.

## Common Causes
- Find My Mac is not enabled in System Preferences
- Location Services are disabled
- The Mac is not connected to the internet
- Apple ID is not signed in or the session expired
- Location Services daemon has crashed

## How to Fix
1. Enable Find My Mac in System Preferences > Apple ID > iCloud
2. Enable Location Services in System Preferences > Security & Privacy
3. Ensure the Mac is connected to the internet
4. Sign out of iCloud and back in
5. Restart the Mac to reset the location services daemon

```bash
# Check Find My Mac status
defaults read com.apple.FindMyMac

# Check Location Services
defaults read com.apple.locationd
```

## Examples

```bash
# View Find My errors
log show --predicate 'process == "findmydeviced"' --last 10m
```

This error is common when Find My Mac was not enabled, when Location Services are disabled, or when the Mac loses its internet connection and cannot report its location.
