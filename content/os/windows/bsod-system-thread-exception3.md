---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E dxgkrnl.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by dxgkrnl.sys DirectX kernel on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E dxgkrnl.sys

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `dxgkrnl.sys` indicates the DirectX graphics kernel subsystem encountered an unhandled exception during a system thread operation. This is commonly caused by GPU driver issues on Windows 10 and 11.

## Common Causes

- **Outdated or corrupted GPU driver** — The NVIDIA, AMD, or Intel graphics driver has a bug in the DirectX kernel path.
- **GPU hardware overheating** — Thermal throttling causes the GPU driver to access invalid memory.
- **DirectX runtime corruption** — Damaged DirectX system files cause the kernel to fail.
- **GPU overclocking instability** — Aggressive GPU clocks cause driver exceptions.

## How to Fix

### Update GPU Drivers

Download the latest driver from the GPU manufacturer:

```powershell
# Check current GPU driver
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download from [NVIDIA](https://www.nvidia.com/drivers), [AMD](https://www.amd.com/support), or [Intel](https://www.intel.com/content/www/us/en/support.html).

### Perform Clean GPU Driver Installation

```cmd
# Use DDU to completely remove old drivers
# Download Display Driver Uninstaller from guru3d.com
# Boot into Safe Mode and run DDU, then install fresh driver
```

### Check GPU Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Ensure GPU temperature stays below 85°C under load. Clean dust from GPU fans.

### Disable GPU Overclocking

Reset GPU clocks to defaults in your GPU control panel (NVIDIA Control Panel, AMD Adrenalin, or Intel Graphics Command Center).

### Repair DirectX Runtime

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Check for Windows Updates

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -Install -AcceptAll
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: dxgkrnl
IMAGE_NAME:  dxgkrnl.sys
FOLLOWUP_NAME:  dxgkrnl!DXGDEVICE::Destroy
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE dxgkrnl.sys]({{< relref "/os/windows/bsod-video-tdr-failure4" >}}) — DirectX TDR timeout
- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA driver TDR failure
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED ntfs.sys]({{< relref "/os/windows/bsod-system-thread-exception5" >}}) — NTFS driver exception
