---
title: "[Solution] Access Violation Runtime Error — Read/Write Memory Error"
description: "Fix access violation runtime errors (read/write) on Windows 10/11. Resolve 0xC0000005 memory access crashes in applications."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Access Violation Runtime Error — Read/Write Memory Error

An access violation runtime error occurs when a program tries to read from or write to a memory address it does not have permission to access. The crash dialog shows:

> "Exception code: 0xC0000005 — Access violation reading location 0x00000000"

Or:

> "Exception code: 0xC0000005 — Access violation writing location 0xXXXXXXXX"

## What This Error Means

Access violations are the most common type of application crash on Windows. The CPU detects that a process tried to access memory outside its address space or in a protected region, and raises an exception. `0xC0000005` maps to `STATUS_ACCESS_VIOLATION`. The location `0x00000000` indicates a null pointer dereference (reading/writing through a NULL pointer).

## Common Causes

- Null pointer dereference (accessing memory at address 0x0)
- Use-after-free (accessing memory that has been freed)
- Buffer overrun corrupting pointers
- Dangling pointer to a destroyed object
- Memory-mapped file access beyond file size
- DEP blocking execution of data pages
- Third-party DLL corrupting application memory

## How to Fix

### Identify the Faulting Code

Check the crash address and module:

```powershell
# Enable crash dumps
New-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Name "DumpFolder" -Value "C:\CrashDumps"
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps" -Name "DumpType" -Value 2
```

Analyze the dump with WinDbg:

```
!analyze -v
!address @rcx
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Test RAM for Errors

```powershell
mdsched.exe
```

### Disable Antivirus Temporarily

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

Test the application. If it works, add an exclusion:

```powershell
Add-MpExclusion -Path "C:\Path\To\Application"
Set-MpPreference -DisableRealtimeMonitoring $false
```

### Reinstall the Application

1. Uninstall via **Settings > Apps**.
2. Delete leftover directories in `%APPDATA%` and `%LOCALAPPDATA%`.
3. Reinstall from the official source.

## Related Errors

- [Unhandled Exception]({{< relref "/os/windows/runtime-error-unhandled-exception" >}}) — Unhandled exceptions at crash address
- [Heap Corruption]({{< relref "/os/windows/runtime-error-heap-corruption" >}}) — Heap corruption causing crashes
- [Buffer Overrun]({{< relref "/os/windows/runtime-error-buffer-overrun" >}}) — Stack buffer overflow
