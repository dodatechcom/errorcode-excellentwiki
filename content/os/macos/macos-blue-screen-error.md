---
title: "[Solution] macOS Blue Screen Error -- Mac Shows Blue Screen at Startup"
description: "Fix macOS blue screen error when Mac displays a blue screen during startup. Resolve blue screen issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Blue Screen Error -- Mac Shows Blue Screen at Startup

A blue screen on macOS (not to be confused with Windows BSOD) typically appears when the system is loading but cannot complete the startup process. It may flash briefly or remain stuck.

## Common Causes
- Corrupted system files or user account
- Display driver issue during startup
- Incompatible login item or launch agent
- File system corruption on the startup volume
- macOS update left the system in an inconsistent state

## How to Fix
1. Force shutdown and try booting into Safe Mode
2. Boot into Recovery Mode and run Disk Utility First Aid
3. Create a new user account to test if the issue is account-specific
4. Reset NVRAM to clear display settings
5. Reinstall macOS from Recovery Mode as a last resort

```bash
# Boot into Safe Mode (hold Shift during startup)
# Boot into Recovery Mode (hold Command+R during startup)

# From Recovery terminal
diskutil verifyVolume disk1s1
```

## Examples

```bash
# Check system logs from Recovery
log show --predicate 'eventMessage contains "blue"' --last 10m
```

This error is common after a corrupted macOS update, when a login item crashes during startup, or when the display driver has an issue loading.
