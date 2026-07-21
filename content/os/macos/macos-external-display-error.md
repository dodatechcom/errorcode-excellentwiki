---
title: "[Solution] macOS External Display Error -- External Monitor Not Working"
description: "Fix macOS external display error when external monitor is not detected or shows no signal. Resolve external display issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS External Display Error -- External Monitor Not Working

External display errors on Mac can manifest as no signal, incorrect resolution, flickering, or the display not being detected at all.

## Common Causes
- Display cable is damaged or not connected properly
- Adapter or dongle is incompatible with the Mac
- Display resolution is set to one the monitor cannot support
- GPU driver issue causing display initialization failure
- Multiple displays have conflicting resolution settings

## How to Fix
1. Disconnect and reconnect the display cable
2. Try a different cable or adapter
3. Reset NVRAM to clear display settings
4. Hold Option and click 'Detect Displays' in System Preferences
5. Try the display at a lower resolution first

```bash
# Check detected displays
system_profiler SPDisplaysDataType

# Reset NVRAM
# Shut down, power on, hold Option+Command+P+R for 20 seconds
```

## Examples

```bash
# Force display detection from terminal
defaults write com.apple.preference.discovery DisplayConnectDisabled -bool false
```

This error is common when using cheap USB-C to HDMI adapters, when the display cable is partially connected, or when the GPU driver has a bug with a specific resolution.
