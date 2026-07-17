---
title: "[Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED — 0x1E win32kfull.sys Windows 11/10"
description: "Fix Blue Screen KMODE_EXCEPTION_NOT_HANDLED stop code 0x1E caused by win32kfull.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD KMODE_EXCEPTION_NOT_HANDLED — 0x1E win32kfull.sys

The `KMODE_EXCEPTION_NOT_HANDLED` stop code `0x1E` with `win32kfull.sys` indicates the Win32k full-screen kernel driver encountered an unhandled exception in kernel mode. This driver manages Windows graphical operations and is commonly involved in display and GUI-related crashes.

## Common Causes

- **GPU driver conflict** — Display drivers interact with win32kfull.sys and cause kernel exceptions.
- **Screen capture or overlay software** — Third-party tools that hook into the display pipeline cause exceptions.
- **Corrupted win32kfull.sys** — The system file is damaged by disk errors or failed updates.
- **Multi-monitor configuration issues** — Complex display setups cause memory access errors.

## How to Fix

### Update GPU Drivers

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Remove Screen Capture Software

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*OBS*" -or $_.Name -like "*capture*" -or $_.Name -like "*overlay*" } | Select-Object Name, Version
```

### Reduce Display Complexity

Disconnect extra monitors and run with a single display to test.

### Disable Hardware Acceleration

In browsers and GPU-accelerated applications, disable hardware acceleration.

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

## Examples

```text
KMODE_EXCEPTION_NOT_HANDLED (1e)
An unhandled kernel exception has occurred.

MODULE_NAME: win32kfull
IMAGE_NAME:  win32kfull.sys
```

## Related Errors

- [BSOD SYSTEM_SERVICE_EXCEPTION win32kfull.sys]({{< relref "/os/windows/bsod-system-service-exception3" >}}) — Win32k service exception
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA win32kfull.sys]({{< relref "/os/windows/bsod-page-fault4" >}}) — Win32k page fault
- [BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/os/windows/bsod-kmode-exception3" >}}) — TCP/IP kernel exception
