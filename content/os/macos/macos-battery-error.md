---
title: "[Solution] Mac Battery Service Error"
description: "Fix Mac battery errors when you see 'Service Recommended,' battery won't charge, or battery health shows 'Replace Soon.' Resolve battery issues."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["battery", "charging", "power", "health", "service"]
weight: 5
---

# Mac Battery Service Error Fix

Battery errors include "Service Recommended" messages, failure to charge, sudden shutdowns at low percentages, or battery health showing degraded capacity.

## What This Error Means

macOS monitors battery health via the SMC and reports cycle count, maximum capacity, and condition. "Service Recommended" means the battery has degraded significantly and should be replaced.

## Common Causes

- Battery has reached end of lifecycle (1000+ cycles)
- SMC not properly managing battery charging
- MagSafe/USB-C charging port issue
- Battery management system calibration off
- Swollen battery (requires immediate service)

## How to Fix

### 1. Check battery health

```bash
# Check battery cycle count and condition
system_profiler SPPowerDataType | grep -A10 "Charge Information"

# Check battery health via powermetrics
sudo powermetrics --samplers battery -i 2000 -n 5
```

### 2. Recalibrate the battery

```bash
# Charge to 100% and keep plugged in for 2 hours
# Unplug and use until the Mac shuts down from low battery
# Leave off for 5 hours
# Charge uninterrupted to 100%
# This recalibrates the battery gauge
```

### 3. Reset the SMC

```bash
# Intel MacBooks:
# Shut down → Hold Shift+Control+Option+Power for 10 sec → Release

# This resets battery management, fan control, and power functions
```

### 4. Check for battery swelling

```bash
# If the trackpad is raised or the bottom case is bulging:
# STOP USING THE MAC IMMEDIATELY
# Contact Apple Support for battery replacement
# A swollen battery is a fire hazard
```

## Related Errors

- [Fan Error](macos-fan-error) — thermal management issues
- [Boot Error](macos-boot-error) — power-related boot failures
- [SSD Error](macos-ssd-error) — hardware health issues
