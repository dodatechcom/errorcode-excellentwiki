---
title: "[Solution] Handoff Not Working Between Devices Error on Mac"
description: "Fix Handoff errors on macOS when Continuity features like Handoff, Universal Clipboard, or Nearby Sharing don't work between devices."
platforms: ["macos"]
severities: ["error"]
error-types: ["system-error"]
tags: ["handoff", "continuity", "universal-clipboard", "airdrop", "macos"]
weight: 5
---

# Handoff Not Working Between Devices Error on Mac

Handoff doesn't work between Mac and other Apple devices, Universal Clipboard fails, or Continuity features are unavailable.

## What This Error Means

Handoff and Continuity features require both Wi-Fi and Bluetooth to be enabled, both devices signed into the same Apple ID, and proper network configuration. Failures occur when one or more prerequisites are not met.

## Common Causes

- Wi-Fi or Bluetooth disabled on either device
- Devices not signed into same Apple ID
- Two-factor authentication not enabled
- Handoff disabled in System Settings
- Different iCloud accounts on devices
- Network isolation preventing device communication

## How to Fix

### Verify Requirements

Both devices must have:
- Wi-Fi enabled
- Bluetooth enabled
- Same Apple ID signed in
- Two-factor authentication enabled
- Handoff enabled in settings

### Enable Handoff

```bash
# Check Handoff status
defaults read com.apple.handoff HandoffSupportEnabled 2>/dev/null || echo "Not set"

# Enable Handoff
defaults write com.apple.handoff HandoffSupportEnabled -bool true

# Or via System Settings > General > AirDrop & Handoff > Allow Handoff
```

### Check Apple ID Match

```bash
# Verify Apple ID on this Mac
defaults read MobileMeAccounts 2>/dev/null | grep AccountID

# Both devices must show the same Apple ID
```

### Reset Continuity Services

```bash
# Restart continuity daemons
sudo pkill -f com.apple.continuity*
sudo pkill -f com.apple.sharingd

# Restart Bluetooth
sudo pkill bluetoothd

# Restart Wi-Fi
networksetup -setairportpower en0 off
sleep 2
networksetup -setairportpower en0 on
```

### Check Network Configuration

```bash
# Ensure both devices are on same network subnet
ifconfig en0 | grep inet

# Check for AP isolation (common in public Wi-Fi)
# Both devices must be able to communicate directly
```

### Reset Universal Clipboard

```bash
# Reset clipboard service
defaults delete com.apple.pboard
killall pboard
```

## Related Errors

- [AirDrop Error]({{< relref "/os/macos/macos-airdrop-error-v2" >}}) — AirDrop discovery
- [Wi-Fi Error]({{< relref "/os/macos/macos-wifi-error-v2" >}}) — Network issues
- [Bluetooth Error]({{< relref "/os/macos/macos-bluetooth-error" >}}) — Bluetooth issues
