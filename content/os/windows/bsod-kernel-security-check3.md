---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 win32kfull.sys Windows 11/10"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE stop code 0x139 caused by win32kfull.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "kernel-security", "win32kfull", "graphics", "stop-0x139"]
weight: 5
---

# BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 win32kfull.sys

The `KERNEL_SECURITY_CHECK_FAILURE` stop code `0x139` with `win32kfull.sys` indicates the Win32k full-screen kernel driver corrupted a critical kernel data structure. The kernel's security integrity check detected corruption in the graphics subsystem.

## Common Causes

- **GPU driver corrupting Win32k structures** — Display drivers interact with win32kfull.sys and corrupt kernel data.
- **Corrupted win32kfull.sys** — The system file is damaged by disk errors or malware.
- **Third-party overlay software** — Screen capture tools hook into Win32k and cause corruption.
- **Multi-monitor driver conflicts** — Multiple display adapters cause Win32k data structure corruption.

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

### Remove Overlay Software

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*overlay*" -or $_.Name -like "*capture*" } | Select-Object Name, Version
```

### Disable Hardware Acceleration

In GPU-accelerated applications, disable hardware acceleration to test.

### Test RAM

```cmd
mdsched.exe
```

### Check Windows Updates

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -Install -AcceptAll
```

## Examples

```text
KERNEL_SECURITY_CHECK_FAILURE (139)
A kernel security check failure has occurred.

MODULE_NAME: win32kfull
IMAGE_NAME:  win32kfull.sys
```

## Related Errors

- [BSOD KERNEL_SECURITY_CHECK_FAILURE]({{< relref "/os/windows/bsod-kernel-security-check-failure" >}}) — General kernel security failure
- [BSOD KERNEL_SECURITY_CHECK_FAILURE storport.sys]({{< relref "/os/windows/bsod-kernel-security-check2" >}}) — Storage port security failure
- [BSOD SYSTEM_SERVICE_EXCEPTION win32kfull.sys]({{< relref "/os/windows/bsod-system-service-exception3" >}}) — Win32k service exception
