---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 win32kfull.sys Windows 11/10"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA stop code 0x50 caused by win32kfull.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "page-fault", "win32kfull", "graphics", "gui", "stop-0x50"]
weight: 5
---

# BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 win32kfull.sys (2nd variant)

The `PAGE_FAULT_IN_NONPAGED_AREA` stop code `0x50` with `win32kfull.sys` is a second variant indicating the Win32k graphics driver accessed invalid non-paged memory. This variant occurs during multi-window and multi-monitor GUI operations.

## Common Causes

- **Multi-monitor GPU driver issues** — Multiple display configurations cause Win32k to access invalid memory.
- **Screen recording or streaming software** — Applications hooking into the display pipeline cause corruption.
- **GPU driver corruption** — Display driver bugs cause Win32k to reference invalid pages.
- **Remote desktop software** — RDP and VNC tools interact with Win32k and cause memory issues.

## How to Fix

### Update GPU Driver

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Disconnect Additional Monitors

Test with a single display to identify multi-monitor issues.

### Remove Screen Recording Software

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*OBS*" -or $_.Name -like "*streaming*" -or $_.Name -like "*remote*" } | Select-Object Name, Version
```

### Disable Hardware Acceleration

In browsers and applications, disable hardware acceleration.

### Test RAM

```cmd
mdsched.exe
```

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

## Examples

```text
PAGE_FAULT_IN_NONPAGED_AREA (50)
Invalid system memory was referenced.

MODULE_NAME: win32kfull
IMAGE_NAME:  win32kfull.sys
```

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA win32kfull.sys]({{< relref "/os/windows/bsod-page-fault4" >}}) — Win32k first variant
- [BSOD SYSTEM_SERVICE_EXCEPTION win32kfull.sys]({{< relref "/os/windows/bsod-system-service-exception3" >}}) — Win32k service exception
- [BSOD KMODE_EXCEPTION_NOT_HANDLED win32kfull.sys]({{< relref "/os/windows/bsod-kmode-exception4" >}}) — Win32k kernel exception
