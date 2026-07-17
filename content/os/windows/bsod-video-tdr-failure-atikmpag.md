---
title: "[Solution] BSOD VIDEO_TDR_FAILURE atikmpag.sys AMD GPU Fix"
description: "Fix Blue Screen VIDEO_TDR_FAILURE caused by atikmpag.sys on Windows 10 and 11. Resolve AMD GPU timeout detection failures with driver reinstalls and thermal fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "amd", "atikmpag", "gpu", "tdr", "radeon"]
weight: 5
---

# [Solution] BSOD VIDEO_TDR_FAILURE atikmpag.sys AMD GPU Fix

VIDEO_TDR_FAILURE with `atikmpag.sys` is a Blue Screen error caused by the AMD Radeon kernel-mode display driver failing to respond to the Timeout Detection and Recovery (TDR) mechanism. Windows attempts to reset the GPU driver, and when it fails, the system crashes.

This error is specific to AMD Radeon GPUs and is frequently seen during gaming, video playback, or when running GPU-accelerated applications.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: VIDEO_TDR_FAILURE
> What failed: atikmpag.sys

`atikmpag.sys` is the AMD kernel-mode display driver component. TDR (Timeout Detection and Recovery) monitors GPU responsiveness and attempts to reset the driver when it stops responding. When the reset fails, Windows crashes.

Common triggers include:

- **Corrupted AMD driver installation** — Partial installs or driver conflicts
- **GPU overheating** — Thermal throttling causes the GPU to hang
- **Unstable overclock** — Memory or core clocks beyond stable limits
- **Faulty GPU hardware** — VRAM degradation or power delivery issues

## Common Causes

1. **Corrupted or outdated AMD driver** — The most frequent cause, especially after failed driver updates.
2. **GPU overheating** — AMD GPUs are sensitive to thermal throttling under sustained load.
3. **Unstable overclock** — Memory or core clock speeds that exceed stable limits.
4. **Faulty GPU hardware** — Failing VRAM or power delivery components.
5. **Windows update conflicts** — Windows overwriting AMD driver files.

## How to Fix

### Solution 1: Clean AMD Driver Installation with DDU

The most reliable fix is a complete driver removal and clean reinstall:

1. Download **DDU** from [wagnardsoft.com](https://www.wagnardsoft.com/display-driver-uninstaller-DDU).
2. Download the latest AMD Adrenalin driver from [amd.com/support](https://www.amd.com/en/support).
3. Disconnect from the internet.
4. Boot into **Safe Mode**.
5. Run DDU and select **Clean and restart**.
6. Install the AMD driver after reboot.

**Check current AMD driver version:**

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*AMD*" -or $_.Name -like "*Radeon*" } | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Solution 2: Delete the Corrupted atikmpag.sys File

If DDU is not available, you can force Windows to rebuild the driver:

1. Boot into **Safe Mode**.
2. Navigate to `C:\Windows\System32\drivers`.
3. Delete or rename `atikmpag.sys` and `atikmdag.sys`.
4. Boot into normal mode and let Windows install a basic display driver.
5. Install the latest AMD driver from the official website.

### Solution 3: Monitor GPU Temperature

```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSAcpi_ThermalZoneTemperature | Select-Object InstanceName, CurrentTemperature
```

AMD GPUs typically throttle at **95°C**. Keep temperatures below **85°C** under load by:
- Cleaning dust from the GPU cooler
- Replacing thermal paste
- Improving case airflow

### Solution 4: Reset GPU Overclock

```cmd
# Reset AMD Overdrive settings (if using AMD Software)
# Open AMD Software: Adrenalin Edition > Performance > Tuning > Reset to Defaults
```

**Check current GPU clocks:**

```powershell
Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorID | Select-Object InstanceName
```

Use GPU-Z to verify clock speeds against stock specifications.

### Solution 5: Increase TDR Timeout

1. Press `Win + R`, type `regedit`, and press **Ctrl + Shift + Enter**.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Create or modify **DWORD (32-bit)** value `TdrDelay` and set it to `8` (seconds).
4. Restart your computer.

## Related Errors

- **[BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/windows/bsod-video-tdr-failure-nvlddmkm2" >}})** — NVIDIA GPU version of this error
- **[BSOD VIDEO_TDR_FAILURE igdkmd64.sys]({{< relref "/windows/bsod-video-tdr-failure-igdkmd64" >}})** — Intel GPU version of this error
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — Generic system thread exception with various drivers
