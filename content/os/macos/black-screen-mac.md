---
title: "[Solution] macOS Black Screen Error — Display Shows Nothing After Boot"
description: "Fix macOS black screen: display shows nothing after boot, wake, or update, but Mac appears running with fans audible."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 105
---

# Black Screen Error — Display Shows Nothing After Boot

Fix macOS black screen: display shows nothing after boot, wake, or update, but Mac appears running with fans audible.

## Common Causes

- Display backlight failure or cable disconnection
- GPU not initializing during boot due to driver issue
- macOS login window process failing before display output
- Corrupted NVRAM settings preventing display initialization

## How to Fix

### 1. Check if Mac Is Actually Running

```bash
system_profiler SPDisplaysDataType
# Listen for startup chime and fan noise
# Connect external display via Thunderbolt/HDMI
```

### 2. Reset NVRAM and SMC

```bash
# Intel: Hold Option+Command+P+R for 20s
sudo shutdown -r now
```

### 3. Boot into Recovery Mode

```bash
# Intel: Restart and hold Command+R
nvram -c
```

### 4. Reset Display and Boot Preferences

```bash
rm -f /Library/Preferences/com.apple.windowserver.plist
# Restart normally
```

## Common Scenarios

This error commonly occurs when:

- Mac appears to boot but display stays completely black
- Black screen appears after macOS update and never recovers
- Display works with external monitor but not built-in screen
- Black screen occurs after Mac sleeps and cannot wake properly

## Prevent It

- Always back up Mac before installing macOS updates
- Reset NVRAM if display issues begin appearing after hardware changes
- Keep macOS updated to receive display initialization fixes
- Test display brightness and external monitors for early hardware issues
