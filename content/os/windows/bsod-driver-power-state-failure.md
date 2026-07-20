---
title: "[Solution] BSOD DRIVER_POWER_STATE_FAILURE — Blue Screen Fix"
description: "Fix Windows Blue Screen DRIVER_POWER_STATE_FAILURE with these step-by-step solutions. Includes driver updates, registry fixes, and diagnostic commands."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 17
---

# [Solution] BSOD DRIVER_POWER_STATE_FAILURE — Blue Screen Fix

The `DRIVER_POWER_STATE_FAILURE` stop code indicates a driver is in an inconsistent power state. This typically occurs when the system transitions between power states (sleep, hibernate, shutdown) and a driver fails to respond correctly.

## Description

This BSOD is commonly triggered by outdated drivers, especially those for network adapters, graphics cards, or storage controllers. Fast Startup and aggressive power management settings can also contribute to this issue.

## Common Causes

1. Outdated or incompatible drivers
2. Fast Startup causing driver conflicts
3. Faulty power supply unit
4. Aggressive power management settings
5. Incompatible hardware after Windows update

## Solutions

### Solution 1: Disable Fast Startup

Fast Startup can cause driver state conflicts:

```cmd
powercfg /h off
```

Or disable via Control Panel > Power Options > Choose what the power buttons do > Change settings currently unavailable > Uncheck "Turn on fast startup."

### Solution 2: Update Drivers

Update all device drivers, especially network and storage:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate -lt (Get-Date).AddYears(-2) } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Solution 3: Check Power Settings

Reset power plan to defaults:

```cmd
powercfg /restoredefaultschemes
```

## Related Errors

- [DRIVER_IRQL_NOT_LESS_OR_EQUAL](bsod-driver-irql-not-less-or-equal.md)
- [SYSTEM_SERVICE_EXCEPTION](bsod-system-service-exception.md)
- [DPC_WATCHDOG_VIOLATION](bsod-dpc-watchdog-violation.md)
