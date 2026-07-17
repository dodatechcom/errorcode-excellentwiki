---
title: "[Solution] BSOD VIDEO_TDR_FAILURE — 0x116 dxgkrnl.sys Windows 11/10"
description: "Fix Blue Screen VIDEO_TDR_FAILURE stop code 0x116 caused by dxgkrnl.sys DirectX kernel on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD VIDEO_TDR_FAILURE — 0x116 dxgkrnl.sys

The `VIDEO_TDR_FAILURE` stop code `0x116` with `dxgkrnl.sys` indicates the DirectX graphics kernel subsystem failed to recover from a TDR (Timeout Detection and Recovery) reset. The GPU stopped responding and the kernel-level DirectX driver could not reset the display pipeline.

## Common Causes

- **GPU driver bug in DirectX kernel path** — The display driver has a defect in the DirectX kernel integration.
- **GPU overheating** — Thermal throttling causes the GPU to become unresponsive.
- **DirectX runtime corruption** — Damaged DirectX system files cause the kernel driver to fail.
- **GPU hardware failure** — Physical GPU defects cause periodic driver crashes.

## How to Fix

### Update GPU Driver

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Increase TDR Timeout

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"TdrDelay"=dword:00000008
"TdrLevel"=dword:00000003
```

### Repair DirectX Runtime

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Monitor GPU Temperature

```powershell
nvidia-smi --query-gpu=temperature.gpu --format=csv 2>$null
```

### Clean Driver Installation

```cmd
# Boot into Safe Mode
# Run DDU (Display Driver Uninstaller)
# Install fresh GPU driver
```

### Check for Windows Updates

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -Install -AcceptAll
```

## Examples

```text
VIDEO_TDR_FAILURE (116)
Attempt to reset the display driver and recover from timeout failed.

MODULE_NAME: dxgkrnl
IMAGE_NAME:  dxgkrnl.sys
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA driver TDR
- [BSOD VIDEO_TDR_FAILURE atikmpag.sys]({{< relref "/os/windows/bsod-video-tdr-failure3" >}}) — AMD driver TDR
- [BSOD VIDEO_SCHEDULER_INTERNAL_ERROR]({{< relref "/os/windows/bsod-video-scheduler-internal" >}}) — Video scheduler failure
