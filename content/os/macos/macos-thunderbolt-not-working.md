---
title: "[Solution] macOS Thunderbolt Not Working -- Thunderbolt Device Not Detected"
description: "Fix macOS Thunderbolt not working when Thunderbolt devices are not detected or connected. Resolve Thunderbolt connection issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Thunderbolt Not Working -- Thunderbolt Device Not Detected

Thunderbolt ports on Mac can connect displays, storage, docks, and eGPUs. When Thunderbolt stops working, connected devices are not recognized.

## Common Causes
- Thunderbolt controller needs a reset (SMC issue)
- Thunderbolt cable is damaged or not Thunderbolt-certified
- Connected device has a firmware issue
- macOS Thunderbolt driver was affected by an update
- NVRAM corruption is preventing Thunderbolt initialization

## How to Fix
1. Disconnect and reconnect the Thunderbolt device
2. Reset the SMC on Intel Macs
3. Reset NVRAM to clear Thunderbolt configuration
4. Try a different Thunderbolt cable
5. Check for firmware updates for the connected device

```bash
# Check Thunderbolt bus status
system_profiler SPThunderboltDataType

# Reset SMC (Intel Macs with T2)
# Shut down, hold left Shift+Control+Option+Power for 10 seconds, release, then power on
```

## Examples

```bash
# Monitor Thunderbolt events
log show --predicate 'eventMessage contains "Thunderbolt"' --last 10m
```

This error is common after a macOS update resets the Thunderbolt controller, when a non-certified cable is used, or when the SMC needs to be reset on Intel Macs.
