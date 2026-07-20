---
title: "[Solution] Error 126 — MOD_NOT_FOUND Fix"
description: "Fix Windows Error Code (MOD_NOT_FOUND) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 126
---

# [Solution] Error 126 — MOD_NOT_FOUND Fix

Win32 error 126 (`ERROR_MOD_NOT_FOUND`) occurs when the specified module could not be found. This typically means a DLL file that a program depends on is missing, corrupted, or not in the expected search path.

## Description

The MOD_NOT_FOUND error is returned when Windows attempts to load a dynamic-link library (DLL) or executable module and cannot locate it. This is one of the most common errors when launching applications, especially after software updates, driver changes, or system modifications. The error code is `ERROR_MOD_NOT_FOUND` (value 126). The full message reads:

> "The specified module could not be found."

## Common Causes

1. A required DLL file is missing from the system.
2. The DLL exists but is not in the application's search path.
3. A dependency of the DLL is itself missing.
4. The DLL file is corrupted or unreadable.
5. A 32-bit application is trying to load a 64-bit DLL or vice versa.
6. A recent Windows update removed or replaced a required DLL.

## Solutions

### Solution 1: Install the Missing DLL

Identify and install the required DLL. Many DLLs are provided by redistributable packages:

```powershell
# Check if the DLL exists anywhere on the system
Get-ChildItem C:\ -Filter "missing.dll" -Recurse -ErrorAction SilentlyContinue
```

Install the appropriate Visual C++ Redistributable:

```cmd
:: Download and install VC++ Redistributable
winget install Microsoft.VCRedist.2015+.x64
winget install Microsoft.VCRedist.2015+.x86
```

### Solution 2: Check the System PATH

Ensure the DLL directory is in the system PATH:

```powershell
# View current PATH
$env:PATH -split ";"

# Add a directory to PATH temporarily
$env:PATH += ";C:\Path\To\DLL"

# Add permanently
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\Path\To\DLL", "Machine")
```

### Solution 3: Run System File Checker

Repair corrupted or missing system DLLs:

```cmd
sfc /scannow
```

```cmd
:: If SFC finds issues, run DISM
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 4: Reinstall the Application

Reinstall the application that is missing the DLL:

```powershell
# Uninstall and reinstall via winget
winget uninstall "ApplicationName"
winget install "ApplicationName"
```

### Solution 5: Check DLL Architecture

Verify the DLL matches the application architecture (32-bit vs 64-bit):

```powershell
# Check if a DLL is 32-bit or 64-bit
$bytes = [System.IO.File]::ReadAllBytes("C:\Path\To\dll")
if ($bytes[0x80] -eq 0x01 -and $bytes[0x81] -eq 0x00) {
    Write-Host "DLL is 32-bit (x86)"
} elseif ($bytes[0x80] -eq 0x64 -and $bytes[0x81] -eq 0x86) {
    Write-Host "DLL is 64-bit (x64)"
}
```

## Related Errors

- [Error 127 — PROC_NOT_FOUND]({{< relref "/os/windows/win32-proc-not-found" >}}) — The specified procedure could not be found
- [Error 11 — BAD_FORMAT]({{< relref "/os/windows/win32-bad-format" >}}) — Incorrect program format
- [Error 2 — FILE_NOT_FOUND]({{< relref "/os/windows/win32-file-not-found" >}}) — The system cannot find the file
