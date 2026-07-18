---
title: "[Solution] macOS Rainbow Wheel Error — Persistent Spinning Cursor"
description: "Fix macOS rainbow wheel of death: persistent spinning cursor across all apps, system appears completely frozen, requires hard reset."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 103
---

# Rainbow Wheel Error — Persistent Spinning Cursor

Fix macOS rainbow wheel of death: persistent spinning cursor across all apps, system appears completely frozen, requires hard reset.

## Common Causes

- System-wide resource exhaustion from memory or CPU overload
- Corrupted system file preventing normal operation
- Failing storage drive causing I/O timeout on critical operations
- macOS launchd or WindowServer process stuck in infinite loop

## How to Fix

### 1. Force Restart the Mac

```bash
# Hold power button for 10 seconds until Mac turns off
log show --predicate 'eventMessage contains "hang"' --last 1h | head -20
```

### 2. Boot into Safe Mode to Diagnose

```bash
# Intel: Hold Shift after startup chime
kextstat | grep -v com.apple
```

### 3. Run Disk Utility First Aid

```bash
diskutil verifyVolume disk0s1
# Recovery → Disk Utility → First Aid
```

### 4. Reset System Preferences and Cache

```bash
rm -rf ~/Library/Caches/*
sudo rm -rf /Library/Caches/*
sudo rm -rf /var/folders/*
sudo shutdown -r now
```

## Common Scenarios

This error commonly occurs when:

- Rainbow wheel appears system-wide and no app responds
- Persistent spinning cursor started after macOS software update
- System shows rainbow wheel immediately after login
- Rainbow wheel occurs only when running specific combination of apps

## Prevent It

- Restart Mac regularly to prevent memory exhaustion and cache buildup
- Monitor disk health and replace failing drives before complete failure
- Avoid running too many resource-intensive apps simultaneously
- Keep macOS updated to receive fixes for known system hangs
