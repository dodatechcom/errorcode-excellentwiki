---
title: "[Solution] macOS AirDrop Error — 'Person' Could Not Be Received"
description: "Fix macOS AirDrop errors: person could not be received, no one nearby, transfer failed. Fix Bluetooth, Wi-Fi, firewall, and visibility settings."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
tags: ["airdrop", "bluetooth", "wi-fi", "transfer", "nearby-sharing"]
weight: 5
---

# AirDrop Error — "Person" Could Not Be Received

An AirDrop error occurs when your Mac cannot send or receive files to/from another Apple device over Wi-Fi and Bluetooth. Common messages include "'Person' could not be received," "No People Nearby," and "Waiting."

## Description

AirDrop uses Bluetooth LE for discovery and peer-to-peer Wi-Fi for transfer. Both radios must be working, and both devices must be within range. AirDrop is supported from macOS Yosemite (10.10) onward.

Common error messages:

- `"Person" could not be received.`
- `No People Nearby — Make sure the other person is nearby and sharing with AirDrop.`
- `AirDrop Waiting — Decline / Accept`
- `AirDrop transfer failed.`

## Common Causes

- Wi-Fi or Bluetooth is turned off on either device
- Firewall blocking incoming connections
- AirDrop receiving is set to "Contacts Only" and you're not in each other's contacts
- Both devices are not on the same Wi-Fi network (not required but helps)
- macOS AirDrop daemon crashed

## How to Fix AirDrop Errors

### 1. Ensure Wi-Fi and Bluetooth Are Enabled

```bash
# Check Wi-Fi status
networksetup -getairportnetwork en0

# Check Bluetooth status
system_profiler SPBluetoothDataType | grep "State"

# Turn on Wi-Fi if off
networksetup -setairportpower en0 on

# Turn on Bluetooth if off
defaults write /Library/Preferences/com.apple.Bluetooth BluetoothPower -bool true
```

### 2. Set AirDrop to "Everyone"

```bash
# System Settings → General → AirDrop
# Set "Allow me to be discovered by" to "Everyone"
# Or for a temporary fix, set to "Everyone for 10 Minutes"
```

### 3. Fix Firewall Blocking AirDrop

```bash
# System Settings → Network → Firewall → Options
# Ensure "Block all incoming connections" is OFF
# Or add AirDrop to the allowed list

# Check firewall status
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
```

### 4. Restart AirDrop Services

```bash
# Kill and restart the AirDrop-related processes
killall sharingd
killall UserEventAgent

# They will restart automatically
# Wait 30 seconds and try AirDrop again
```

### 5. Check Bluetooth Discovery Mode

```bash
# Ensure Mac is discoverable
defaults write com.apple.NetworkBrowser DisableAirDrop -bool false

# Verify AirDrop is enabled
defaults read com.apple.NetworkBrowser DisableAirDrop
# 0 = enabled, 1 = disabled
```

### 6. Reset Network Settings

```bash
# Remove Wi-Fi preferences (will forget networks)
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.wifi.message-tracer.plist

# Restart Mac to reconfigure Wi-Fi
```

## Examples

This error commonly occurs when:

- One device has Bluetooth off while the other has Wi-Fi off
- The Mac's firewall is set to block all incoming connections
- You're not in each other's contacts list and AirDrop is set to "Contacts Only"
- macOS Sleep/Wake cycle puts Bluetooth into a low-power state

## Related Errors

- [Finder Error](finder-error) — "The operation can't be completed" when saving AirDrop files
- [Keychain Error](keychain-error) — Bluetooth pairing issues
- [iCloud Error](icloud-error) — AirDrop uses iCloud for contact identification
