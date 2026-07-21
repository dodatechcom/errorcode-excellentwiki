---
title: "[Solution] macOS Stuck on Apple Logo -- Startup Hangs Before Login"
description: "Fix macOS stuck on Apple logo at startup. Resolve Mac hanging before the login screen appears with progress bar frozen."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Stuck on Apple Logo -- Startup Hangs Before Login

When macOS hangs at the Apple logo, the progress bar either never appears, moves partway and stops, or the display remains on the logo indefinitely. The system is attempting to load kernel extensions and system daemons but is blocked.

## Common Causes
- Corrupted font cache or launch services database
- Failing internal drive with unreadable blocks
- Corrupted user account preventing login window from loading
- Incompatible login item or launch agent
- FileVault encryption process stalled

## How to Fix
1. Hold the power button to shut down, wait 30 seconds, and power on again
2. Boot into Safe Mode to bypass startup items
3. In Recovery Mode, run First Aid on both the data volume and container
4. Use Recovery terminal to check and repair boot volume permissions

```bash
# In Recovery Mode terminal
diskutil list
diskutil verifyVolume disk1s1
```

## Examples

```bash
# Force a verbose boot to see where it hangs
# Hold Command+V during startup to see boot messages
```

This issue frequently occurs when a third-party launch agent installed before a macOS update crashes during the boot sequence, or when FileVault is re-encrypting and encounters bad sectors.
