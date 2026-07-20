---
title: "[Solution] BSOD ATTEMPTED_WRITE_TO_READONLY_MEMORY — Blue Screen Fix"
description: "Fix Windows Blue Screen ATTEMPTED_WRITE_TO_READONLY_MEMORY with these step-by-step solutions. Includes driver updates, hardware checks, and system file repairs."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 20
---

# [Solution] BSOD ATTEMPTED_WRITE_TO_READONLY_MEMORY — Blue Screen Fix

The `ATTEMPTED_WRITE_TO_READONLY_MEMORY` stop code indicates a driver attempted to write to read-only memory. This is a serious memory protection violation that can cause system instability.

## Description

This BSOD occurs when a kernel-mode driver tries to modify memory that has been marked as read-only. It is typically caused by buggy drivers, faulty hardware, or corrupted system files.

## Common Causes

1. Outdated or buggy device drivers
2. Faulty RAM modules
3. Corrupted Windows system files
4. Incompatible hardware
5. Malware infection

## Solutions

### Solution 1: Update Drivers

Update all device drivers, especially recently installed ones:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate -lt (Get-Date).AddYears(-2) } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Solution 2: Check for Faulty Hardware

Run hardware diagnostics:

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

Physically check RAM and other hardware components for damage or loose connections.

### Solution 3: Run System File Checker

Repair corrupted system files:

```cmd
sfc /scannow
```

Restart the computer after the scan completes and check if the issue persists.

## Related Errors

- [DRIVER_IRQL_NOT_LESS_OR_EQUAL](bsod-driver-irql-not-less-or-equal.md)
- [KMODE_EXCEPTION_NOT_HANDLED](bsod-kmode-exception-not-handled.md)
- [MEMORY_MANAGEMENT](bsod-memory-management.md)
