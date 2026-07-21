---
title: "[Solution] macOS Boot Picker Error -- Option Key Not Showing Boot Volumes"
description: "Fix macOS boot picker not appearing when holding Option key at startup. Resolve Mac not showing available boot disks."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Boot Picker Error -- Option Key Not Showing Boot Volumes

The boot picker is the screen that appears when you hold Option during startup, showing all available boot volumes. When it fails to appear or shows no volumes, you cannot select an alternate startup disk.

## Common Causes
- Option key is not being held long enough or at the right time
- USB keyboard not initializing fast enough to register the keypress
- NVRAM corruption preventing boot picker from loading
- Only one bootable volume exists and the picker skips it
- Apple Silicon Macs use a different boot picker via the power button

## How to Fix
1. On Apple Silicon Macs, press and hold the power button until startup options appear
2. On Intel Macs, press and hold Option immediately after pressing the power button
3. Reset NVRAM if the boot picker is consistently failing
4. Try a different USB port for your keyboard

```bash
# Reset NVRAM on Intel Macs
# Shut down, then power on and hold Option+Command+P+R for 20 seconds
# Release and the boot picker should appear on next startup
```

## Examples

```bash
# Check if multiple bootable volumes exist from terminal
diskutil list
bless --info --verbose /
bless --info --verbose --getboot
```

This issue is common when using third-party keyboards that do not initialize quickly enough, after an NVRAM corruption, or when a Boot Camp partition has been improperly removed.
