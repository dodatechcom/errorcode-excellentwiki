---
title: "[Solution] macOS Brightness Error -- Display Brightness Not Working"
description: "Fix macOS brightness error when display brightness controls do not work. Resolve brightness adjustment issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Brightness Error -- Display Brightness Not Working

Brightness controls allow you to adjust the screen brightness on MacBook or external displays. When they fail, the screen may be too bright or too dark, or the brightness keys may not respond.

## Common Causes
- Brightness keys are not mapped correctly
- Display driver issue preventing brightness adjustment
- External display does not support DDC brightness control
- SMC is not managing brightness correctly
- Night Shift or True Tone is interfering

## How to Fix
1. Check System Preferences > Displays for brightness settings
2. Try adjusting brightness from the menu bar
3. Reset SMC on Intel Macs
4. Disable Night Shift and True Tone temporarily
5. Check if the external display supports brightness control

```bash
# Check display brightness settings
defaults read com.apple.Brightness

# Reset SMC (Intel Macs with T2)
# Shut down, hold left Shift+Control+Option+Power for 10 seconds
```

## Examples

```bash
# Adjust brightness from terminal (requires brightness CLI tool)
# brew install brightness
brightness 0.5
```

This error is common when the SMC needs a reset, when an external display does not support DDC brightness control, or when Night Shift interferes with brightness adjustment.
