---
title: "[Solution] BSOD VIDEO_TDR_FAILURE — 0x116 atikmpag.sys Windows 11/10"
description: "Fix Blue Screen VIDEO_TDR_FAILURE stop code 0x116 caused by atikmpag.sys AMD display driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "video-tdr", "atikmpag", "amd", "gpu", "stop-0x116"]
weight: 5
---

# BSOD VIDEO_TDR_FAILURE — 0x116 atikmpag.sys

The `VIDEO_TDR_FAILURE` stop code `0x116` with `atikmpag.sys` indicates the AMD display driver kernel module failed to recover from a TDR reset. Windows detected the GPU stopped responding and attempted a driver reset, but the AMD driver could not recover.

## Common Causes

- **Outdated or corrupted AMD GPU driver** — The AMD Radeon driver has bugs in the display kernel module.
- **GPU overheating** — Thermal throttling causes the AMD GPU to stop responding.
- **AMD driver conflict with Windows Update** — Windows Update installs an incompatible AMD driver version.
- **Defective GPU hardware** — Physical defects on the AMD graphics card cause periodic crashes.

## How to Fix

### Update AMD GPU Driver

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*AMD*" -or $_.Name -like "*Radeon*" } | Select-Object Name, DriverVersion, DriverDate
```

Download the latest driver from [amd.com/support](https://www.amd.com/support).

### Increase TDR Delay

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"TdrDelay"=dword:00000008
```

### Disable Windows Update Driver Installation

```powershell
# Prevent Windows from auto-updating GPU drivers
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching" -Name "SearchOrderConfig" -Value 0
```

### Clean Driver Installation

```cmd
# Boot into Safe Mode
# Run DDU (Display Driver Uninstaller) for AMD
# Install the latest AMD Adrenalin driver
```

### Monitor GPU Health

```powershell
# Check GPU temperature and fan speed
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

### Check Event Viewer for Pre-Crash Errors

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*display*" -or $_.ProviderName -like "*video*" } | Select-Object -First 10 TimeCreated, Message | Format-Table -Wrap
```

## Examples

```text
VIDEO_TDR_FAILURE (116)
Attempt to reset the display driver and recover from timeout failed.

atikmpag.sys — Address FFFFF88004A0A0A0 base at FFFFF88004600000
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA GPU TDR failure
- [BSOD VIDEO_TDR_FAILURE dxgkrnl.sys]({{< relref "/os/windows/bsod-video-tdr-failure4" >}}) — DirectX kernel TDR
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-system-thread-exception3" >}}) — System thread GPU exception
