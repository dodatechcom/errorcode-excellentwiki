---
title: "[Solution] macOS Blue Screen Error — Display Turns Blue"
description: "Fix macOS blue screen: display turns solid blue with spinning cursor, system unresponsive, requires force restart to recover."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 100
---

# Blue Screen Error — Display Turns Blue

Fix macOS blue screen: display turns solid blue with spinning cursor, system unresponsive, requires force restart to recover.

## Common Causes

- WindowServer process crash leaving display in undefined state
- Graphics driver failure during display mode change
- Corrupted system UI framework or missing display resources
- macOS login window process failing to initialize properly

## How to Fix

### 1. Force Restart and Check Logs

```bash
ls -lt /Library/Logs/DiagnosticReports/WindowServer* | head -5
log show --predicate 'eventMessage contains "WindowServer"' --last 1h
```

### 2. Boot into Safe Mode

```bash
# Intel: Hold Shift after hearing startup chime
kextstat | grep -v com.apple
```

### 3. Reset WindowServer Preferences

```bash
defaults delete com.apple.windowserver.plist
rm -f ~/Library/Preferences/ByHost/com.apple.windowserver.*.plist
sudo shutdown -r now
```

### 4. Reinstall macOS Display Components

```bash
# Recovery → Reinstall macOS to restore system files
```

## Common Scenarios

This error commonly occurs when:

- Mac shows blue screen after login and never reaches desktop
- Blue screen appears when switching display modes or resolutions
- WindowServer crash report generated at time of blue screen
- Blue screen occurs only when external display is connected

## Prevent It

- Keep macOS updated to receive WindowServer stability fixes
- Avoid installing third-party display enhancement utilities
- Use compatible display resolution and refresh rate settings
- Run Disk Utility First Aid to check system file corruption
