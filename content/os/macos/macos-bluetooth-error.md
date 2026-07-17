---
title: "[Solution] macOS Bluetooth Error — Device Not Connecting"
description: "Fix macOS Bluetooth errors when devices won't pair, connect, or keep disconnecting. Reset Bluetooth module and resolve pairing issues."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["bluetooth", "pairing", "connection", "peripherals", "wireless"]
weight: 5
---

# macOS Bluetooth Error Fix

Bluetooth errors on macOS include devices refusing to pair, frequent disconnections, audio stuttering, or the Bluetooth menu showing "Bluetooth: Not Available."

## What This Error Means

macOS Bluetooth relies on the Bluetooth module and its associated daemon (`blued`). When pairing or connection fails, it's usually due to corrupted pairing data, interference, or a stuck Bluetooth module.

## Common Causes

- Corrupt Bluetooth cache or pairing database
- Bluetooth module stuck in bad state
- Interference from USB 3.0 devices or other 2.4GHz signals
- macOS update breaking Bluetooth compatibility
- Peripheral device out of range or low battery

## How to Fix

### 1. Reset the Bluetooth module

```bash
# Hold Shift+Option and click the Bluetooth menu bar icon
# Click "Reset the Bluetooth module" at the bottom
# Or via terminal:
sudo pkill bluetoothd
# macOS will automatically relaunch the daemon
```

### 2. Delete Bluetooth preference files

```bash
# Remove corrupt pairing data
sudo rm -f /Library/Preferences/com.apple.Bluetooth.plist

# Remove the Bluetooth pairing database
sudo rm -rf /Library/Preferences/ByHost/com.apple.Bluetooth.*

# Restart the Mac and re-pair devices
```

### 3. Remove specific device and re-pair

```bash
# Open System Preferences → Bluetooth
# Hover over the device → click the X to remove it
# Put the device in pairing mode
# Click "Connect" when it appears in the Bluetooth list
```

### 4. Check Bluetooth diagnostics

```bash
# Check Bluetooth status
system_profiler SPBluetoothDataType

# View Bluetooth logs
log show --predicate 'subsystem == "com.apple.bluetooth"' --last 1h
```

## Related Errors

- [USB Error](macos-usb-error) — USB device connection issues
- [Handoff Error](macos-handoff-error) — continuity features that depend on Bluetooth
- [AirDrop Error](macos-airdrop-error) — AirDrop requires Bluetooth
