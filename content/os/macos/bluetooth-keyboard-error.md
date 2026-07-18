---
title: "[Solution] macOS Bluetooth Keyboard Error — Magic Keyboard Not Working"
description: "Fix macOS Bluetooth keyboard error: Magic Keyboard not pairing, keyboard input lag, keyboard disconnects during use."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 174
---

# Bluetooth Keyboard Error — Magic Keyboard Not Working

Fix macOS Bluetooth keyboard error: Magic Keyboard not pairing, keyboard input lag, keyboard disconnects during use.

## Common Causes

- Magic Keyboard battery too low for reliable connection
- Bluetooth interference causing keyboard disconnects
- Keyboard paired with different Apple ID or device
- Mac Bluetooth cache preventing keyboard reconnection

## How to Fix

### 1. Check Keyboard Connection and Battery

```bash
system_profiler SPBluetoothDataType | grep -A 10 'Keyboard'
# Check battery: System Settings → Bluetooth → Keyboard
```

### 2. Re-Pair Magic Keyboard

```bash
# System Settings → Bluetooth → Forget This Device for keyboard
# Turn keyboard off → wait 10 seconds → turn on → re-pair
```

### 3. Reset Bluetooth and Keyboard

```bash
# Hold Shift+Option → Click Bluetooth menu → Reset Bluetooth Module
# If keyboard still won't connect, use USB keyboard to navigate
```

### 4. Check for macOS Keyboard Settings

```bash
# System Settings → Keyboard → Ensure 'Input Sources' is configured correctly
```

## Common Scenarios

This error commonly occurs when:

- Magic Keyboard types slowly with noticeable input lag
- Keyboard disconnects intermittently during typing
- Keyboard pairs but no input is registered on Mac
- Bluetooth keyboard not appearing in device list for pairing

## Prevent It

- Keep Magic Keyboard battery charged above 20% for reliable typing
- Reset Bluetooth module if keyboard disconnects frequently
- Use USB keyboard as backup for navigating to Bluetooth settings
- Update macOS for latest Magic Keyboard compatibility fixes
