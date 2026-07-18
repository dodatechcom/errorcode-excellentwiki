---
title: "[Solution] macOS Bluetooth Pairing Error — Cannot Pair with Device"
description: "Fix macOS Bluetooth pairing failure: cannot pair with Bluetooth device, pairing code rejected, connection refused or timed out."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 171
---

# Bluetooth Pairing Error — Cannot Pair with Device

Fix macOS Bluetooth pairing failure: cannot pair with Bluetooth device, pairing code rejected, connection refused or timed out.

## Common Causes

- Bluetooth device already paired with another device
- Pairing PIN or passkey entered incorrectly
- Device Bluetooth firmware incompatible with macOS
- Mac Bluetooth cache corrupted preventing new pairings

## How to Fix

### 1. Reset Bluetooth and Re-Pair

```bash
# System Settings → Bluetooth → Forget This Device for the target device
# Put device in pairing mode and re-pair
```

### 2. Clear Bluetooth Cache

```bash
sudo rm -f /Library/Preferences/com.apple.Bluetooth.plist
sudo killall -HUP bluetoothd
sudo shutdown -r now
```

### 3. Check Device Compatibility

```bash
# Ensure device supports Bluetooth 4.0+ for modern macOS
# Check device manufacturer website for macOS compatibility
```

### 4. Try Pairing via Different Method

```bash
# Some devices pair better via USB first, then switch to Bluetooth
```

## Common Scenarios

This error commonly occurs when:

- Bluetooth pairing code is rejected when entered on Mac
- Device appears in Bluetooth list but pairing times out
- Paired device shows 'Connected' but immediately disconnects
- New Bluetooth device not appearing in discovery list at all

## Prevent It

- Forget device and pair fresh if pairing code is rejected
- Check device manual for correct pairing procedure with macOS
- Update device firmware for better macOS Bluetooth compatibility
- Reset Bluetooth module if multiple devices fail to pair
