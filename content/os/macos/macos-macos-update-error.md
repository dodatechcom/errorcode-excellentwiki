---
title: "[Solution] macOS Software Update Error"
description: "Fix macOS software update errors when System Preferences shows 'Update Not Found,' downloads fail, or installation fails with error codes."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Software Update Error Fix

Software update errors include "No updates available" (when updates exist), download failures, installation failures, or "An error occurred while installing updates."

## What This Error Means

macOS Software Update checks Apple's servers for available updates and downloads/installs them. Failures can be due to network issues, corrupted update cache, disk space, or Apple server problems.

## Common Causes

- Insufficient disk space for the update
- Network connection issues
- Corrupt update cache
- Date/time incorrect preventing SSL validation
- macOS Recovery partition missing or corrupt
- Apple server outage

## How to Fix

### 1. Check for updates via terminal

```bash
# Check for available updates
softwareupdate -l

# Install all available updates
sudo softwareupdate -ia

# Install a specific update
sudo softwareupdate -i "macOS Sonoma 14.2"
```

### 2. Clear the Software Update cache

```bash
# Remove cached updates
sudo rm -rf /Library/Updates/*

# Delete Software Update preferences
sudo rm -f /Library/Preferences/com.apple.SoftwareUpdate.plist
```

### 3. Verify disk space

```bash
# Check available disk space
df -h /

# macOS updates typically need 15-20GB free
```

### 4. Reset Software Update service

```bash
# Stop the Software Update service
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.softwareupdated.plist

# Wait 10 seconds
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.softwareupdated.plist
```

## Related Errors

- [macOS Install Error](macos-macos-install-error) — full OS installation errors
- [macOS Recovery Error](macos-macos-recovery) — recovery mode issues
- [Disk Utility Error](disk-utility-error) — disk space and repair issues
