---
title: "[Solution] macOS Bluetooth Audio Stuttering -- Bluetooth Audio Cuts Out"
description: "Fix macOS Bluetooth audio stuttering when audio cuts out or stutters over Bluetooth speakers or headphones. Resolve Bluetooth audio issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Bluetooth Audio Stuttering -- Bluetooth Audio Cuts Out

Bluetooth audio stuttering manifests as intermittent audio dropouts, crackling, or brief silences during playback. This is usually caused by interference or bandwidth issues.

## Common Causes
- WiFi and Bluetooth are sharing the same antenna and interfering
- USB 3.0 devices are generating electromagnetic interference
- Bluetooth codec settings are not optimal
- The Bluetooth device is too far from the Mac
- Multiple Bluetooth devices are connected simultaneously

## How to Fix
1. Move the Mac closer to the Bluetooth audio device
2. Disconnect other Bluetooth devices to free up bandwidth
3. Use 5 GHz WiFi instead of 2.4 GHz to reduce Bluetooth interference
4. Switch to a wired connection if possible
5. Reset the Bluetooth module by holding Shift+Option and clicking the Bluetooth icon

```bash
# Check connected Bluetooth devices
system_profiler SPBluetoothDataType | grep -A 5 "Connected"

# Remove a problematic Bluetooth device and re-pair
sudo defaults delete /Library/Preferences/com.apple.Bluetooth
```

## Examples

```bash
# Monitor Bluetooth connection quality
log show --predicate 'process == "bluetoothd"' --last 5m
```

This error is common when USB 3.0 hard drives are near the Bluetooth device, when the Mac is at the edge of Bluetooth range, or when too many Bluetooth devices are connected simultaneously.
