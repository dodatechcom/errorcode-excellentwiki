---
title: "[Solution] BSOD VIDEO_SCHEDULER_INTERNAL_ERROR — 0x119 Windows 11/10"
description: "Fix Blue Screen VIDEO_SCHEDULER_INTERNAL_ERROR stop code 0x119 on Windows 10 and 11. Resolve video scheduler and GPU driver issues."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "video-scheduler", "gpu", "display", "stop-0x119"]
weight: 5
---

# BSOD VIDEO_SCHEDULER_INTERNAL_ERROR — 0x119

The `VIDEO_SCHEDULER_INTERNAL_ERROR` stop code `0x119` indicates the video scheduler, which manages GPU scheduling in the Windows kernel, detected an internal error. This points to GPU driver bugs or GPU hardware issues.

## Common Causes

- **GPU driver bug** — The display driver has a defect in the video scheduler component.
- **GPU hardware failure** — Physical defects on the graphics card cause scheduler errors.
- **GPU overheating** — Thermal throttling disrupts the video scheduler's timing.
- **Multiple display adapters conflict** — Conflicting GPU drivers from different vendors cause scheduler confusion.
- **GPU virtualization issues** — Hyper-V or GPU partitioning creates scheduler conflicts.

## How to Fix

### Update GPU Driver

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest driver from the GPU manufacturer's website.

### Perform Clean Driver Installation

```cmd
# Download and run DDU (Display Driver Uninstaller)
# Boot into Safe Mode
# Run DDU to remove all GPU drivers
# Install fresh driver from manufacturer
```

### Monitor GPU Temperature

```powershell
nvidia-smi --query-gpu=temperature.gpu,fan.speed --format=csv 2>$null
```

Ensure GPU temperature stays below 85°C under load.

### Disable GPU Overclocking

Reset GPU core and memory clocks to stock using the GPU control panel.

### Check for Multiple GPU Drivers

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, Status, DriverVersion | Format-Table -AutoSize
```

Remove conflicting GPU drivers if both integrated and discrete GPUs have third-party drivers.

### Disable Hyper-V GPU Partitioning

If using Hyper-V, check if GPU-PV (Paravirtualization) is causing conflicts and disable it.

## Examples

```text
VIDEO_SCHEDULER_INTERNAL_ERROR (119)
The video scheduler has detected a fatal violation.

MODULE_NAME: dxgkrnl
IMAGE_NAME:  dxgkrnl.sys
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA TDR failure
- [BSOD VIDEO_TDR_FAILURE atikmpag.sys]({{< relref "/os/windows/bsod-video-tdr-failure3" >}}) — AMD TDR failure
- [BSOD VIDEO_TDR_FAILURE dxgkrnl.sys]({{< relref "/os/windows/bsod-video-tdr-failure4" >}}) — DirectX kernel TDR
