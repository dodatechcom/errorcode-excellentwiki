---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E win32kfull.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by win32kfull.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "system-thread-exception", "win32kfull", "graphics", "stop-0x1000007e"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E win32kfull.sys

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `win32kfull.sys` indicates the Win32k full-screen kernel driver encountered an unhandled exception in a system thread. This is commonly caused by GPU driver bugs or display subsystem corruption.

## Common Causes

- **GPU driver conflict with Win32k** — Display drivers cause exceptions in Win32k system threads.
- **Screen capture or overlay software** — Third-party tools hook into the display pipeline.
- **Corrupted win32kfull.sys** — The system file is damaged by disk errors.
- **Multi-monitor configuration issues** — Complex display setups cause Win32k exceptions.

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
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*OBS*" -or $_.Name -like "*capture*" -or $_.Name -like "*streaming*" } | Select-Object Name, Version
```

### Reduce Display Configuration

Disconnect extra monitors and test with a single display.

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

### Disable Hardware Acceleration

In browsers and GPU-accelerated applications, disable hardware acceleration to test.

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: win32kfull
IMAGE_NAME:  win32kfull.sys
```

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED ntfs.sys]({{< relref "/os/windows/bsod-system-thread-exception5" >}}) — NTFS thread exception
- [BSOD SYSTEM_SERVICE_EXCEPTION win32kfull.sys]({{< relref "/os/windows/bsod-system-service-exception3" >}}) — Win32k service exception
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED fltmgr.sys]({{< relref "/os/windows/bsod-system-thread-exception4" >}}) — Filter manager exception
