---
title: "[Solution] macOS Software Update Error"
description: "Fix macOS software update errors. Resolve 'An error occurred', update stuck downloading, and failed macOS Ventura/Sonoma/Sequoia updates."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS Software Update Error

macOS update errors include "An error occurred while downloading the selected updates", update stuck at "Preparing", or the update failing during installation.

## What This Error Means

macOS updates are delivered via the Software Update daemon (`softwareupdated`) and can fail due to network issues, insufficient disk space, corrupted update cache, or incompatible third-party software. Major version upgrades use a full installer that may have different failure modes.

## Common Causes

- Insufficient disk space (need 15-35 GB for major upgrades)
- Network issue during large download
- Corrupt SoftwareUpdate cache
- Third-party kext or software incompatible with new macOS
- Firmware update pending (Apple Silicon)
- VPN or proxy interfering with update download

## How to Fix

### Check Available Updates

```bash
softwareupdate --list
```

### Free Up Disk Space

```bash
# Check disk space
df -h /

# Clear caches
sudo rm -rf /Library/Caches/*
rm -rf ~/Library/Caches/*

# Clear old Time Machine local snapshots
tmutil thinlocalsnapshots / 1000000000 4
```

### Reset Software Update Daemon

```bash
sudo launchctl bootout system /System/Library/LaunchDaemons/com.apple.SoftwareUpdate.plist
sudo launchctl bootstrap system /System/Library/LaunchDaemons/com.apple.SoftwareUpdate.plist
```

### Delete Update Cache

```bash
sudo rm -rf /Library/Updates/*
sudo rm -rf /var/folders/*/*/com.apple.SoftwareUpdate/*
```

### Use Full Installer for Major Upgrades

```bash
# Download full installer
softwareupdate --fetch-full-installer --full-installer-version 14.0

# Or from App Store
```

### Check for Firmware Updates (Apple Silicon)

```bash
# Check current firmware
system_profiler SPHardwareDataType | grep "Firmware"

# Firmware updates install during macOS update
# Ensure Mac is plugged in during update
```

### Boot into Safe Mode and Update

```bash
# Intel: Hold Shift during startup
# Apple Silicon: Hold power button, select disk, hold Shift
# Then try Software Update from Safe Mode
```

## Related Errors

- [macOS Firmware Error]({{< relref "/os/macos/macos-firmware-error-v2" >}}) — Firmware update issues
- [macOS Gatekeeper Error]({{< relref "/os/macos/macos-gatekeeper-error-v2" >}}) — App blocking after update
- [Kernel Panic]({{< relref "/os/macos/kernel-panic" >}}) — Kernel panic after update
