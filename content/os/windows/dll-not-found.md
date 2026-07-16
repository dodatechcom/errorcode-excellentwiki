---
title: "[Solution] The Program Can't Start Because X.dll Is Missing Fix"
description: "Fix 'The program can't start because X.dll is missing' error on Windows 10 and 11. Reinstall the application, restore DLL files, and run system file checks."
platforms: ["windows"]
severities: ["error"]
error_types: ["dll-error"]
tags: ["dll", "missing-dll", "application-error", "vcruntime", "msvcp"]
weight: 5
---

# [Solution] The Program Can't Start Because X.dll Is Missing Fix

This error occurs when a program tries to launch but cannot find a required DLL (Dynamic Link Library) file. The full message reads:

> "The program can't start because [filename].dll is missing from your computer. Try reinstalling the program to fix this problem."

This error affects both Windows 10 and 11 and can appear with any DLL file — common ones include `vcruntime140.dll`, `msvcp140.dll`, `msvcr100.dll`, `d3dx9_43.dll`, `xinput1_3.dll`, or `api-ms-win-crt-runtime-l1-1-0.dll`.

DLL files are shared libraries that multiple programs use. When a DLL is missing, corrupted, or the wrong version, dependent programs cannot load and fail at startup.

## Common Causes

- **Missing Visual C++ Redistributable** — The most common cause. Applications built with Visual C++ require the redistributable package to be installed.
- **Corrupted or deleted DLL file** — Antivirus quarantine, disk cleanup, or accidental deletion removed the DLL.
- **Application not installed properly** — Incomplete installation didn't copy all required files.
- **Wrong DLL version** — A 32-bit application needs 32-bit DLLs, or vice versa.

## How to Fix

### Install the Visual C++ Redistributable

Most "missing DLL" errors are caused by a missing Visual C++ Redistributable. Install both x64 and x86 versions:

```powershell
# Download VC++ Redistributable 2015-2022 (x64)
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait

# Download VC++ Redistributable 2015-2022 (x86)
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x86.exe" -OutFile "$env:TEMP\vc_redist.x86.exe"
Start-Process "$env:TEMP\vc_redist.x86.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

Also install older versions if needed:
- [Visual C++ 2013 Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)
- [Visual C++ 2012 Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)
- [Visual C++ 2010 Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=26999)
- [Visual C++ 2008 Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=26368)

### Reinstall the Problematic Application

1. Open **Settings > Apps > Installed apps**.
2. Find the application and click **Uninstall**.
3. Download a fresh copy from the official source.
4. Install and test.

### Check What Program Needs the DLL

Identify which program is trying to use the missing DLL:

```powershell
Get-WmiObject Win32_Process | Where-Object { $_.CommandLine -like "*missing_dll_name*" } | Select-Object Name, ProcessId, CommandLine | Format-Table -AutoSize
```

Or check the Windows Event Log for application errors that reference the DLL:

```powershell
Get-WinEvent -LogName Application | Where-Object { $_.Message -like "*missing_dll_name*" } | Select-Object -First 5 TimeCreated, Message | Format-List
```

### Restore the DLL from System File Checker

```cmd
sfc /scannow
```

If SFC doesn't fix it, run DISM first:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Register the DLL

Some DLLs need to be registered with the system:

```cmd
regsvr32 "C:\Path\To\filename.dll"
```

**Note**: Not all DLLs can be registered this way. Only COM DLLs support `regsvr32`. If you get an error, the DLL does not need to be registered.

### Check the Application's Runtime Directory

The DLL might exist on your system but not in the application's folder:

1. Find the missing DLL on your system:

```powershell
Get-ChildItem -Path C:\ -Filter "filename.dll" -Recurse -ErrorAction SilentlyContinue | Select-Object FullName, Length, LastWriteTime
```

2. Copy the DLL to the application's installation directory.

### Install DirectX for Gaming DLL Errors

Missing DirectX DLLs (like `d3dx9_43.dll`, `d3d11.dll`, `xinput1_3.dll`) are common with games:

1. Download the [DirectX End-User Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=35) from Microsoft.
2. Run the installer.
3. Restart your computer.

## Examples

This error commonly occurs in these scenarios:

- **After a fresh Windows install** — The Visual C++ Redistributable is not included with Windows and must be installed manually.
- **When running old games** — Games need specific DirectX or Visual C++ versions that aren't pre-installed.
- **After antivirus quarantine** — Antivirus falsely flags a DLL as malicious and removes it.
- **With portable applications** — Portable apps that don't include their required DLLs in the package.

## Related Errors

- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point" >}}) — DLL exists but is the wrong version
- [Access Violation 0xC0000005]({{< relref "/os/windows/runtime-error-c0000005" >}}) — Memory access errors from corrupted DLLs
- [Application Error Event ID 1000]({{< relref "/os/windows/event-1000" >}}) — Application crash logs referencing missing DLLs
