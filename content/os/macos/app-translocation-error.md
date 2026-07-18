---
title: "[Solution] macOS App Translocation Error — App Moved to Quarantine"
description: "Fix macOS app translocation: app moved to quarantine location, app translocated and cannot save data, random path prefix."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 204
---

# App Translocation Error — App Moved to Quarantine

Fix macOS app translocation: app moved to quarantine location, app translocated and cannot save data, random path prefix.

## Common Causes

- macOS translocating app to prevent unsigned code execution
- App opened from DMG or unverified source triggering translocation
- Quarantine attribute causing path randomization
- App data stored in translocated path lost after restart

## How to Fix

### 1. Remove Quarantine Attribute

```bash
sudo xattr -rd com.apple.quarantine /path/to/app.app
# Remove quarantine flag to prevent translocation
```

### 2. Move App to Applications Folder

```bash
# Drag app from DMG directly to /Applications/ instead of opening from DMG
```

### 3. Check Translocation Path

```bash
ps aux | grep app
# Look for randomized /var/folders/ path in process info
```

### 4. Reinstall App from Trusted Source

```bash
# Delete translocated copy → Download fresh from official source
```

## Common Scenarios

This error commonly occurs when:

- App opens from random path like /private/var/folders/... instead of /Applications/
- App cannot find its own data files due to path randomization
- App settings reset every time because translocated path changes
- App was moved from DMG and shows quarantine warning

## Prevent It

- Always drag apps to /Applications/ folder instead of running from DMG
- Remove quarantine attribute for trusted apps using xattr command
- Reinstall app from official source if translocation causes issues
- Check app path in Activity Monitor to detect translocation
