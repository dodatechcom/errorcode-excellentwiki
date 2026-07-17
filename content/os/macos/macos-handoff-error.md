---
title: "[Solution] macOS Handoff Not Working"
description: "Fix Handoff not working on Mac when continuity features fail between iPhone, iPad, and Mac. Resolve clipboard and handoff issues."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Handoff Not Working Fix

Handoff allows you to start a task on one Apple device and continue on another. When it fails, tasks don't transfer between devices, and the Handoff icon doesn't appear in the Dock.

## What This Error Means

Handoff requires both Wi-Fi and Bluetooth to be enabled, the same Apple ID signed in on all devices, and two-factor authentication active. It uses Bluetooth for discovery and Wi-Fi for data transfer.

## Common Causes

- Different Apple IDs on devices
- Wi-Fi or Bluetooth disabled on either device
- Two-factor authentication not enabled
- Bluetooth module stuck
- Handoff disabled in settings
- macOS or iOS version mismatch

## How to Fix

### 1. Verify Handoff is enabled on Mac

```bash
# System Preferences → General → "Allow Handoff between this Mac and your iCloud devices"
# Ensure it is checked
defaults read com.apple.preference.general Handoff
```

### 2. Ensure same Apple ID and 2FA

```bash
# Verify Apple ID on Mac
defaults read /Library/Preferences/com.apple.AppleMultitouchTrackpad

# Check System Preferences → Apple ID
# Both devices must use the same Apple ID with 2FA enabled
```

### 3. Restart Bluetooth and Wi-Fi on both devices

```bash
# On Mac: toggle Bluetooth and Wi-Fi off and on
# On iPhone/iPad: toggle Airplane Mode on and off
```

### 4. Reset the Handoff preference

```bash
defaults delete com.apple.preference.general Handoff
defaults write com.apple.preference.general Handoff -bool true
```

## Related Errors

- [Universal Clipboard](macos-universal-clipboard) — clipboard sharing issues
- [Continuity Camera](macos-continuity-error) — continuity camera errors
- [Bluetooth Error](macos-bluetooth-error) — Bluetooth connection issues
