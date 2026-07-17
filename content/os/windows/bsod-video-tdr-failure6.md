---
title: "[Solution] BSOD VIDEO_TDR_FAILURE — 0x116 nvlddmkm.sys Windows 11/10"
description: "Fix Blue Screen VIDEO_TDR_FAILURE stop code 0x116 caused by nvlddmkm.sys NVIDIA driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD VIDEO_TDR_FAILURE — 0x116 nvlddmkm.sys (2nd variant)

The `VIDEO_TDR_FAILURE` stop code `0x116` with `nvlddmkm.sys` is a second variant of the NVIDIA TDR failure. This version typically occurs during gaming or GPU-intensive applications where the NVIDIA driver's display management times out.

## Common Causes

- **NVIDIA driver bug during GPU-intensive tasks** — Games and rendering applications trigger driver timeouts.
- **Insufficient GPU power delivery** — Power supply cannot sustain GPU load causing TDR.
- **GPU memory errors** — VRAM defects cause rendering failures that trigger TDR.
- **NVIDIA driver conflict with game overlay** — GeForce Experience or Steam overlay cause TDR.

## How to Fix

### Update NVIDIA Driver

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*NVIDIA*" } | Select-Object Name, DriverVersion, DriverDate
```

### Disable Game Overlays

Disable NVIDIA GeForce Experience overlay, Steam overlay, and Discord overlay.

### Increase TDR Timeout

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"TdrDelay"=dword:0000000a
"TdrLevel"=dword:00000003
```

### Check GPU Power Supply

Ensure the GPU has adequate power connectors from the PSU. Check PSU wattage is sufficient.

### Monitor GPU Temperature Under Load

```powershell
nvidia-smi --query-gpu=temperature.gpu,power.draw --format=csv 2>$null
```

### Clean Driver Installation

```cmd
# Boot into Safe Mode
# Run DDU for NVIDIA
# Install latest Game Ready driver
```

## Examples

```text
VIDEO_TDR_FAILURE (116)
Attempt to reset the display driver and recover from timeout failed.

nvlddmkm.sys — Display driver stopped responding and has recovered
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA TDR first variant
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL nvlddmkm.sys]({{< relref "/os/windows/bsod-irql-driver3" >}}) — NVIDIA IRQL violation
- [BSOD VIDEO_TDR_FAILURE dxgkrnl.sys]({{< relref "/os/windows/bsod-video-tdr-failure4" >}}) — DirectX kernel TDR
