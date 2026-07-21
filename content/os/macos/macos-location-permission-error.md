---
title: "[Solution] macOS Location Permission Error -- App Cannot Access Location"
description: "Fix macOS location permission error when an app cannot access location services. Resolve location permission issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Location Permission Error -- App Cannot Access Location

Apps need location permission to determine your geographic location. When permission is not granted, location-based features like maps, weather, and Find My do not work.

## Common Causes
- Location Services are disabled globally
- App location permission was not granted
- TCC database is corrupted
- Location Services daemon has crashed
- Privacy settings restrict location access

## How to Fix
1. Enable Location Services in System Preferences > Privacy & Security > Location Services
2. Enable location permission for the specific app
3. Check that the Location Services daemon is running
4. Reset location permissions and re-grant them
5. Restart the Mac to reload location services

```bash
# Check Location Services status
defaults read com.apple.locationd

# Check location permissions
sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db "SELECT client FROM access WHERE service='kTCCServiceLocation';"

# Reset location permissions
tccutil reset Location
```

## Examples

```bash
# Check Location Services status
systemsetup -getusingnetworktime
```

This error is common when Location Services are disabled globally, when the app location permission was not granted, or when the Location Services daemon has crashed.
