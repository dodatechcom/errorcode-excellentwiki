---
title: "[Solution] macOS Find My Error — Cannot Locate Mac"
description: "Fix macOS Find My not working: cannot locate Mac remotely, Find My Mac shows offline, location services not working for Find My."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 120
---

# Find My Error — Cannot Locate Mac

Fix macOS Find My not working: cannot locate Mac remotely, Find My Mac shows offline, location services not working for Find My.

## Common Causes

- Find My Mac not enabled in System Settings
- Mac not connected to internet for location reporting
- Location Services disabled preventing Find My from working
- Find My service experiencing server-side issues

## How to Fix

### 1. Verify Find My Mac Is Enabled

```bash
defaults read com.apple.FindMyMac
# System Settings → Apple ID → Find My → Find My Mac → Toggle ON
```

### 2. Enable Location Services

```bash
sudo defaults write /Library/Preferences/com.apple.locationd.plist LocationServicesEnabled -bool true
# System Settings → Privacy & Security → Location Services
```

### 3. Check Internet Connection

```bash
ping -c 3 google.com
networksetup -getairportnetwork en0
# Ensure Power Nap is enabled for sleep-time location
```

### 4. Test Find My from iCloud.com

```bash
open https://www.icloud.com/find
# Sign in with your Apple ID and select your Mac
```

## Common Scenarios

This error commonly occurs when:

- Find My Mac shows 'Offline' in iCloud.com when Mac is clearly on
- Location displayed in Find My is outdated by many hours
- Cannot play sound or lock Mac remotely via Find My
- Find My Mac option is grayed out in System Settings

## Prevent It

- Keep Find My Mac enabled at all times in System Settings
- Ensure Mac stays connected to internet even when in sleep mode
- Enable Power Nap to allow Find My to locate Mac during sleep
- Keep macOS updated for Find My service compatibility
