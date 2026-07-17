---
title: "[Solution] macOS Display Error — External Monitor Not Detected"
description: "Fix macOS display errors when external monitors aren't detected, show wrong resolution, or flicker. Resolve display output issues on Mac."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["display", "monitor", "resolution", "external", "thunderbolt", "hdmi"]
weight: 5
---

# macOS Display Error Fix

Display errors on macOS include external monitors not being detected, wrong resolution, flickering, black screens, or the display showing artifacts.

## What This Error Means

macOS display management handles multiple monitors through WindowServer. When an external display isn't detected or functions incorrectly, it's usually a cable, adapter, or GPU configuration issue.

## Common Causes

- Faulty or incompatible display cable/adapter
- Monitor set to wrong input source
- macOS display preference corruption
- GPU driver issue (especially with eGPU)
- Monitor not supporting the resolution/refresh rate

## How to Fix

### 1. Reset display preferences

```bash
# Delete display preference files
sudo rm -f /Library/Preferences/com.apple.windowserver.plist
rm -f ~/Library/Preferences/ByHost/com.apple.windowserver.*

# Restart the Mac
```

### 2. Check connected displays

```bash
# List all displays
system_profiler SPDisplaysDataType

# Check display connection status
ioreg -l | grep -i "display"
```

### 3. Force detect displays

```bash
# Option-click the Scaled resolution option in System Preferences → Displays
# This reveals additional resolutions
# Or hold Option while clicking "Detect Displays" in the Displays preference pane
```

### 4. Reset NVRAM (display-related settings)

```bash
# Shut down Mac
# Turn on and hold Option+Command+P+R for 20 seconds
# This resets display output settings
```

## Related Errors

- [GPU Kernel Panic](macos-kernel-panic-gpu) — GPU-related display crashes
- [Metal Error](metal-error) — Metal graphics API errors
- [Kernel Panic](kernel-panic) — system crashes affecting display
