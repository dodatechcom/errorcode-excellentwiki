---
title: "[Solution] macOS AirDrop Discoverability Error — Mac Not Visible to Others"
description: "Fix macOS AirDrop discoverability: Mac not visible to other devices, AirDrop contacts-only not finding friends, AirDrop invisible."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 176
---

# AirDrop Discoverability Error — Mac Not Visible to Others

Fix macOS AirDrop discoverability: Mac not visible to other devices, AirDrop contacts-only not finding friends, AirDrop invisible.

## Common Causes

- AirDrop set to 'Contacts Only' and not in contacts list
- Bluetooth not discoverable preventing AirDrop visibility
- Wi-Fi not on same network hindering device discovery
- AirDrop daemon not broadcasting discovery signal

## How to Fix

### 1. Set AirDrop Discovery to Everyone

```bash
# System Settings → General → AirDrop → Set to 'Everyone'
# Or 'Everyone for 10 Minutes' for temporary discoverability
```

### 2. Check Bluetooth Discovery Mode

```bash
defaults write com.apple.NetworkBrowser DisableAirDrop -bool false
defaults read com.apple.NetworkBrowser DisableAirDrop
```

### 3. Verify AirDrop Is Enabled

```bash
# System Settings → General → AirDrop → Ensure 'Allow me to be discovered' is ON
# Check sharingd is running: ps aux | grep sharingd
```

### 4. Restart AirDrop Daemon

```bash
killall sharingd
# sharingd will restart automatically and re-enable AirDrop discovery
```

## Common Scenarios

This error commonly occurs when:

- Other devices cannot see your Mac in AirDrop even when nearby
- AirDrop works for sending but not receiving from other devices
- Contacts-only AirDrop cannot find people who are in your contacts
- AirDrop discoverable status toggles off by itself

## Prevent It

- Set AirDrop to Everyone temporarily when sharing with non-contacts
- Ensure both Bluetooth and Wi-Fi are enabled for discoverability
- Keep sharingd daemon running for AirDrop to function
- Restart Mac if AirDrop discoverability stops working
