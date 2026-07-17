---
title: "[Solution] BSOD SYSTEM_SERVICE_EXCEPTION — 0x3B win32kfull.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_SERVICE_EXCEPTION stop code 0x3B caused by win32kfull.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_SERVICE_EXCEPTION — 0x3B win32kfull.sys

The `SYSTEM_SERVICE_EXCEPTION` stop code `0x3B` with `win32kfull.sys` indicates the Win32k full-screen driver encountered an exception during a system service call. This driver manages Windows graphical user interface operations and is commonly involved in display-related crashes.

## Common Causes

- **GPU driver conflict with Win32k** — Display drivers interact with win32kfull.sys and cause exceptions during GUI operations.
- **Corrupted Windows graphical components** — Damaged system files in the Win32k subsystem.
- **Third-party overlay or screen capture software** — Software that hooks into the display pipeline causes exceptions.
- **Windows update compatibility** — An update introduces incompatibility with the Win32k driver.

## How to Fix

### Update GPU Drivers

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest driver from the GPU manufacturer's website.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Remove Screen Capture and Overlay Software

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*OBS*" -or $_.Name -like "*overlay*" -or $_.Name -like "*screen capture*" } | Select-Object Name, Version
```

Uninstall or update screen recording and overlay applications.

### Disable Hardware Acceleration Temporarily

In the application causing the crash (browser, game), disable hardware acceleration to test.

### Run System File Check in Safe Mode

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

### Check for Windows Updates

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -Install -AcceptAll
```

## Examples

```text
SYSTEM_SERVICE_EXCEPTION (3b)
An exception happened while executing a system service routine.

MODULE_NAME: win32kfull
IMAGE_NAME:  win32kfull.sys
```

## Related Errors

- [BSOD SYSTEM_SERVICE_EXCEPTION tcpip.sys]({{< relref "/os/windows/bsod-system-service-exception4" >}}) — TCP/IP service exception
- [BSOD KMODE_EXCEPTION_NOT_HANDLED win32kfull.sys]({{< relref "/os/windows/bsod-kmode-exception4" >}}) — Win32k kernel mode exception
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA win32kfull.sys]({{< relref "/os/windows/bsod-page-fault4" >}}) — Win32k page fault
