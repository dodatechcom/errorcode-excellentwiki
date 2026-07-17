---
title: "[Solution] DLL Dependency Error — A Dependency DLL Is Missing"
description: "Fix Windows DLL dependency errors when a program fails to load because a required dependency DLL is missing or not registered."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["dll", "dependency", "missing-dll", "load-library", "entry-point"]
weight: 5
---

# DLL Dependency Error — A Dependency DLL Is Missing

A DLL dependency error occurs when a program loads successfully but fails because one of the DLLs it depends on is missing, corrupted, or not registered. The error message typically reads:

> "The program can't start because [dependency.dll] is missing from your computer."

Or:

> "The application was unable to start correctly (0xc000007b)."

## What This Error Means

Every DLL can depend on other DLLs. When a program loads `myapp.dll`, that DLL may need `vcruntime140.dll`, `msvcp140.dll`, or other system DLLs. If any link in the dependency chain is broken, the program fails to load. This is distinct from a missing main DLL — the program's DLL exists, but one of *its* dependencies does not.

## Common Causes

- Missing Visual C++ Redistributable (most common cause)
- Mixing 32-bit and 64-bit DLLs
- Corrupted system DLL after a Windows update
- Antivirus quarantined a dependency DLL
- Incomplete application installation
- Outdated .NET Framework or other runtime

## How to Fix

### Install Visual C++ Redistributables

```powershell
# Download VC++ Redistributable 2015-2022 (both architectures)
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait

Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x86.exe" -OutFile "$env:TEMP\vc_redist.x86.exe"
Start-Process "$env:TEMP\vc_redist.x86.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

### Use Dependencies Tool to Inspect DLL Chain

Download the [Dependencies](https://github.com/lucasg/Dependencies) tool to visualize the full DLL dependency tree:

```powershell
# After installing Dependencies, run:
Dependencies.exe "C:\Path\To\program.exe"
```

This shows exactly which DLL is missing or cannot be found.

### Run System File Checker

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Reinstall the Application

```powershell
# Uninstall via Settings
Get-AppxPackage *AppName* | Remove-AppxPackage

# Clean leftover files
Remove-Item -Path "$env:APPDATA\AppName" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$env:LOCALAPPDATA\AppName" -Recurse -Force -ErrorAction SilentlyContinue
```

Then download and install the latest version from the official source.

## Related Errors

- [Missing DLL Error]({{< relref "/os/windows/dll-not-found" >}}) — The main DLL itself is missing
- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point" >}}) — DLL exists but exports the wrong version
- [vcruntime140.dll Not Found]({{< relref "/os/windows/vcruntime140" >}}) — Specific VC++ runtime missing
