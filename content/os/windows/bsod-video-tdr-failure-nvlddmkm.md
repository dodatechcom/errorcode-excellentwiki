---
title: "[Solution] BSOD VIDEO_TDR_FAILURE (nvlddmkm.sys) — Blue Screen Fix"
description: "Fix Windows Blue Screen VIDEO_TDR_FAILURE nvlddmkm.sys with these step-by-step solutions. Includes NVIDIA driver updates, GPU temperature checks, and driver reinstalls."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 22
---

# [Solution] BSOD VIDEO_TDR_FAILURE (nvlddmkm.sys) — Blue Screen Fix

The `VIDEO_TDR_FAILURE` stop code with `nvlddmkm.sys` indicates the NVIDIA graphics driver stopped responding and failed to recover. TDR (Timeout Detection and Recovery) is Windows' mechanism to reset unresponsive display drivers.

## Description

This BSOD is specific to NVIDIA GPUs and occurs when the graphics driver crashes and cannot recover. Common triggers include overheating GPUs, outdated drivers, and unstable overclocks.

## Common Causes

1. Outdated or corrupted NVIDIA drivers
2. GPU overheating
3. Unstable GPU overclock
4. Faulty GPU hardware
5. Insufficient power supply to GPU

## Solutions

### Solution 1: Update NVIDIA Drivers

Download and install the latest NVIDIA drivers:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceName -like "*NVIDIA*" } | Select-Object DeviceName, DriverVersion, DriverDate
```

Download from [nvidia.com/drivers](https://www.nvidia.com/drivers) or use GeForce Experience.

### Solution 2: Check GPU Temperature

Monitor GPU temperature under load:

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Clean dust from GPU heatsink and fans. Ensure proper case airflow. Replace thermal paste if temperatures exceed 85°C under load.

### Solution 3: Reinstall NVIDIA Drivers

Perform a clean driver reinstall:

1. Download Display Driver Uninstaller (DDU)
2. Boot into Safe Mode
3. Run DDU to remove all NVIDIA drivers
4. Restart and install fresh NVIDIA drivers

## Related Errors

- [VIDEO_SCHEDULER_INTERNAL_ERROR](bsod-video-scheduler-internal-error.md)
- [DRIVER_IRQL_NOT_LESS_OR_EQUAL](bsod-driver-irql-not-less-or-equal.md)
- [DPC_WATCHDOG_VIOLATION](bsod-dpc-watchdog-violation.md)
