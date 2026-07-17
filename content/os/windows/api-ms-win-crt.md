---
title: "[Solution] api-ms-win-crt-runtime-l1-1-0.dll Not Found Fix"
description: "Fix 'api-ms-win-crt-runtime-l1-1-0.dll not found' error on Windows 10/11. Install the Universal C Runtime update to resolve the dependency."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["api-ms-win-crt", "universal-crt", "dll", "windows-update", "vc-runtime"]
weight: 5
---

# api-ms-win-crt-runtime-l1-1-0.dll Not Found

The `api-ms-win-crt-runtime-l1-1-0.dll not found` error occurs when an application requires the Universal C Runtime (UCRT) which is not installed. The error reads:

> "The program can't start because api-ms-win-crt-runtime-l1-1-0.dll is missing from your computer."

## What This Error Means

`api-ms-win-crt-runtime-l1-1-0.dll` is an API set that points to the Universal C Runtime, introduced in Windows 10 and available for Windows 7/8.1 via Windows Update. It is part of the C11 Standard Library implementation. Applications compiled with Visual C++ 2015 or later depend on this DLL for standard C functions like `printf`, `malloc`, and `memcpy`.

## Common Causes

- Windows 7 or 8.1 without the required Windows Update (KB2999226)
- Visual C++ Redistributable 2015 not installed
- Windows Update failed to install the Universal C Runtime
- Corrupted Windows Update components
- Running on an unsupported or unpatched Windows version

## How to Fix

### Install Windows Update KB2999226 (Windows 7/8.1)

```powershell
# Check if the update is installed
Get-HotFix -Id KB2999226 -ErrorAction SilentlyContinue

# Download and install manually
# Visit https://support.microsoft.com/en-us/topic/update-for-universal-c-runtime-in-windows-c0514201-7fe6-95a3-b0a5-287930f3560c
```

### Install the Visual C++ Redistributable

```powershell
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Run Windows Update

```powershell
# Check for and install all pending updates
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate
Install-WindowsUpdate -AcceptAll
```

### Verify UCRT Installation

```powershell
# Check if ucrtbase.dll exists (the actual runtime)
Test-Path "C:\Windows\System32\ucrtbase.dll"

# Check the API set DLL
Test-Path "C:\Windows\System32\api-ms-win-crt-runtime-l1-1-0.dll"
```

### Manually Copy UCRT DLLs

```powershell
# UCRT files are in the Windows Kit
Copy-Item "C:\Program Files (x86)\Windows Kits\10\bin\10.0.*\x64\ucrt\ucrtbase.dll" "C:\Windows\System32\" -Force
```

## Related Errors

- [vcruntime140.dll Not Found]({{< relref "/os/windows/vcruntime140" >}}) — VC++ 2015-2022 runtime missing
- [msvcp140.dll Not Found]({{< relref "/os/windows/msvcp140" >}}) — C++ standard library DLL missing
- [Missing DLL Error]({{< relref "/os/windows/dll-not-found" >}}) — Generic missing DLL errors
