---
title: "[Solution] ntdll.dll Error 0xc0000005 Fix"
description: "Fix ntdll.dll error 0xc0000005 (access violation) on Windows 10 and 11. Resolve crashes in the core Windows NT DLL with system repairs and application fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["system-error"]
tags: ["dll", "ntdll", "0xc0000005", "access-violation", "system-dll"]
weight: 5
---

# [Solution] ntdll.dll Error 0xc0000005 Fix

An error in `ntdll.dll` with code `0xc0000005` (access violation) means a program tried to access memory it is not allowed to use through the Windows NT Layer DLL. The error message typically reads:

> "The application was unable to start correctly (0xc0000005). Click OK to close the application."
> or
> "Exception code: 0xc0000005. Faulting module: ntdll.dll"

`ntdll.dll` is the lowest-level user-mode DLL in Windows, providing NT kernel interface functions. An access violation here often indicates a corrupted application, browser extensions, or system file damage.

## Common Causes

1. **Corrupted application** — The program has damaged files or configuration.
2. **Browser extension conflicts** — Browser add-ons causing ntdll.dll crashes.
3. **Corrupted Windows system files** — Damaged ntdll.dll or dependent files.
4. **Malware** — Malware injecting into the ntdll.dll address space.
5. **Faulty RAM** — Memory errors causing access violations.

## How to Fix

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Identify the Faulting Application

```powershell
Get-WinEvent -LogName Application | Where-Object { $_.Id -eq 1000 } | Select-Object -First 5 TimeCreated, Message | Format-List
```

Look for events mentioning `ntdll.dll` and note the faulting application name.

### Reinstall the Problematic Application

1. Uninstall from **Settings > Apps**.
2. Delete the application's data folders:
   ```powershell
   Get-ChildItem "$env:APPDATA" -Filter "*AppName*" -Directory | Remove-Item -Recurse -Force
   ```
3. Download and reinstall from the official source.

### Disable Browser Extensions

If the crash occurs in a web browser:

**Chrome:**
1. Open **Settings > Extensions**.
2. Toggle off all extensions.
3. Enable them one by one to find the culprit.

**Firefox:**
1. Open **about:addons**.
2. Disable all extensions.
3. Enable them one by one.

### Run Memory Diagnostics

```cmd
mdsched.exe
```

Select **Restart now and check for problems**.

### Scan for Malware

```powershell
Start-MpScan -ScanType FullScan
Start-MpScan -ScanType OfflineScan
```

### Run the Application in Compatibility Mode

1. Right-click the application shortcut.
2. Select **Properties > Compatibility**.
3. Check **Run this program in compatibility mode**.
4. Select an older Windows version and test.

## Related Errors

- [kernel32.dll Access Violation]({{< relref "/os/windows/dll-not-found-kernel32" >}}) — Core system DLL access violation
- [user32.dll Load Failed]({{< relref "/os/windows/dll-not-found-user32" >}}) — User interface DLL failure
- [DLL Dependency Error]({{< relref "/os/windows/dll-dependency-walker" >}}) — Missing DLL dependency
