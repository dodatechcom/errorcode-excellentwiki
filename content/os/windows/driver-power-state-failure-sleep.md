---
title: "[Solution] Driver Power State Failure Sleep Wake Fix"
description: "Fix DRIVER_POWER_STATE_FAILURE blue screen when computer enters sleep or wakes up on Windows. Resolve driver sleep transition errors on Windows 10/11."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] Driver Power State Failure Sleep Wake Fix

The DRIVER_POWER_STATE_FAILURE blue screen occurs when a driver is in an inconsistent power state during sleep, hibernation, or wake transitions.

## Common Causes
- Network adapter driver not supporting modern standby
- GPU driver failing to complete power-down during sleep
- USB driver not waking properly from hibernation
- Intel Management Engine Interface driver issues
- Bluetooth driver blocking sleep transition

## How to Fix

### Solution 1: Disable Fast Startup

1. Open Control Panel > Power Options
2. Click Choose what the power buttons do
3. Click Change settings that are currently unavailable
4. Uncheck Turn on fast startup

### Solution 2: Update All Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate } | Sort-Object DriverDate -Descending | Select-Object DeviceName, DriverVersion, DriverDate -First 10
```

### Solution 3: Configure Power Management

```cmd
powercfg /a
powercfg /devicequery wake_armed
```

### Solution 4: Disable Hybrid Sleep

Open Power Options > Change plan settings > Change advanced power settings and disable Hybrid sleep under Sleep settings.

### Solution 5: Update BIOS

Download and install the latest BIOS update to fix power management bugs.

## Examples
```powershell
powercfg /a
powercfg /devicequery wake_armed
powercfg /lastwake
```
