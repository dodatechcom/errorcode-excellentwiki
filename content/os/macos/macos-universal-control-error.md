---
title: "[Solution] macOS Universal Control Error -- Universal Control Not Working"
description: "Fix macOS Universal Control error when Mac and iPad cannot share keyboard and mouse. Resolve Universal Control connection issues."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Universal Control Error -- Universal Control Not Working

Universal Control allows you to use a single keyboard and mouse across multiple Macs and iPads. When it fails, the devices may not be discovered or the cursor may not move between them.

## Common Causes
- Both devices are not signed into the same Apple ID
- Bluetooth or WiFi is turned off on one device
- Universal Control is not enabled in System Preferences
- Devices are too far apart for Bluetooth discovery
- macOS or iPadOS version does not support Universal Control

## How to Fix
1. Ensure both devices are signed into the same Apple ID with two-factor authentication
2. Enable Universal Control in System Preferences > Displays > Advanced
3. Enable Bluetooth and WiFi on both devices
4. Place devices within 10 feet of each other
5. Update both devices to the latest macOS/iPadOS version

```bash
# Check Universal Control status
# System Preferences > Displays > Advanced

# Verify both devices are on the same Apple ID
# System Preferences > Apple ID
```

## Examples

```bash
# Check Bluetooth status
system_profiler SPBluetoothDataType | grep -i "connected"

# Check WiFi status
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I
```

This error is common when the devices are signed into different Apple IDs, when Bluetooth is disabled, or when the devices are too far apart for Bluetooth discovery.
