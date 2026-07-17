---
title: "[Solution] vcruntime140.dll Not Found — Fix VC++ Runtime Error"
description: "Fix 'vcruntime140.dll not found' error on Windows 10 and 11. Install the Visual C++ Redistributable to resolve application startup failures."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["vcruntime140", "dll", "visual-cpp", "redistributable", "runtime"]
weight: 5
---

# vcruntime140.dll Not Found

The `vcruntime140.dll not found` error occurs when an application built with Visual C++ 2015-2022 cannot find the required Visual C++ runtime DLL. The full error reads:

> "The program can't start because vcruntime140.dll is missing from your computer."

## What This Error Means

`vcruntime140.dll` is part of the Microsoft Visual C++ 2015-2022 Redistributable. It contains essential C runtime functions that compiled applications depend on. The DLL is not included with Windows and must be installed separately by the application installer or manually by the user.

## Common Causes

- Visual C++ Redistributable not installed
- Application installer did not include the redistributable
- DLL was removed by antivirus or disk cleanup
- 32-bit application requires 32-bit version but only 64-bit is installed
- Corrupted redistributable installation

## How to Fix

### Install the Visual C++ Redistributable

```powershell
# Download and install x64 version
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait

# Download and install x86 version (for 32-bit apps)
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x86.exe" -OutFile "$env:TEMP\vc_redist.x86.exe"
Start-Process "$env:TEMP\vc_redist.x86.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Verify Installation

```powershell
# Check if the DLL exists
Test-Path "C:\Windows\System32\vcruntime140.dll"
Test-Path "C:\Windows\SysWOW64\vcruntime140.dll"

# Check installed redistributables
Get-ItemProperty HKLM:\SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64 -ErrorAction SilentlyContinue
```

### Copy DLL to Application Directory

If the redistributable cannot be installed globally, copy `vcruntime140.dll` to the application's installation directory.

## Related Errors

- [Missing DLL Error]({{< relref "/os/windows/dll-not-found" >}}) — Generic missing DLL errors
- [msvcp140.dll Not Found]({{< relref "/os/windows/msvcp140" >}}) — Related C++ standard library DLL
- [api-ms-win-crt-runtime-l1-1-0.dll Not Found]({{< relref "/os/windows/api-ms-win-crt" >}}) — Universal CRT dependency
