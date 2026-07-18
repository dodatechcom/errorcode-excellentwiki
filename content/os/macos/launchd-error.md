---
title: "[Solution] macOS launchd Error — System Services Fail to Start"
description: "Fix macOS launchd failure: system services fail to start at boot, apps crash on launch, login items missing or not loading."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 110
---

# launchd Error — System Services Fail to Start

Fix macOS launchd failure: system services fail to start at boot, apps crash on launch, login items missing or not loading.

## Common Causes

- Corrupted launch daemon or agent plist file
- Missing executable referenced by launch daemon configuration
- Permission issue preventing launchd from starting service
- Circular dependency between system services at boot

## How to Fix

### 1. Check Launchd Service Status

```bash
launchctl list
launchctl list | grep -i fail
log show --predicate 'subsystem == "com.apple.launchd"' --last 1h | grep -i error
```

### 2. Repair Corrupted Plist Files

```bash
plutil -lint /Library/LaunchDaemons/com.example.service.plist
sudo launchctl bootout system/com.example.service
```

### 3. Reset Launch Services Database

```bash
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -kill -r -domain local -domain system -domain user
```

### 4. Reload Failed Services

```bash
sudo launchctl bootout system/com.apple.service.name
sudo launchctl bootstrap system /Library/LaunchDaemons/com.apple.service.name.plist
```

## Common Scenarios

This error commonly occurs when:

- Multiple apps fail to launch with error about missing services
- Login items do not appear after user logs in
- System services like Spotlight or Time Machine stop working
- launchd error appears in Console when checking system logs

## Prevent It

- Validate plist files before adding them to LaunchDaemons
- Avoid modifying system launch daemons manually unless necessary
- Keep macOS updated to receive launchd stability fixes
- Back up launch daemon configurations before making changes
