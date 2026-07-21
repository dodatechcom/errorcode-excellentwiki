---
title: "[Solution] NTSTATUS STATUS_ASSERTION_FAILURE Fix"
description: "Fix NTSTATUS STATUS_ASSERTION_FAILURE error on Windows when a kernel-mode driver assertion check fails during execution."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] NTSTATUS STATUS_ASSERTION_FAILURE Fix

The NTSTATUS STATUS_ASSERTION_FAILURE (0xC0000205) error indicates a kernel-mode assertion check has failed. This is a defensive check in driver code that detects an impossible or invalid state and intentionally halts the system.

## Common Causes
- Bug in a third-party kernel-mode driver
- Incompatible driver interaction with the Windows kernel
- Corrupted driver binary from disk errors or malware
- Race condition in a multi-threaded driver
- Driver attempting invalid memory access patterns

## How to Fix

### Solution 1: Identify the Faulting Driver

Check the minidump file for the assertion failure details. Review C:\Windows\Minidump\ for recent dump files and analyze with WinDbg.

### Solution 2: Update All Drivers

Open Device Manager and update all device drivers, focusing on recently installed or updated ones.

### Solution 3: Enable Driver Verifier

```cmd
verifier /standard /all
```

Restart and reproduce the issue to identify the specific driver.

### Solution 4: Check for Windows Updates

Install all available Windows updates as they may contain fixes for kernel-mode driver issues.

### Solution 5: Roll Back Recent Driver Changes

```powershell
pnputil /enum-drivers
```

Use the published name to delete the problematic driver package.

## Examples
```powershell
Get-WindowsDriver -Online | Where-Object { $_.ClassName -eq 'System' } | Sort-Object Date -Descending | Select-Object -First 5
```
