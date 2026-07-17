---
title: "[Solution] Mac Trackpad Error"
description: "Fix Mac trackpad errors when the trackpad stops responding, clicks register incorrectly, or Force Touch/scrolling malfunctions."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["trackpad", "click", "scroll", "force-touch", "pointing-device"]
weight: 5
---

# Mac Trackpad Error Fix

Trackpad errors include unresponsive clicking, erratic cursor movement, broken scrolling, or Force Touch not working. These can be software (driver) or hardware (physical) issues.

## What This Error Means

The trackpad uses the AppleMultitouchTrackpad driver and communicates via the I2C/SPI bus. Software issues can be fixed by resetting preferences or the SMC; hardware issues require service.

## Common Causes

- Corrupt trackpad preference file
- SMC not properly managing trackpad hardware
- Swollen battery pressing on trackpad
- Liquid damage under the trackpad surface
- macOS update breaking trackpad driver

## How to Fix

### 1. Reset trackpad preferences

```bash
# Delete trackpad preferences
rm -f ~/Library/Preferences/com.apple.AppleMultitouchTrackpad.plist
rm -f ~/Library/Preferences/com.apple.driver.AppleBluetoothMultitouch.trackpad.plist

# Restart the Mac
```

### 2. Reset the SMC

```bash
# Intel MacBooks:
# Shut down → Hold Shift+Control+Option+Power for 10 sec → Release → Power on

# This resets trackpad hardware management
```

### 3. Test in Safe Mode

```bash
# Boot in Safe Mode (hold Shift during startup)
# If trackpad works in Safe Mode, a third-party kext is causing the issue
```

### 4. Check trackpad diagnostics

```bash
# Run Apple Diagnostics
# Shut down → Hold D during startup
# Check for error codes related to input devices
```

## Related Errors

- [Keyboard Error](macos-keyboard-error) — keyboard input issues
- [Touch Bar Error](macos-touchbar-error) — Touch Bar malfunctions
- [Touch ID Error](macos-touch-id-error) — biometric sensor issues
