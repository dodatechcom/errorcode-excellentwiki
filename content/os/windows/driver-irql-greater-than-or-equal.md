---
title: "[Solution] DRIVER_IRQL_NOT_LESS_OR_EQUAL BSOD Fix"
description: "Fix Blue Screen DRIVER_IRQL_NOT_LESS_OR_EQUAL caused by accessing a memory address at too high an IRQL on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] DRIVER_IRQL_NOT_LESS_OR_EQUAL BSOD Fix

The DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen occurs when a driver attempts to access pageable memory at an elevated Interrupt Request Level (IRQL).

## Common Causes
- Network adapter driver accessing paged memory at DISPATCH_LEVEL
- Storage driver bug causing invalid memory access
- Third-party antivirus or firewall driver fault
- Corrupted driver binary on disk
- Outdated driver incompatible with current Windows version

## How to Fix

### Solution 1: Identify the Faulting Driver

Check the blue screen details for the driver name (usually in the format driver.sys).

### Solution 2: Update Network Drivers

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion
```

### Solution 3: Remove Third-Party Security Software

Temporarily uninstall third-party antivirus or firewall software that may have kernel-mode components.

### Solution 4: Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 5: Enable Driver Verifier

```cmd
verifier /standard /all
```

## Examples
```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion, Status
```
