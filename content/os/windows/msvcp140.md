---
title: "[Solution] msvcp140.dll Not Found — Fix C++ Standard Library Error"
description: "Fix 'msvcp140.dll not found' error on Windows 10 and 11. Install the Visual C++ Redistributable to resolve C++ standard library dependency failures."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# msvcp140.dll Not Found

The `msvcp140.dll not found` error occurs when an application requires the C++ Standard Library from Visual C++ 2015-2022 but the DLL is missing. The error reads:

> "The program can't start because msvcp140.dll is missing from your computer."

## What This Error Means

`msvcp140.dll` is the Microsoft C++ Standard Library DLL for Visual C++ 2015-2022. It provides implementations of the C++ Standard Template Library (STL) including `std::string`, `std::vector`, `std::map`, and other containers. Any application compiled with Visual C++ 2015 or later that uses the STL requires this DLL.

## Common Causes

- Visual C++ Redistributable not installed
- Application did not include the redistributable in its installer
- Antivirus quarantined the DLL
- Only one architecture version installed (32-bit or 64-bit)
- Corrupted redistributable installation

## How to Fix

### Install the Visual C++ Redistributable

```powershell
# Download and install both architectures
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait

Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x86.exe" -OutFile "$env:TEMP\vc_redist.x86.exe"
Start-Process "$env:TEMP\vc_redist.x86.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Check Which Version You Need

```powershell
# Check if the application is 32-bit or 64-bit
$exePath = "C:\Program Files\MyApp\app.exe"
$bytes = [System.IO.File]::ReadAllBytes($exePath)
$peOffset = [BitConverter]::ToInt32($bytes, 60)
$machineType = [BitConverter]::ToUInt16($bytes, $peOffset + 4)
if ($machineType -eq 0x014c) { "32-bit application" } else { "64-bit application" }
```

### Verify DLL Exists

```powershell
# Check both system directories
Get-ChildItem C:\Windows\System32\msvcp140.dll -ErrorAction SilentlyContinue
Get-ChildItem C:\Windows\SysWOW64\msvcp140.dll -ErrorAction SilentlyContinue
```

### Repair via DISM

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Related Errors

- [vcruntime140.dll Not Found]({{< relref "/os/windows/vcruntime140" >}}) — C runtime DLL missing (often co-occurs)
- [Missing DLL Error]({{< relref "/os/windows/dll-not-found" >}}) — Generic missing DLL errors
- [api-ms-win-crt-runtime-l1-1-0.dll Not Found]({{< relref "/os/windows/api-ms-win-crt" >}}) — Universal CRT dependency
