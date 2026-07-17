---
title: "[Solution] ucrtbase.dll Not Found Fix"
description: "Fix 'ucrtbase.dll is missing' error on Windows 10 and 11. Resolve missing Universal C Runtime DLL with Windows Update, KB installs, and system repairs."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
tags: ["dll", "ucrtbase", "missing", "universal-c-runtime", "ucrt"]
weight: 5
---

# [Solution] ucrtbase.dll Not Found Fix

This error occurs when a program tries to launch but cannot find `ucrtbase.dll`. The full message reads:

> "The program can't start because ucrtbase.dll is missing from your computer. Try reinstalling the program to fix this problem."

`ucrtbase.dll` is the Universal C Runtime (UCRT) component that provides standard C library functions. It is delivered through Windows Update and the Visual C++ Redistributable. This error typically appears on older Windows 10 builds that have not been updated.

## Common Causes

1. **Windows not updated** — The UCRT was added via Windows Update and may not be installed on older builds.
2. **Corrupted UCRT installation** — The existing UCRT files are damaged.
3. **Visual C++ Redistributable missing** — The redistributable includes UCRT components.
4. **Antivirus quarantine** — Security software removed the DLL.

## How to Fix

### Install Windows Updates

The UCRT is delivered via Windows Update. Install all pending updates:

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

Or manually via **Settings > Windows Update > Check for updates**.

### Install Visual C++ Redistributable

```powershell
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Install the KB2999226 Update

For older Windows 10 builds, install the Universal C Runtime update manually:

1. Visit [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
2. Search for **KB2999226**.
3. Download the correct version for your system.
4. Install and restart.

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check if DLL Exists

```powershell
Get-ChildItem -Path C:\Windows\System32 -Filter "ucrtbase.dll" -ErrorAction SilentlyContinue | Select-Object FullName, Length, LastWriteTime
```

## Related Errors

- [vcruntime140.dll Not Found]({{< relref "/os/windows/dll-not-found-vcruntime140" >}}) — Missing VC++ runtime
- [api-ms-win-crt-runtime-l1-1-0.dll Not Found]({{< relref "/os/windows/dll-not-found-api-ms-win-crt" >}}) — Related UCRT API set
- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point-not-found" >}}) — DLL exists but wrong version
