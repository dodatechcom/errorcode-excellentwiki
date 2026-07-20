---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — Blue Screen Fix"
description: "Fix Windows Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED with these step-by-step solutions. Includes driver updates, registry fixes, and diagnostic commands."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 16
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — Blue Screen Fix

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code indicates a system thread generated an exception that the error handler did not catch. This often points to a driver issue or corrupted system files.

## Description

This BSOD occurs when a kernel-mode thread encounters an unhandled exception during execution. It is commonly triggered by incompatible drivers, corrupted Windows updates, or hardware failures.

## Common Causes

1. Incompatible or outdated device drivers
2. Corrupted Windows system files
3. Faulty hardware components
4. Incomplete Windows updates
5. Malware infection

## Solutions

### Solution 1: Boot into Safe Mode

Access Safe Mode to troubleshoot without problematic drivers:

1. Restart the computer three times during boot to trigger Recovery
2. Navigate to Troubleshoot > Advanced options > Startup Settings
3. Click Restart and press F4 for Safe Mode or F5 for Safe Mode with Networking

### Solution 2: Update Drivers

Check and update problematic drivers:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate -lt (Get-Date).AddYears(-2) } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download and install the latest drivers from the hardware manufacturer's website.

### Solution 3: Run System File Checker

Repair corrupted system files:

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

## Related Errors

- [KMODE_EXCEPTION_NOT_HANDLED](bsod-kmode-exception-not-handled.md)
- [SYSTEM_SERVICE_EXCEPTION](bsod-system-service-exception.md)
- [DRIVER_IRQL_NOT_LESS_OR_EQUAL](bsod-driver-irql-not-less-or-equal.md)
