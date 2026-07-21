---
title: "[Solution] macOS Boot Timeout -- Mac Stuck on Apple Logo"
description: "Fix macOS boot timeout when Mac is stuck on Apple logo during startup. Resolve boot loops and infinite loading on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Boot Timeout -- Mac Stuck on Apple Logo

A boot timeout occurs when macOS fails to complete the startup process within the expected timeframe. The Mac displays the Apple logo with a progress bar that stalls or never advances.

## Common Causes
- Corrupted system files from an interrupted macOS update
- Failing storage drive unable to read boot files
- Incorrect startup disk selected in System Preferences
- FileVault encryption keys failing to unlock the drive
- Third-party kernel extensions blocking the boot sequence

## How to Fix
1. Force shutdown by holding the power button for 10 seconds, then retry
2. Boot into Safe Mode by holding Shift during startup
3. Reset NVRAM by holding Option+Command+P+R for 20 seconds
4. Boot into Recovery Mode (Command+R) and run Disk Utility First Aid
5. Reinstall macOS from Recovery Mode if the disk checks out

```bash
# Boot into Recovery Mode
# Hold Command+R during startup
# Open Disk Utility and select your startup disk
# Click First Aid to repair the disk
```

## Examples

```bash
# Check startup disk from Recovery terminal
diskutil list
diskutil verifyVolume disk1s1
```

This error commonly happens after a failed macOS update, when FileVault is enabled and the drive has bad sectors, or after connecting an external Thunderbolt device during boot.
