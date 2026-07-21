---
title: "[Solution] macOS White Screen Error -- Mac Shows White Screen at Startup"
description: "Fix macOS white screen error when Mac displays a white or blank screen during startup. Resolve white screen issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS White Screen Error -- Mac Shows White Screen at Startup

A white or blank screen during startup indicates the system has powered on but cannot initialize the display or complete the boot process.

## Common Causes
- GPU or display driver is failing to initialize
- Display cable is disconnected or damaged
- System files required for display initialization are corrupted
- External display is interfering with the built-in display
- NVRAM has incorrect display settings

## How to Fix
1. Force shutdown and try booting with verbose mode (Command+V)
2. Reset NVRAM to clear display settings
3. Disconnect any external displays
4. Boot into Recovery Mode and run First Aid
5. Try booting from an external drive to isolate the issue

```bash
# Reset NVRAM
# Shut down, power on, hold Option+Command+P+R for 20 seconds

# Verbose boot to see where it hangs
# Hold Command+V during startup
```

## Examples

```bash
# Check display hardware
system_profiler SPDisplaysDataType
```

This error is common when the GPU driver fails to initialize, when an external display interferes, or when NVRAM has incorrect display settings.
