---
title: "[Solution] macOS Boot Loop -- Mac Keeps Restarting Repeatedly"
description: "Fix macOS boot loop where Mac keeps restarting over and over. Resolve infinite restart cycles during Mac startup."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Boot Loop -- Mac Keeps Restarting Repeatedly

A boot loop is a condition where macOS continuously restarts without reaching the desktop. The Mac may show the Apple logo briefly, go black, then restart again in an endless cycle.

## Common Causes
- Corrupted system extensions or kexts installed before an update
- Startup item causing a crash on every boot
- Corrupted NVRAM or SMC settings
- APFS volume container corruption
- macOS update installed incompatible system components

## How to Fix
1. Boot into Safe Mode (hold Shift) to load macOS with minimal extensions
2. If Safe Mode works, remove recently installed kexts or apps from Login Items
3. Reset NVRAM and SMC to clear corrupted settings
4. Boot into Recovery and use Disk Utility First Aid on the startup volume
5. Use Recovery terminal to remove problematic kexts manually

```bash
# In Recovery Mode terminal
# List third-party kexts
ls /Library/Extensions/ | grep -v com.apple

# Remove a problematic kext
sudo rm -rf /Library/Extensions/BadKext.kext
```

## Examples

```bash
# Check system logs from Recovery Mode
log show --predicate 'eventMessage contains "boot"' --last 10m
```

This error often appears after installing VPN software with a kernel extension, after a forced shutdown during an update, or when an external GPU is connected during startup.
