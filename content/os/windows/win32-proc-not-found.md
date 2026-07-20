---
title: "[Solution] Error 127 — PROC_NOT_FOUND Fix"
description: "Fix Windows Error Code (PROC_NOT_FOUND) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 127
---

# [Solution] Error 127 — PROC_NOT_FOUND Fix

Win32 error 127 (`ERROR_PROC_NOT_FOUND`) occurs when the specified procedure could not be found. This means a DLL was loaded successfully, but the requested function (procedure) does not exist within it.

## Description

The PROC_NOT_FOUND error is returned when `GetProcAddress` or a similar mechanism fails to locate a function within a loaded DLL. This commonly happens when an application calls an API function that does not exist in the installed version of a DLL, or when the function name is misspelled. The error code is `ERROR_PROC_NOT_FOUND` (value 127). The full message reads:

> "The specified procedure could not be found."

## Common Causes

1. The function name is misspelled or incorrect.
2. The DLL version does not contain the requested function.
3. A 32-bit application is calling a function exported only in the 64-bit DLL.
4. A Windows update changed the DLL exports.
5. The DLL was replaced with an incompatible version.
6. The function is provided by a different DLL than expected.

## Solutions

### Solution 1: Check the Function Name

Verify the function name matches exactly what the DLL exports:

```powershell
# List exported functions from a DLL
dumpbin /exports "C:\Path\To\dll" 2>$null | Select-String -Pattern "^\s+\d+\s+[A-F0-9]+\s+[A-F0-9]+\s+(\w+)"
```

Or use PowerShell to check the module:

```powershell
[System.Reflection.Assembly]::LoadFile("C:\Path\To\dll").ExportedTypes | Select-Object Name
```

### Solution 2: Update or Reinstall the DLL

Install the correct version of the DLL or its parent package:

```cmd
:: Reinstall Visual C++ Redistributable
winget install Microsoft.VCRedist.2015+.x64
winget install Microsoft.VCRedist.2015+.x86

:: Or reinstall DirectX
dxdiag
```

### Solution 3: Verify API Version Compatibility

Check that the API version your application expects matches the installed version:

```powershell
# Check the version of a system DLL
$f = Get-Item "C:\Windows\System32\kernel32.dll"
$f.VersionInfo.FileVersion
```

### Solution 4: Install the Correct Architecture

Ensure you have both 32-bit and 64-bit versions of the required DLL:

```cmd
:: Check which SysWOW64 has for 32-bit DLLs
dir C:\Windows\SysWOW64\dllname.dll
:: Check System32 for 64-bit DLLs
dir C:\Windows\System32\dllname.dll
```

### Solution 5: Use Dependency Walker

Use Dependency Walker or Dependencies (modern alternative) to inspect missing procedures:

```cmd
:: Run Dependencies tool
Dependencies.exe -chain "C:\Path\To\application.exe"
```

## Related Errors

- [Error 126 — MOD_NOT_FOUND]({{< relref "/os/windows/win32-mod-not-found" >}}) — The specified module could not be found
- [Error 11 — BAD_FORMAT]({{< relref "/os/windows/win32-bad-format" >}}) — Incorrect program format
- [Error 6 — INVALID_HANDLE]({{< relref "/os/windows/win32-invalid-handle" >}}) — The handle is invalid
