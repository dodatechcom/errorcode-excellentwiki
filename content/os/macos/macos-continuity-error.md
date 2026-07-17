---
title: "[Solution] macOS Continuity Camera Error"
description: "Fix Continuity Camera not working on Mac when you can't scan documents or take photos with iPhone from Mac."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Continuity Camera Error Fix

Continuity Camera lets you use your iPhone's camera to scan documents or take photos directly into a Mac app. When it fails, the option doesn't appear or the transfer fails.

## What This Error Means

Continuity Camera requires both devices to be signed into the same Apple ID with Wi-Fi and Bluetooth enabled. It uses AirDrop-like protocols for image transfer.

## Common Causes

- Devices on different Apple IDs
- Wi-Fi or Bluetooth disabled
- iPhone camera not accessible (locked with passcode only)
- macOS or iOS version too old
- Third-party firewall blocking the transfer

## How to Fix

### 1. Ensure both devices meet requirements

```bash
# Check macOS version (requires macOS Mojave or later)
sw_vers

# Check iOS version (requires iOS 12 or later) on the iPhone
# Both devices must be on the same Apple ID with 2FA
```

### 2. Enable Continuity on Mac

```bash
# Ensure Handoff is enabled
defaults read com.apple.preference.general Handoff

# If not enabled:
defaults write com.apple.preference.general Handoff -bool true
```

### 3. Restart both devices

```bash
# Restart the Mac
sudo shutdown -r now "Restarting for Continuity Camera"

# Force restart iPhone (hold power + volume down for 10 seconds)
```

### 4. Check camera permissions

```bash
# Ensure the target app has camera access
# System Preferences → Security & Privacy → Privacy → Camera
# Check the app is listed and enabled
```

## Related Errors

- [Handoff Error](macos-handoff-error) — general Handoff issues
- [AirDrop Error](macos-airdrop-error) — AirDrop file transfer issues
- [Universal Clipboard](macos-universal-clipboard) — clipboard sharing issues
