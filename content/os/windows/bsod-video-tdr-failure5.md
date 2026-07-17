---
title: "[Solution] BSOD VIDEO_TDR_FAILURE — 0x116 dxgkrnl.sys Windows 11/10"
description: "Fix Blue Screen VIDEO_TDR_FAILURE stop code 0x116 caused by dxgkrnl.sys DirectX kernel driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "video-tdr", "dxgkrnl", "directx", "gpu", "stop-0x116"]
weight: 5
---

# BSOD VIDEO_TDR_FAILURE — 0x116 dxgkrnl.sys (2nd variant)

The `VIDEO_TDR_FAILURE` stop code `0x116` with `dxgkrnl.sys` indicates the DirectX graphics kernel failed to respond to a TDR request. This variant occurs during GPU compute workloads, not just display rendering.

## Common Causes

- **GPU compute workload overload** — Mining, rendering, or compute tasks exceed GPU capabilities.
- **DirectX kernel driver bug** — The dxgkrnl.sys driver has a defect in its compute scheduling path.
- **GPU memory exhaustion** — VRAM is fully consumed causing DirectX to fail.
- **Hyper-V GPU-PV conflict** — GPU virtualization causes DirectX kernel scheduling issues.

## How to Fix

### Update GPU Driver

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Increase TDR Delay

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"TdrDelay"=dword:00000010
```

### Reduce GPU Workload

Limit concurrent GPU compute tasks and monitor VRAM usage:
```powershell
nvidia-smi --query-gpu=memory.used,memory.total --format=csv 2>$null
```

### Disable Hyper-V GPU-PV

```powershell
Set-VMGpuPartitionAdapter -VMName "VMName" -ResourcePartitionType None
```

### Repair DirectX

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Monitor GPU Temperature

```powershell
nvidia-smi --query-gpu=temperature.gpu --format=csv 2>$null
```

## Examples

```text
VIDEO_TDR_FAILURE (116)
Attempt to reset the display driver and recover from timeout failed.

MODULE_NAME: dxgkrnl
IMAGE_NAME:  dxgkrnl.sys
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE dxgkrnl.sys]({{< relref "/os/windows/bsod-video-tdr-failure4" >}}) — DirectX kernel TDR variant
- [BSOD VIDEO_SCHEDULER_INTERNAL_ERROR]({{< relref "/os/windows/bsod-video-scheduler-internal" >}}) — Video scheduler failure
- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA TDR failure
