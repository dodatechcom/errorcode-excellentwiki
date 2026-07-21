---
title: "[Solution] macOS Battery Not Charging -- MacBook Plugged In But Not Charging"
description: "Fix macOS battery not charging when MacBook is plugged in but the battery percentage does not increase. Resolve charging issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Battery Not Charging -- MacBook Plugged In But Not Charging

When a MacBook is plugged in but the battery does not charge, it may be due to battery management features, faulty hardware, or power adapter issues.

## Common Causes
- Optimized Battery Charging is limiting charge to 80%
- Power adapter wattage is insufficient for the MacBook
- Charging cable or adapter is damaged
- Battery health is degraded
- SMC is not managing charging correctly

## How to Fix
1. Check if Optimized Battery Charging is enabled and temporarily disable it
2. Try a different power adapter with sufficient wattage
3. Reset the SMC to recalibrate battery management
4. Check the battery health and consider replacement if degraded
5. Try charging when the Mac is powered off

```bash
# Check battery status
system_profiler SPPowerDataType

# Check if Optimized Battery Charging is active
defaults read com.apple.PowerCharger
```

## Examples

```bash
# Check charging status from terminal
ioreg -l | grep -i "CurrentCapacity\|MaxCapacity\|IsCharging"
```

This error is common when Optimized Battery Charging limits the charge to 80%, when the power adapter wattage is insufficient, or when the battery has degraded beyond useful life.
