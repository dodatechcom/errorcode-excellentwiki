---
title: "[Solution] BSOD VIDEO_TDR_FAILURE — 0x116 nvlddmkm.sys Windows 11/10"
description: "Fix Blue Screen VIDEO_TDR_FAILURE stop code 0x116 caused by nvlddmkm.sys NVIDIA driver timeout on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD VIDEO_TDR_FAILURE — 0x116 nvlddmkm.sys

The `VIDEO_TDR_FAILURE` stop code `0x116` with `nvlddmkm.sys` means the NVIDIA display driver failed to respond to the Timeout Detection and Recovery (TDR) request. Windows tried to reset the GPU but the driver could not recover, resulting in a blue screen.

## Common Causes

- **Outdated or corrupted NVIDIA GPU driver** — The NVIDIA display driver has a known bug or is incompatible.
- **GPU overheating** — Thermal throttling causes the GPU to become unresponsive during rendering.
- **Unstable GPU overclock** — Excessive core or memory clocks cause the driver to crash.
- **Failing GPU hardware** — Physical GPU defects cause periodic driver crashes.
- **Defective VRAM** — Memory errors on the graphics card cause rendering failures.

## How to Fix

### Update NVIDIA Driver

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*NVIDIA*" } | Select-Object Name, DriverVersion, DriverDate
```

Download the latest Game Ready or Studio driver from [nvidia.com/drivers](https://www.nvidia.com/drivers).

### Increase TDR Timeout

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"TdrDelay"=dword:00000008
"TdrLevel"=dword:00000003
```

This gives the GPU 8 seconds to respond instead of the default 2 seconds. Restart after applying.

### Monitor GPU Temperature

```powershell
# Install GPU-Z or use nvidia-smi
nvidia-smi --query-gpu=temperature.gpu,fan.speed,power.draw --format=csv
```

Keep GPU temperature below 85°C. Clean dust and improve airflow.

### Disable GPU Overclocking

Reset all GPU frequencies to stock using MSI Afterburner or NVIDIA Inspector.

### Run Memory Diagnostic

```cmd
mdsched.exe
```

Bad system RAM can also cause GPU driver failures.

### Clean Driver Installation

```cmd
# Boot into Safe Mode
# Run DDU (Display Driver Uninstaller)
# Install fresh NVIDIA driver
```

## Examples

```text
VIDEO_TDR_FAILURE (116)
Attempt to reset the display driver and recover from timeout failed.

nvlddmkm.sys — Address FFFFF88004A0A0A0 base at FFFFF88004600000, DateStamp 60xxxxxx
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE atikmpag.sys]({{< relref "/os/windows/bsod-video-tdr-failure3" >}}) — AMD GPU TDR failure
- [BSOD VIDEO_TDR_FAILURE dxgkrnl.sys]({{< relref "/os/windows/bsod-video-tdr-failure4" >}}) — DirectX kernel TDR
- [BSOD VIDEO_SCHEDULER_INTERNAL_ERROR]({{< relref "/os/windows/bsod-video-scheduler-internal" >}}) — Video scheduler failure
