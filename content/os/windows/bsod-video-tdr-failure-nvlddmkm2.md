---
title: "[Solution] BSOD VIDEO_TDR_FAILURE nvlddmkm.sys NVIDIA GPU Fix"
description: "Fix Blue Screen VIDEO_TDR_FAILURE caused by nvlddmkm.sys on Windows 10 and 11. Resolve NVIDIA GPU timeout detection failures with driver updates and thermal fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "nvidia", "nvlddmkm", "gpu", "tdr", "video"]
weight: 5
---

# [Solution] BSOD VIDEO_TDR_FAILURE nvlddmkm.sys NVIDIA GPU Fix

VIDEO_TDR_FAILURE with `nvlddmkm.sys` is a Blue Screen error that occurs when the NVIDIA graphics driver fails to respond to the Timeout Detection and Recovery (TDR) mechanism. Windows attempts to reset the GPU driver, and when that reset fails, the system crashes.

This BSOD is extremely common with NVIDIA GPUs, especially during gaming, 3D rendering, or multi-monitor setups. The TDR timeout is typically 2 seconds — if the GPU does not respond within that window, Windows triggers the crash.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: VIDEO_TDR_FAILURE
> What failed: nvlddmkm.sys

TDR stands for **Timeout Detection and Recovery**. Windows monitors GPU responsiveness and attempts to reset the driver if it stops responding. When the reset itself fails (because the driver is too deeply corrupted or the hardware is unresponsive), Windows crashes with this BSOD.

Common triggers include:

- **GPU overheating** — Thermal protection causes the GPU to stop responding
- **GPU under load** — Demanding applications exceed GPU capabilities
- **Faulty VRAM** — Memory errors cause the driver to hang
- **Unstable overclock** — Core or memory clocks exceed stable limits

## Common Causes

1. **GPU overheating** — Inadequate cooling or dried thermal paste causes the GPU to throttle and hang.
2. **Unstable GPU overclock** — Pushing memory or core clocks beyond stable limits.
3. **Corrupted NVIDIA driver** — Bad driver installation or conflicting driver components.
4. **Faulty GPU hardware** — Degraded VRAM or failing GPU die.
5. **Power supply issues** — Insufficient or unstable power delivery to the GPU.

## How to Fix

### Solution 1: Increase TDR Timeout

Increasing the TDR delay gives the GPU more time to respond before Windows gives up:

1. Press `Win + R`, type `regedit`, and press **Ctrl + Shift + Enter**.
2. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
3. Create or modify a **DWORD (32-bit)** value named `TdrDelay`.
4. Set the value to `8` (seconds) in decimal.
5. Create or modify a **DWORD (32-bit)** value named `TdrLevel`.
6. Set the value to `3` (default recovery behavior).
7. Restart your computer.

**Verify the registry values:**

```powershell
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" -Name TdrDelay, TdrLevel -ErrorAction SilentlyContinue | Select-Object TdrDelay, TdrLevel
```

### Solution 2: Clean Install NVIDIA Driver with DDU

1. Download **DDU** from [wagnardsoft.com](https://www.wagnardsoft.com/display-driver-uninstaller-DDU).
2. Download the latest NVIDIA driver from [nvidia.com/drivers](https://www.nvidia.com/Download/index.aspx).
3. Boot into **Safe Mode**.
4. Run DDU and select **Clean and restart**.
5. Install the downloaded NVIDIA driver after reboot.

### Solution 3: Monitor GPU Temperature

```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSAcpi_ThermalZoneTemperature | Select-Object InstanceName, CurrentTemperature
```

If temperatures exceed **85°C** during load:
- Clean dust from the GPU heatsink and case fans
- Replace thermal paste if older than 3 years
- Add case fans or improve airflow
- Ensure the GPU is not in a poorly ventilated area

### Solution 4: Reset GPU Overclock

1. Open **MSI Afterburner** or your overclocking tool.
2. Click the **reset** button to restore defaults.
3. Apply and save.

**Check current GPU clocks:**

```cmd
nvidia-smi --query-gpu=clocks.gr,clocks.mem --format=csv
```

Compare against stock specifications on the NVIDIA website for your GPU model.

### Solution 5: Check Power Supply

Insufficient power can cause GPU hangs under load:

1. Verify your PSU wattage meets the GPU's minimum requirement.
2. Ensure PCIe power connectors are firmly seated on the GPU.
3. Try a different PCIe power cable from the PSU.
4. If using a power adapter, ensure it is rated for the GPU's power draw.

## Related Errors

- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED nvlddmkm.sys]({{< relref "/windows/bsod-system-thread-exception-nvlddmkm" >}})** — NVIDIA driver system thread crash
- **[BSOD VIDEO_TDR_FAILURE atikmpag.sys]({{< relref "/windows/bsod-video-tdr-failure-atikmpag" >}})** — AMD GPU version of this error
- **[BSOD VIDEO_TDR_FAILURE igdkmd64.sys]({{< relref "/windows/bsod-video-tdr-failure-igdkmd64" >}})** — Intel GPU version of this error
