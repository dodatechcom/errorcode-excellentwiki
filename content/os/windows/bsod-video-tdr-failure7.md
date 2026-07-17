---
title: "[Solution] BSOD VIDEO_TDR_FAILURE — 0x116 igdkmd64.sys Windows 11/10"
description: "Fix Blue Screen VIDEO_TDR_FAILURE stop code 0x116 caused by igdkmd64.sys Intel GPU driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD VIDEO_TDR_FAILURE — 0x116 igdkmd64.sys

The `VIDEO_TDR_FAILURE` stop code `0x116` with `igdkmd64.sys` indicates the Intel Graphics Kernel Mode Driver failed to respond to a TDR reset. The Intel integrated GPU driver encountered a timeout during display operations.

## Common Causes

- **Outdated Intel GPU driver** — The Intel display driver has a bug in the kernel mode component.
- **Intel GPU overheating** — Integrated GPU thermal throttling causes display timeouts.
- **Windows Update installing wrong Intel driver** — Incompatible Intel driver installed via Windows Update.
- **Dual GPU conflict** — Conflict between Intel integrated and discrete GPU drivers.

## How to Fix

### Update Intel GPU Driver

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*Intel*" } | Select-Object Name, DriverVersion, DriverDate
```

Download from [intel.com/content/www/us/en/support.html](https://www.intel.com/content/www/us/en/support.html).

### Disable Windows Update Driver Installation

```powershell
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching" -Name "SearchOrderConfig" -Value 0
```

### Increase TDR Timeout

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"TdrDelay"=dword:00000008
```

### Check Intel GPU Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

### Disable Intel GPU Power Management

In Device Manager > Display adapters > Intel adapter > Properties > Power Management:
- Uncheck "Allow the computer to turn off this device to save power"

### Clean Driver Installation

```cmd
# Boot into Safe Mode
# Run DDU for Intel Graphics
# Install latest Intel GPU driver
```

## Examples

```text
VIDEO_TDR_FAILURE (116)
Attempt to reset the display driver and recover from timeout failed.

MODULE_NAME: igdkmd64
IMAGE_NAME:  igdkmd64.sys
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA TDR failure
- [BSOD VIDEO_TDR_FAILURE atikmpag.sys]({{< relref "/os/windows/bsod-video-tdr-failure3" >}}) — AMD TDR failure
- [BSOD VIDEO_SCHEDULER_INTERNAL_ERROR]({{< relref "/os/windows/bsod-video-scheduler-internal" >}}) — Video scheduler failure
