---
title: "[Solution] api-ms-win-crt-runtime-l1-1-0.dll Not Found Fix"
description: "Fix 'api-ms-win-crt-runtime-l1-1-0.dll is missing' error on Windows 10 and 11. Resolve missing UCRT API set DLL with Windows Update and redistributable installs."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
weight: 5
---

# [Solution] api-ms-win-crt-runtime-l1-1-0.dll Not Found Fix

This error occurs when a program tries to launch but cannot find `api-ms-win-crt-runtime-l1-1-0.dll`. The full message reads:

> "The program can't start because api-ms-win-crt-runtime-l1-1-0.dll is missing from your computer. Try reinstalling the program to fix this problem."

This DLL is an API set (also called an API schema) that redirects to the Universal C Runtime (UCRT). It is part of Windows 10 and later but may be missing on older builds that have not been updated.

## Common Causes

1. **Windows not updated** — The API set requires a specific Windows version.
2. **Missing Universal C Runtime** — UCRT components not installed.
3. **Visual C++ Redistributable missing** — The redistributable includes UCRT components.
4. **Corrupted system files** — Damaged API set redirection.

## How to Fix

### Install All Windows Updates

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

### Install Visual C++ Redistributable

```powershell
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait

Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x86.exe" -OutFile "$env:TEMP\vc_redist.x86.exe"
Start-Process "$env:TEMP\vc_redist.x86.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Install KB2999226 Manually

1. Visit [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Search for **KB2999226**.
3. Download and install for your architecture.
4. Restart.

### Reinstall the Application

1. Uninstall from **Settings > Apps**.
2. Download a fresh copy from the official source.
3. Install and test.

## Related Errors

- [ucrtbase.dll Not Found]({{< relref "/os/windows/dll-not-found-ucrtbase" >}}) — Missing UCRT base DLL
- [vcruntime140.dll Not Found]({{< relref "/os/windows/dll-not-found-vcruntime140" >}}) — Missing VC++ runtime
- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point-not-found" >}}) — DLL exists but wrong version
