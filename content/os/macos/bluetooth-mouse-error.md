---
title: "[Solution] macOS Bluetooth Mouse Error — Magic Mouse Not Connecting"
description: "Fix macOS Bluetooth mouse error: Magic Mouse not connecting, mouse lag or stuttering, mouse disconnects randomly."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 173
---

# Bluetooth Mouse Error — Magic Mouse Not Connecting

Fix macOS Bluetooth mouse error: Magic Mouse not connecting, mouse lag or stuttering, mouse disconnects randomly.

## Common Causes

- Magic Mouse battery too low for stable connection
- Bluetooth interference from other wireless devices
- Mouse Bluetooth firmware needs update
- Mac Bluetooth module experiencing intermittent issues

## How to Fix

### 1. Check Mouse Connection and Battery

```bash
system_profiler SPBluetoothDataType | grep -A 10 'Mouse'
# Check battery level: System Settings → Bluetooth → Mouse
```

### 2. Re-Pair Magic Mouse

```bash
# System Settings → Bluetooth → Forget This Device
# Turn mouse off → wait 10 seconds → turn on → re-pair
```

### 3. Reset Bluetooth Module

```bash
# Hold Shift+Option → Click Bluetooth menu → Reset Bluetooth Module
sudo shutdown -r now
```

### 4. Clean Mouse Sensor and Surface

```bash
# Use mouse on clean, non-reflective surface for best tracking
```

## Common Scenarios

This error commonly occurs when:

- Magic Mouse cursor stutters or jumps across screen
- Mouse disconnects several times per day requiring re-pairing
- Magic Mouse not detected in Bluetooth settings at all
- Mouse works for a few minutes then stops responding

## Prevent It

- Keep Magic Mouse battery above 20% for stable connection
- Place Mac and mouse within 10 feet with clear line of sight
- Update macOS for latest Magic Mouse driver improvements
- Clean mouse sensor regularly for optimal tracking performance
