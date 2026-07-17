---
title: "[Solution] vcruntime140.dll Not Found Fix"
description: "Fix 'vcruntime140.dll is missing' error on Windows 10 and 11. Resolve missing Visual C++ runtime DLL by installing the Visual C++ Redistributable package."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
weight: 5
---

# [Solution] vcruntime140.dll Not Found Fix

This error occurs when a program tries to launch but cannot find `vcruntime140.dll`. The full message reads:

> "The program can't start because vcruntime140.dll is missing from your computer. Try reinstalling the program to fix this problem."

`vcruntime140.dll` is part of the Microsoft Visual C++ 2015-2022 Redistributable. It provides essential runtime functions for applications built with Visual C++. This is one of the most common missing DLL errors on Windows.

## Common Causes

1. **Visual C++ Redistributable not installed** — The most common cause; the package was never installed.
2. **Corrupted redistributable installation** — The existing installation is damaged.
3. **Antivirus quarantine** — Security software falsely flagged and removed the DLL.
4. **32-bit vs 64-bit mismatch** — A 32-bit app needs the x86 redistributable, not x64.

## How to Fix

### Install Visual C++ Redistributable 2015-2022

Install both x64 and x86 versions:

```powershell
# Download VC++ Redistributable 2015-2022 (x64)
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait

# Download VC++ Redistributable 2015-2022 (x86)
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x86.exe" -OutFile "$env:TEMP\vc_redist.x86.exe"
Start-Process "$env:TEMP\vc_redist.x86.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Reinstall the Problematic Application

1. Open **Settings > Apps > Installed apps**.
2. Find the application and click **Uninstall**.
3. Download a fresh copy from the official source.
4. Install and test.

### Check if the DLL Exists on Your System

```powershell
Get-ChildItem -Path C:\ -Filter "vcruntime140.dll" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName, Length, LastWriteTime
```

If found, copy it to the application's installation directory.

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Antivirus Quarantine

If the DLL was quarantined, restore it from your antivirus quarantine or reinstall the redistributable after adding an exclusion.

## Related Errors

- [msvcp140.dll Not Found]({{< relref "/os/windows/dll-not-found-msvcp140" >}}) — Missing C++ standard library DLL
- [ucrtbase.dll Not Found]({{< relref "/os/windows/dll-not-found-ucrtbase" >}}) — Missing Universal C Runtime DLL
- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point-not-found" >}}) — DLL exists but wrong version
