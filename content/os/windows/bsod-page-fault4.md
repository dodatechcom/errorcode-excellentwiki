---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 win32kfull.sys Windows 11/10"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA stop code 0x50 caused by win32kfull.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 win32kfull.sys

The `PAGE_FAULT_IN_NONPAGED_AREA` stop code `0x50` with `win32kfull.sys` indicates the Win32k full-screen kernel driver attempted to access an invalid non-paged memory page. This is a graphics subsystem crash caused by GPU driver bugs or display subsystem corruption.

## Common Causes

- **GPU driver accessing invalid memory** — Display drivers interact with win32kfull.sys and access bad memory.
- **Corrupted win32kfull.sys** — The Win32k system file is damaged.
- **Screen overlay software** — Third-party overlays and capture software hook into the display pipeline.
- **Display resolution or multi-monitor issues** — Multi-monitor configurations cause memory access errors.

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

### Disable Screen Overlays

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*overlay*" -or $_.Name -like "*capture*" -or $_.Name -like "*streaming*" } | Select-Object Name, Version
```

### Reduce Display Resolution Temporarily

Change to a lower resolution to test if the issue is resolution-related.

### Disable Hardware Acceleration

In browsers and applications, disable hardware acceleration to test.

### Test RAM

```cmd
mdsched.exe
```

Memory corruption can cause win32k to reference invalid pages.

## Examples

```text
PAGE_FAULT_IN_NONPAGED_AREA (50)
Invalid system memory was referenced.

MODULE_NAME: win32kfull
IMAGE_NAME:  win32kfull.sys
```

## Related Errors

- [BSOD SYSTEM_SERVICE_EXCEPTION win32kfull.sys]({{< relref "/os/windows/bsod-system-service-exception3" >}}) — Win32k service exception
- [BSOD KMODE_EXCEPTION_NOT_HANDLED win32kfull.sys]({{< relref "/os/windows/bsod-kmode-exception4" >}}) — Win32k kernel exception
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntfs.sys]({{< relref "/os/windows/bsod-page-fault-in-npaged" >}}) — NTFS page fault
