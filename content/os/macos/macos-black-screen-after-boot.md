---
title: "[Solution] macOS Black Screen After Boot -- Mac Boots to Black Screen"
description: "Fix macOS black screen after boot when Mac starts but shows only a black screen. Resolve black screen after login on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Black Screen After Boot -- Mac Boots to Black Screen

A black screen after boot indicates the Mac has started but the display is not showing the desktop. The cursor may or may not be visible, and you may hear the startup chime or fan noise.

## Common Causes
- WindowServer process crashed during startup
- Display resolution is set to an unsupported value
- User account is corrupted
- Login item is crashing and preventing the desktop from loading
- GPU driver failed to initialize properly

## How to Fix
1. Try pressing any key or moving the mouse to wake the display
2. Force shutdown and try booting into Safe Mode
3. Reset NVRAM to clear display settings
4. Try creating a new user account from Recovery Mode
5. Boot into Recovery Mode and run Disk Utility First Aid

```bash
# Try to access Activity Monitor if you can get to a terminal
# Press Command+Space, type Terminal

# Force quit unresponsive apps
killall WindowServer
```

## Examples

```bash
# Check WindowServer status
ps aux | grep WindowServer
```

This error is common when WindowServer crashes, when the display resolution is set to an unsupported value, or when a login item crashes and prevents the desktop from loading.
