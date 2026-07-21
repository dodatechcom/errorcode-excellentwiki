---
title: "[Solution] macOS Display Resolution Error -- Wrong Resolution on External Display"
description: "Fix macOS display resolution error when external display shows incorrect resolution. Resolve display resolution issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Display Resolution Error -- Wrong Resolution on External Display

When an external display shows the wrong resolution, the image may appear stretched, blurry, or not fill the entire screen. This is usually a configuration or driver issue.

## Common Causes
- Display is not using the native resolution
- HDMI or DisplayPort cable does not support the resolution
- GPU cannot drive the display at the desired resolution
- Display EDID information is incorrect
- Multiple displays have conflicting resolution settings

## How to Fix
1. Open System Preferences > Displays and select the correct resolution
2. Hold Option and click Scaled to see all available resolutions
3. Try a different cable that supports the desired resolution
4. Reset NVRAM to clear display settings
5. Check the display's native resolution in its settings menu

```bash
# Check current display settings
system_profiler SPDisplaysDataType

# Reset NVRAM
# Shut down, power on, hold Option+Command+P+R for 20 seconds
```

## Examples

```bash
# List available display resolutions
system_profiler SPDisplaysDataType | grep -A 20 "Resolution"
```

This error is common when using a cable that does not support the display's full resolution, when the display EDID is incorrectly read, or when NVRAM has cached incorrect display settings.
