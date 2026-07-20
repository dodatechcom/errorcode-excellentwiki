---
title: "[Solution] Error 998 — NOACCESS Fix"
description: "Fix Windows Error Code (NOACCESS) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 998
---

# [Solution] Error 998 — NOACCESS Fix

Win32 error 998 (`ERROR_NOACCESS`) occurs when there is invalid access to a memory location. This error indicates that the application attempted to access memory in a way that violates the memory protection rules of the operating system.

## Description

The NOACCESS error is returned when a process tries to access memory that it does not have permission to read or write. This can occur due to memory corruption, buffer overflows, null pointer dereferences, or driver issues. The error code is `ERROR_NOACCESS` (value 998). The full message reads:

> "Invalid access to memory location."

## Common Causes

1. A null pointer dereference or wild pointer access.
2. Memory corruption from a previous buffer overflow.
3. A driver accesses invalid memory addresses.
4. The application tries to write to read-only memory.
5. A use-after-free bug accesses freed memory.
6. Faulty RAM hardware causes invalid memory accesses.

## Solutions

### Solution 1: Check Memory Access

Use Windows Memory Diagnostic to check for hardware issues:

```powershell
# Schedule memory diagnostic on next restart
Start-Process mdsched.exe -Verb RunAs
```

```cmd
:: Or run directly
mdsched.exe
```

### Solution 2: Update Drivers

Outdated or buggy drivers can cause invalid memory access:

```powershell
# Check for driver updates
pnputil /scan-devices

# List installed drivers
driverquery /fo table /nh
```

### Solution 3: Run Memory Diagnostic

Perform a detailed memory test:

```powershell
# Run Windows Memory Diagnostic
mdsched.exe /f /r

# Or use a more detailed test
Start-Process "mdsched.exe" -ArgumentList "/f /r" -Verb RunAs
```

### Solution 4: Check for Application Bugs

If a specific application causes the error, check for updates:

```powershell
# Check application version
Get-ItemProperty "C:\Path\To\app.exe" | Select-Object VersionInfo

# Update via package manager
winget upgrade "ApplicationName"
```

### Solution 5: Disable DEP for Specific Application

If the error is caused by Data Execution Prevention:

```cmd
:: Add application to DEP exception list (use with caution)
bcdedit /set nx OptIn
```

```powershell
# Check DEP settings
Get-Process | Where-Object { $_.ProcessName -eq "AppName" } | Select-Object ProcessName, Id
```

## Related Errors

- [Error 997 — IO_PENDING]({{< relref "/os/windows/win32-io-pending" >}}) — Overlapped I/O in progress
- [Error 999 — SWAPERROR]({{< relref "/os/windows/win32-swaperror" >}}) — Error performing inpage operation
- [Error 8 — NOT_ENOUGH_MEMORY]({{< relref "/os/windows/win32-not-enough-memory" >}}) — Not enough memory
