---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION — 0x133 dxgkrnl.sys Windows 11/10"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION stop code 0x133 caused by dxgkrnl.sys DirectX kernel on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "dpc-watchdog", "dxgkrnl", "directx", "gpu", "stop-0x133"]
weight: 5
---

# BSOD DPC_WATCHDOG_VIOLATION — 0x133 dxgkrnl.sys

The `DPC_WATCHDOG_VIOLATION` stop code `0x133` with `dxgkrnl.sys` indicates the DirectX graphics kernel driver took too long to complete a Deferred Procedure Call. The DPC watchdog timer expired while the GPU driver was processing a display or compute operation.

## Common Causes

- **GPU driver DPC timeout** — The DirectX kernel driver hangs during a DPC callback.
- **GPU hardware hang** — Physical GPU issues cause the driver to stop responding.
- **Multi-GPU configuration issues** — SLI/CrossFire setups cause DPC timing issues.
- **GPU driver conflict with other DPC drivers** — Other drivers block the GPU DPC from completing.

## How to Fix

### Update GPU Driver

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Increase DPC Timeout

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"TdrDelay"=dword:00000008
```

### Monitor GPU Performance

```powershell
nvidia-smi --query-gpu=temperature.gpu,utilization.gpu,memory.used --format=csv 2>$null
```

### Disable GPU Overclocking

Reset GPU core and memory clocks to stock.

### Clean Driver Installation

```cmd
# Boot into Safe Mode
# Run DDU (Display Driver Uninstaller)
# Install fresh GPU driver
```

### Check for DPC Conflicts

```cmd
# Enable DPC monitoring
wpr -start GeneralProfile -start CPU -filemode
```

## Examples

```text
DPC_WATCHDOG_VIOLATION (133)
A DPC did not complete in a timely manner.

MODULE_NAME: dxgkrnl
IMAGE_NAME:  dxgkrnl.sys
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE dxgkrnl.sys]({{< relref "/os/windows/bsod-video-tdr-failure4" >}}) — DirectX TDR failure
- [BSOD DPC_WATCHDOG_VIOLATION stornvme.sys]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — NVMe DPC timeout
- [BSOD DPC_WATCHDOG_VIOLATION iaStorA.sys]({{< relref "/os/windows/bsod-dpc-watchdog3" >}}) — Intel RST DPC timeout
