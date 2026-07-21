---
title: "[Solution] macOS Gray Screen Error -- Mac Shows Gray Screen at Startup"
description: "Fix macOS gray screen error when Mac displays a gray screen during startup. Resolve gray screen issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Gray Screen Error -- Mac Shows Gray Screen at Startup

A gray screen during startup typically appears after the Apple logo and indicates the system is loading but cannot complete the process. It may show a spinning gear or progress bar that stalls.

## Common Causes
- Corrupted system files or login items
- Display driver issue during the late boot phase
- FileVault is failing to unlock the volume
- Third-party kext is blocking the boot
- APFS container has errors

## How to Fix
1. Force shutdown and try booting into Safe Mode
2. Boot into Recovery Mode and run First Aid on the startup volume
3. Check FileVault status and try disabling it temporarily
4. Remove recently installed kexts from Recovery Mode terminal
5. Reset NVRAM and try again

```bash
# From Recovery Mode terminal
# Check FileVault status
diskutil apfs list | grep -i "FileVault"

# List third-party kexts
ls /Library/Extensions/ | grep -v com.apple
```

## Examples

```bash
# Boot into Safe Mode (hold Shift during startup)
# This loads macOS with minimal extensions
```

This error is common when FileVault fails to unlock, when a third-party kext blocks the boot, or when the APFS container has errors that First Aid can repair.
