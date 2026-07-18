---
title: "[Solution] macOS AirDrop Not Working — Cannot Find or Send to Devices"
description: "Fix macOS AirDrop not working: AirDrop cannot find devices, AirDrop transfer fails, AirDrop option grayed out in Finder."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 175
---

# AirDrop Not Working — Cannot Find or Send to Devices

Fix macOS AirDrop not working: AirDrop cannot find devices, AirDrop transfer fails, AirDrop option grayed out in Finder.

## Common Causes

- Wi-Fi or Bluetooth disabled preventing AirDrop functionality
- Firewall blocking AirDrop connections
- Both devices not discoverable by each other
- macOS AirDrop daemon (sharingd) not running properly

## How to Fix

### 1. Ensure Wi-Fi and Bluetooth Are Enabled

```bash
networksetup -getairportnetwork en0
system_profiler SPBluetoothDataType | grep 'State'
networksetup -setairportpower en0 on
```

### 2. Set AirDrop to Everyone

```bash
# System Settings → General → AirDrop → Allow me to be discovered by → Everyone
```

### 3. Fix Firewall Blocking AirDrop

```bash
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

### 4. Restart AirDrop Services

```bash
killall sharingd
killall UserEventAgent
# They will restart automatically
```

## Common Scenarios

This error commonly occurs when:

- AirDrop says 'No People Nearby' even with nearby Apple devices
- AirDrop shows 'Waiting' but transfer never starts
- AirDrop option grayed out in Finder share menu
- AirDrop finds device but transfer fails immediately

## Prevent It

- Set AirDrop to 'Everyone for 10 Minutes' for temporary sharing
- Ensure both Wi-Fi and Bluetooth are enabled on both devices
- Check firewall settings if AirDrop is blocked
- Restart sharingd daemon if AirDrop stops finding devices
