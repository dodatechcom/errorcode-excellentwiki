---
title: "[Solution] macOS Kernel Panic Bluetooth — Bluetooth Driver Crash"
description: "Fix macOS kernel panic from Bluetooth: system crashes when using Bluetooth peripherals, AirDrop, or when Bluetooth module fails."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 95
---

# Kernel Panic Bluetooth — Bluetooth Driver Crash

Fix macOS kernel panic from Bluetooth: system crashes when using Bluetooth peripherals, AirDrop, or when Bluetooth module fails.

## Common Causes

- Failing Bluetooth module or antenna cable disconnection
- Corrupted Bluetooth kext or preference files
- Incompatible Bluetooth device causing stack overflow
- Bluetooth module firmware issue requiring reset

## How to Fix

### 1. Check Bluetooth Panic and Module Info

```bash
system_profiler SPBluetoothDataType | grep -A 5 'State'
log show --predicate 'eventMessage contains "bluetooth"' --last 24h | grep panic
```

### 2. Reset Bluetooth Module

```bash
sudo rm -f /Library/Preferences/com.apple.Bluetooth.plist
sudo killall -HUP bluetoothd
```

### 3. Remove Faulty Bluetooth Devices

```bash
system_profiler SPBluetoothDataType | grep -A 10 'Connected: Yes'
# Unpair all devices via System Settings → Bluetooth
```

### 4. Update macOS and Check Hardware

```bash
softwareupdate -i -a
# Run Apple Diagnostics: restart and hold D
```

## Common Scenarios

This error commonly occurs when:

- Mac crashes when connecting specific Bluetooth mouse or keyboard
- Kernel panic log references AppleBluetooth or IOBluetoothFamily
- Panic occurs when using AirDrop or Bluetooth audio
- Bluetooth module shows as unavailable after kernel panic

## Prevent It

- Remove Bluetooth devices that consistently trigger kernel panics
- Keep macOS updated to receive Bluetooth driver improvements
- Avoid pairing too many Bluetooth devices simultaneously
- Check Apple Diagnostics periodically for Bluetooth hardware health
