---
title: "[Solution] BSOD VIDEO_TDR_FAILURE Windows 11/10 — Fixed"
description: "Fix Blue Screen VIDEO_TDR_FAILURE error on Windows 10 and 11. Update GPU drivers, check temperature, and adjust TDR settings to resolve this graphics-related stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "video-tdr", "gpu", "graphics", "stop-code"]
weight: 5
---

# [Solution] BSOD VIDEO_TDR_FAILURE Windows 11/10 — Fixed

VIDEO_TDR_FAILURE is a critical Blue Screen of Death error with stop code `0x00000116`. It occurs when the Windows Timeout Detection and Recovery (TDR) feature fails to recover from a graphics driver timeout. The GPU stops responding, Windows attempts to reset the driver, and when that reset fails, the system crashes.

This BSOD affects both Windows 10 and 11 and is almost always related to the graphics driver or GPU hardware. The blue screen message typically names the failing driver file.

## Common Causes

- **Outdated or corrupted GPU drivers** — The graphics driver crashes during rendering and cannot recover through TDR.
- **GPU overheating** — Thermal throttling or hardware failure causes the GPU to stop responding.
- **Overclocked GPU** — Unstable GPU clock speeds cause rendering failures under load.
- **Failing GPU hardware** — Physical degradation of the graphics card causes intermittent lockups.

## How to Fix

### Update GPU Drivers

The graphics driver is almost always the cause. Perform a clean driver installation.

**Check current GPU driver version:**

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate, Status | Format-Table -AutoSize
```

Download and install the latest driver from the GPU manufacturer:
- **NVIDIA**: Use GeForce Experience or download from [nvidia.com/drivers](https://www.nvidia.com/drivers)
- **AMD**: Use AMD Software: Adrenalin Edition
- **Intel**: Use Intel Driver & Support Assistant

During installation, select **Perform a clean install** to remove all previous driver remnants.

### Monitor GPU Temperature

Overheating is a common secondary cause:

```powershell
Get-WmiObject -Namespace root\wmi -Class WmiMonitorBrightness | Select-Object CurrentBrightness
```

Use GPU-Z or HWMonitor to check GPU temperature during load. Normal operating temperatures:
- **Idle**: 30–45°C
- **Under load**: 65–85°C
- **Danger zone**: Above 90°C

Clean dust from GPU fans and heatsinks. Ensure adequate case ventilation.

### Increase TDR Timeout

If the GPU driver is legitimate but slow to respond, you can increase the TDR timeout:

1. Open **Registry Editor** (`Win + R` > `regedit`).
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Create or modify a **DWORD (32-bit)** value named `TdrDelay`.
4. Set the value to `8` (seconds) instead of the default 2.
5. Restart your computer.

**Or increase recovery attempts with TdrLevel:**

1. In the same registry location, create or modify a **DWORD (32-bit)** value named `TdrLevel`.
2. Set the value to `0` to disable automatic recovery (use only for debugging).

### Remove GPU Overclock

If you are overclocking the GPU:

1. Open your overclocking tool (MSI Afterburner, EVGA Precision, etc.).
2. Click **Reset** to return to stock clock speeds.
3. Apply changes and restart.

**Reset NVIDIA GPU to stock clocks:**

```powershell
nvidia-smi -rac
```

### Check for Failing GPU Hardware

If driver updates and temperature fixes don't resolve the issue, the GPU hardware may be failing:

1. Run a GPU stress test (FurMark, 3DMark) and monitor for artifacts or crashes.
2. Try the GPU in another system to confirm whether the card is faulty.
3. If under warranty, contact the manufacturer for a replacement.

### Run SFC to Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples

This error commonly occurs in these scenarios:

- **During gaming or 3D rendering** — GPU driver timeout under sustained heavy load.
- **When watching HD video** — Hardware video acceleration causes GPU lockup.
- **After GPU driver update** — New driver version has a bug in its TDR handling.
- **With overclocked GPUs** — Unstable clock speeds cause rendering failures.

## Related Errors

- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-system-thread-exception" >}}) — Often triggered by the same GPU driver issues
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — Driver accessing memory at invalid IRQL
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel-mode exception from driver instability
- [BSOD DPC Watchdog Violation]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — Another driver timeout BSOD
