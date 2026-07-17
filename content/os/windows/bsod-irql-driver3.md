---
title: "[Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xD1 nvlddmkm.sys Windows 11/10"
description: "Fix Blue Screen DRIVER_IRQL_NOT_LESS_OR_EQUAL stop code 0xD1 caused by nvlddmkm.sys NVIDIA driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "driver-irql", "nvlddmkm", "nvidia", "gpu", "stop-0xd1"]
weight: 5
---

# BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xD1 nvlddmkm.sys

The `DRIVER_IRQL_NOT_LESS_OR_EQUAL` stop code `0xD1` with `nvlddmkm.sys` indicates the NVIDIA display driver attempted to access paged memory at an elevated IRQL. This is a GPU-related BSOD caused by bugs in the NVIDIA kernel-mode driver.

## Common Causes

- **Outdated NVIDIA GPU driver** — The NVIDIA display driver has a bug in its kernel-mode component.
- **GPU overheating** — Thermal throttling causes the GPU driver to access invalid memory.
- **NVIDIA driver conflict with Windows Update** — Windows installs an incompatible NVIDIA driver.
- **GPU VRAM corruption** — Memory errors on the graphics card cause the driver to fail.

## How to Fix

### Update NVIDIA Driver

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*NVIDIA*" } | Select-Object Name, DriverVersion, DriverDate
```

Download from [nvidia.com/drivers](https://www.nvidia.com/drivers).

### Clean Driver Installation

```cmd
# Boot into Safe Mode
# Run DDU (Display Driver Uninstaller) for NVIDIA
# Install fresh driver
```

### Monitor GPU Temperature

```powershell
nvidia-smi --query-gpu=temperature.gpu,fan.speed,power.draw --format=csv 2>$null
```

### Disable GPU Overclocking

Reset all GPU clocks to stock using MSI Afterburner or NVIDIA Inspector.

### Disable NVIDIA Power Management

In Device Manager > Display adapters > NVIDIA adapter > Properties > Power Management:
- Uncheck "Allow the computer to turn off this device to save power"

### Test System RAM

```cmd
mdsched.exe
```

## Examples

```text
DRIVER_IRQL_NOT_LESS_OR_EQUAL (d1)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.

MODULE_NAME: nvlddmkm
IMAGE_NAME:  nvlddmkm.sys
```

## Related Errors

- [BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/os/windows/bsod-video-tdr-failure2" >}}) — NVIDIA TDR failure
- [BSOD VIDEO_TDR_FAILURE atikmpag.sys]({{< relref "/os/windows/bsod-video-tdr-failure3" >}}) — AMD TDR failure
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — General driver IRQL
