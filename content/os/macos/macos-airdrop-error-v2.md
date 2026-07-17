---
title: "[Solution] AirDrop Cannot See Other Devices Error on Mac"
description: "Fix AirDrop errors when Mac cannot discover other devices, files fail to send, or AirDrop not working at all."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# AirDrop Cannot See Other Devices Error on Mac

AirDrop cannot discover nearby devices, files fail to send, or receives "AirDrop: No one nearby" messages.

## What This Error Means

AirDrop uses both Wi-Fi and Bluetooth to discover and transfer files between Apple devices. Discovery failures occur when one or both radios are disabled, restricted, or malfunctioning, or when security settings block AirDrop.

## Common Causes

- Wi-Fi or Bluetooth disabled
- Firewall blocking AirDrop connections
- AirDrop set to "No One" or "Contacts Only" with no matching contacts
- Bluetooth discovery not working
- Network isolation (different Wi-Fi networks)
- macOS privacy settings restricting discovery

## How to Fix

### Enable Wi-Fi and Bluetooth

```bash
# Check Wi-Fi status
networksetup -getairportpower en0

# Enable Wi-Fi
networksetup -setairportpower en0 on

# Check Bluetooth status
system_profiler SPBluetoothDataType | grep "State"
```

### Configure AirDrop Visibility

```bash
# Set AirDrop to everyone (temporary)
defaults write com.apple.NetworkBrowser DisableAirDrop -bool false

# Or via GUI: Finder > AirDrop > "Allow me to be discovered by:"
```

### Check Firewall Settings

```bash
# Check if firewall is blocking AirDrop
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --listapps

# Allow AirDrop through firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setblockall off
```

### Reset Bluetooth and Wi-Fi

```bash
# Reset Bluetooth module
sudo pkill bluetoothd

# Reset Wi-Fi
sudo networksetup -setairportpower en0 off
sleep 2
sudo networksetup -setairportpower en0 on
```

### Check Firewall for AirDrop

```bash
# Allow incoming connections for AirDrop
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/libexec/AssetCacheLocatorUtil
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblockapp /usr/libexec/AssetCacheLocatorUtil
```

### Verify Contact Settings

If using "Contacts Only":
- Ensure both devices are signed into iCloud
- Exchange Apple ID email addresses in Contacts app
- Both devices must have each other's email in contact cards

## Related Errors

- [Handoff Error]({{< relref "/os/macos/macos-handoff-error-v2" >}}) — Continuity features
- [Wi-Fi Error]({{< relref "/os/macos/macos-wifi-error-v2" >}}) — Network connectivity
- [Bluetooth Error]({{< relref "/os/macos/macos-bluetooth-error" >}}) — Bluetooth issues
