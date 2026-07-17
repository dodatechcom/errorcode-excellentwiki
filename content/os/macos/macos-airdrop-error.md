---
title: "[Solution] macOS AirDrop Not Working"
description: "Fix AirDrop not working on Mac when you can't send or receive files. Resolve discovery, connection, and transfer issues."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS AirDrop Not Working Fix

AirDrop errors include devices not appearing, transfers failing, or AirDrop being completely unavailable. Both Wi-Fi and Bluetooth must be enabled for AirDrop to function.

## What This Error Means

AirDrop uses a combination of Wi-Fi (for data transfer) and Bluetooth Low Energy (for device discovery). When either fails, AirDrop cannot discover or connect to nearby devices.

## Common Causes

- Wi-Fi or Bluetooth turned off
- AirDrop set to "Contacts Only" and recipient not in contacts
- Personal Hotspot active (blocks Wi-Fi)
- macOS Firewall blocking AirDrop connections
- Bluetooth module in bad state
- 5GHz Wi-Fi band incompatibility with some devices

## How to Fix

### 1. Ensure Wi-Fi and Bluetooth are on

```bash
# Check Wi-Fi status
networksetup -getairportnetwork en0

# Check Bluetooth status
system_profiler SPBluetoothDataType | grep -i "state\|connected"
```

### 2. Set AirDrop to "Everyone"

```bash
# Open Finder → Go → AirDrop
# Click "Allow me to be discovered by:" → select "Everyone"
# Or via terminal:
defaults write com.apple.NetworkBrowser DisableAirDrop -bool false
```

### 3. Reset network and Bluetooth

```bash
# Turn off Wi-Fi and Bluetooth
networksetup -setairportpower en0 off
sudo defaults write /Library/Preferences/com.apple.Bluetooth ControllerPowerState -int 0

# Wait 30 seconds
# Turn both back on
networksetup -setairportpower en0 on
sudo defaults write /Library/Preferences/com.apple.Bluetooth ControllerPowerState -int 1
sudo killall -HUP bluetoothd
```

### 4. Check Firewall settings

```bash
# Ensure Firewall isn't blocking AirDrop
# System Preferences → Security & Privacy → Firewall → Firewall Options
# Uncheck "Block all incoming connections"
# Ensure "AirDrop" is allowed
```

## Related Errors

- [Bluetooth Error](macos-bluetooth-error) — Bluetooth connectivity issues
- [Wi-Fi Error](macos-wifi-error) — Wi-Fi connection problems
- [Handoff Error](macos-handoff-error) — continuity feature issues
