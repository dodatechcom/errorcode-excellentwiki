---
title: "[Solution] macOS Bluetooth Mouse Lag -- Wireless Mouse Pointer Stutters"
description: "Fix macOS Bluetooth mouse lag when the wireless mouse pointer stutters or jumps. Resolve Bluetooth mouse lag on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Bluetooth Mouse Lag -- Wireless Mouse Pointer Stutters

Bluetooth mouse lag on Mac appears as the cursor freezing momentarily, jumping across the screen, or responding slowly to movement.

## Common Causes
- Bluetooth bandwidth is shared with other connected devices
- USB 3.0 interference affecting the Bluetooth radio
- Mouse battery is low causing weak signal
- WiFi on 2.4 GHz is interfering with Bluetooth
- Mouse polling rate is set too low in third-party software

## How to Fix
1. Replace or recharge the mouse battery
2. Disconnect other Bluetooth devices to free bandwidth
3. Move USB 3.0 devices away from the Mac or the mouse receiver
4. Switch WiFi to the 5 GHz band
5. Ensure macOS and mouse firmware are up to date

```bash
# Check connected Bluetooth devices
system_profiler SPBluetoothDataType

# Check mouse battery level (if reported by macOS)
# Go to System Preferences > Mouse to see battery indicator
```

## Examples

```bash
# Monitor Bluetooth connection quality
log show --predicate 'process == "bluetoothd"' --last 3m --style compact
```

This error is common when USB 3.0 hubs are near the Mac, when the mouse battery is low, or when too many Bluetooth devices are competing for bandwidth.
