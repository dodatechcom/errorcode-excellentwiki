---
title: "[Solution] General Protection Fault (GPF) in Windows"
description: "Fix General Protection Fault (GPF) errors on Windows. Resolve privilege level violations, segment limit violations, and memory access GPFs."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# General Protection Fault (GPF) in Windows

A General Protection Fault (GPF) occurs when a program violates the processor's protection rules. The crash shows:

> "Exception code: 0xC0000005 — Access violation"

Or in 16-bit applications:

> "This program has performed an illegal operation and will be shut down."

## What This Error Means

A General Protection Fault is a CPU exception raised when a program tries to access a memory segment it does not have permission to use, accesses memory beyond a segment limit, or performs a privileged operation from user mode. In modern Windows (32-bit and 64-bit), GPFs manifest as access violations (`0xC0000005`). In legacy 16-bit applications running under NTVDM, GPFs appear in their original form.

## Common Causes

- 16-bit application running on 64-bit Windows (NTVDM not available)
- Legacy application with 16-bit components on modern Windows
- Corrupted code segment in a 16-bit application
- Memory-mapped I/O access beyond hardware limits
- Driver accessing invalid memory segments
- Third-party DLL hooking privileged operations

## How to Fix

### For 16-bit Applications

16-bit applications cannot run on 64-bit Windows. Options:

```powershell
# Check if running 64-bit Windows
[Environment]::Is64BitOperatingSystem  # True = cannot run 16-bit apps

# Check Windows version
[System.Environment]::OSVersion.Version
```

**Solutions:**

- Use a virtual machine with 32-bit Windows XP or Windows 7
- Use DOSBox for DOS applications
- Contact the vendor for a 64-bit update

### Run in Compatibility Mode (32-bit Windows only)

1. Right-click the application > **Properties**.
2. Go to the **Compatibility** tab.
3. Check **Run this program in compatibility mode for**.
4. Select **Windows XP (Service Pack 3)** or **Windows 7**.
5. Check **Run as administrator**.

### Check for Driver Issues

```powershell
# Check for driver errors
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Use NTVDM for 16-bit Applications (32-bit Windows only)

```cmd
:: Enable NTVDM if disabled
:: Open Registry Editor
:: Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WOW
:: Set Disallowed = 0
:: Restart computer
```

## Related Errors

- [Access Violation 0xC0000005]({{< relref "/os/windows/runtime-error-c0000005" >}}) — Modern access violation errors
- [Unhandled Exception]({{< relref "/os/windows/runtime-error-unhandled-exception" >}}) — Unhandled exceptions at crash address
- [kernel32.dll Error]({{< relref "/os/windows/kernel32-dll" >}}) — Core system DLL crashes
