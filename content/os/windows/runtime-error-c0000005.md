---
title: "[Solution] Runtime Error 0xC0000005 Access Violation Fix"
description: "Fix Windows runtime error 0xC0000005 (Access Violation) on Windows 10 and 11. Run SFC scan, check RAM, reinstall apps, and update drivers to resolve crash issues."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 5
---

# [Solution] Runtime Error 0xC0000005 Access Violation Fix

Runtime error 0xC0000005 is an Access Violation that occurs when a program attempts to read, write, or execute memory that it doesn't have permission to access. The application crashes immediately or shortly after launch.

This error affects both Windows 10 and 11 and is one of the most common application crash errors. It maps to `STATUS_ACCESS_VIOLATION` in the Windows NT status codes and can affect any program — from system utilities to games and professional software.

## Description

The full error message typically reads:

> "The application was unable to start correctly (0xC0000005). Click OK to close the application."

Or in a crash dialog:

> "Exception code: 0xC0000005 — Access violation reading location 0xXXXXXXXX."

A process attempted to access a memory address that is either unmapped, protected, or outside its allowed address space.

## Common Causes

- **Corrupted application files** — The program's executable or DLLs are damaged.
- **DLL conflicts or corruption** — Missing, outdated, or conflicting shared libraries.
- **Faulty RAM** — Memory errors cause random access violations across applications.
- **DEP (Data Execution Prevention)** — System security feature blocking a program's memory operations.

## How to Fix

### Run System File Checker

```cmd
sfc /scannow
```

If SFC reports corruption it cannot fix:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check and Test RAM

**Run Windows Memory Diagnostic:**

1. Press `Win + R`, type `mdsched.exe`, press Enter.
2. Select **Restart now and check for problems**.

**Check results after reboot:**

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -eq "Microsoft-Windows-MemoryDiagnostics-Results" } | Select-Object -First 1 Message
```

**Use MemTest86 for comprehensive testing:**

1. Download from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB drive.
3. Boot from USB and run at least 4 passes.
4. Any errors indicate faulty memory modules that need replacement.

### Reinstall the Problematic Application

1. Open **Settings > Apps > Installed apps**.
2. Find the application and click **Uninstall**.
3. Remove leftover files:

```powershell
Remove-Item -Path "$env:APPDATA\AppName" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$env:LOCALAPPDATA\AppName" -Recurse -Force -ErrorAction SilentlyContinue
```

4. Download and reinstall from the official source.

### Add the Application to DEP Exclusion List

Data Execution Prevention can sometimes block legitimate applications:

1. Press `Win + R`, type `sysdm.cpl`, press Enter.
2. Go to the **Advanced** tab.
3. Under **Performance**, click **Settings**.
4. Go to the **Data Execution Prevention** tab.
5. Select **Turn on DEP for all programs and services except those I select**.
6. Click **Add** and browse to the application's `.exe` file.
7. Click **Apply** and **OK**.

### Reinstall Visual C++ Redistributables

Many applications depend on the Visual C++ Redistributable:

```powershell
# Download VC++ Redistributables (2015-2022 combined)
Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process "$env:TEMP\vc_redist.x64.exe" -ArgumentList "/install /quiet /norestart" -Wait
```

Download all commonly needed versions from [Microsoft's website](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).

### Update or Reinstall Drivers

Outdated GPU and audio drivers can cause access violations:

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

**Roll back a recently updated driver:**

1. Open **Device Manager** (`Win + X` > Device Manager).
2. Expand the relevant device category.
3. Right-click the device and select **Properties**.
4. Go to the **Driver** tab and click **Roll Back Driver**.

### Disable Antivirus Temporarily

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

Test the application. If it works, add the application to the exclusion list:

```powershell
Add-MpExclusion -Path "C:\Path\To\Application"
```

Re-enable antivirus:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
```

## Examples

This error commonly occurs in these scenarios:

- **Application crashes on launch** — The program fails immediately with an error dialog.
- **Game crashes during gameplay** — Especially with mods, overlays, or outdated GPU drivers.
- **Office application errors** — Microsoft Office apps crashing on specific operations.
- **Browser crashes** — Web browsers crashing due to plugin or extension conflicts.

## Related Errors

- [Missing DLL Error]({{< relref "/os/windows/dll-not-found" >}}) — DLL file missing from the system
- [DLL Entry Point Not Found]({{< relref "/os/windows/dll-entry-point" >}}) — DLL exists but wrong version
- [Application Error Event ID 1000]({{< relref "/os/windows/event-1000" >}}) — Application crash logs with access violation details
- [Disk Full Error]({{< relref "/os/windows/disk-full" >}}) — Insufficient disk space can cause memory mapping failures
