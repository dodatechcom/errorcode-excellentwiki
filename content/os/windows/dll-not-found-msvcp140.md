---
title: "[Solution] msvcp140.dll Not Found Fix"
description: "Fix 'msvcp140.dll is missing' error on Windows 10 and 11. Resolve missing Visual C++ standard library DLL with redistributable installs and system repairs."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
tags: ["dll", "msvcp140", "missing", "visual-cpp", "redistributable"]
weight: 5
---

# [Solution] msvcp140.dll Not Found Fix

This error occurs when a program tries to launch but cannot find `msvcp140.dll`. The full message reads:

> "The program can't start because msvcp140.dll is missing from your computer. Try reinstalling the program to fix this problem."

`msvcp140.dll` is part of the Microsoft Visual C++ 2015-2022 Redistributable. It contains the C++ Standard Library functions. This error is extremely common with games and applications built with Visual C++.

## Common Causes

1. **Visual C++ Redistributable not installed** — The package was never installed.
2. **Corrupted redistributable** — Existing installation is damaged.
3. **Antivirus quarantine** — Security software removed the DLL.
4. **32-bit vs 64-bit mismatch** — Wrong architecture redistributable installed.

## How to Fix

### Install Visual C++ Redistributable 2015-2022

```powershell
# x64 version
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait

# x86 version
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x86.exe" -OutFile "$env:TEMP\vc_redist.x86.exe"
Start-Process "$env:TEMP\vc_redist.x86.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Reinstall the Application

1. Uninstall the application from **Settings > Apps**.
2. Download a fresh copy from the official source.
3. Install and test.

### Check if DLL Exists

```powershell
Get-ChildItem -Path C:\ -Filter "msvcp140.dll" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName, Length, LastWriteTime
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Install Older Redistributable Versions

If the application requires an older version:

- [Visual C++ 2013 Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)
- [Visual C++ 2012 Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)

## Related Errors

- [vcruntime140.dll Not Found]({{< relref "/os/windows/dll-not-found-vcruntime140" >}}) — Missing VC++ runtime DLL
- [ucrtbase.dll Not Found]({{< relref "/os/windows/dll-not-found-ucrtbase" >}}) — Missing Universal C Runtime
- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point-not-found" >}}) — DLL exists but wrong version
