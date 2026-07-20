---
title: "[Solution] BSOD APC_INDEX_MISMATCH — Blue Screen Fix"
description: "Fix Windows Blue Screen APC_INDEX_MISMATCH with these step-by-step solutions. Includes driver updates, audio driver fixes, and system diagnostics."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 24
---

# [Solution] BSOD APC_INDEX_MISMATCH — Blue Screen Fix

The `APC_INDEX_MISMATCH` stop code indicates an Asynchronous Procedure Call (APC) index mismatch in the kernel. This is commonly caused by audio or input device drivers.

## Description

This BSOD typically occurs when a driver returns the wrong APC index, causing a kernel synchronization error. It is most frequently triggered by audio drivers, especially those from Realtek, but can also be caused by other peripheral drivers.

## Common Causes

1. Outdated or corrupted audio drivers
2. Realtek audio driver conflicts
3. Faulty audio hardware
4. Windows update breaking audio drivers
5. Third-party audio software conflicts

## Solutions

### Solution 1: Update Audio Drivers

Update your audio drivers from the motherboard manufacturer's website:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceName -like "*Audio*" -or $_.DeviceName -like "*Realtek*" } | Select-Object DeviceName, DriverVersion, DriverDate
```

### Solution 2: Roll Back Audio Driver

If the issue started after a driver update:

1. Open Device Manager
2. Expand Sound, video and game controllers
3. Right-click your audio device
4. Select Properties > Driver tab
5. Click "Roll Back Driver"

### Solution 3: Run System File Checker

Repair corrupted system files:

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

## Related Errors

- [DRIVER_IRQL_NOT_LESS_OR_EQUAL](bsod-driver-irql-not-less-or-equal.md)
- [KMODE_EXCEPTION_NOT_HANDLED](bsod-kmode-exception-not-handled.md)
- [SYSTEM_SERVICE_EXCEPTION](bsod-system-service-exception.md)
