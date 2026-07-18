---
title: "[Solution] macOS Bluetooth Error — Bluetooth Not Working or Pairing Fails"
description: "Fix macOS Bluetooth error: Bluetooth not working, devices not pairing, Bluetooth menu icon missing or grayed out."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 170
---

# Bluetooth Error — Bluetooth Not Working or Pairing Fails

Fix macOS Bluetooth error: Bluetooth not working, devices not pairing, Bluetooth menu icon missing or grayed out.

## Common Causes

- Bluetooth module frozen or not responding
- Corrupted Bluetooth preference files
- Bluetooth hardware antenna issue in Mac
- Third-party Bluetooth device incompatible with macOS

## How to Fix

### 1. Check Bluetooth Status

```bash
system_profiler SPBluetoothDataType | grep 'State'
defaults read /Library/Preferences/com.apple.Bluetooth BluetoothPower
```

### 2. Reset Bluetooth Module

```bash
# Hold Shift+Option → Click Bluetooth menu → Reset the Bluetooth Module
sudo rm -f /Library/Preferences/com.apple.Bluetooth.plist
sudo killall -HUP bluetoothd
```

### 3. Delete Bluetooth Preferences

```bash
sudo rm -rf /Library/Preferences/ByHost/com.apple.Bluetooth.*
sudo shutdown -r now
```

### 4. Check for Hardware Issues

```bash
# Run Apple Diagnostics: restart and hold D
# Check for Bluetooth hardware errors in system log
```

## Common Scenarios

This error commonly occurs when:

- Bluetooth icon grayed out in menu bar
- Bluetooth devices pair but immediately disconnect
- Cannot discover any Bluetooth devices nearby
- Bluetooth turns on but immediately turns off again

## Prevent It

- Reset Bluetooth module if devices stop pairing
- Keep macOS updated for Bluetooth driver improvements
- Remove Bluetooth devices that consistently fail to pair
- Run Apple Diagnostics if Bluetooth hardware issues suspected
