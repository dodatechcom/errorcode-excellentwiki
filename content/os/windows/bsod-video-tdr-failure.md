---
title: "[Solution] BSOD VIDEO_TDR_FAILURE Windows 11/10 — Fixed"
description: "Fix Blue Screen VIDEO_TDR_FAILURE on Windows 10 and 11. Resolve stop code 0x116 with GPU driver fixes for NVIDIA, AMD, and Intel graphics cards."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "video", "tdr", "gpu", "nvidia", "amd", "graphics"]
weight: 5
---

# [Solution] BSOD VIDEO_TDR_FAILURE Windows 11/10 — Fixed

VIDEO_TDR_FAILURE is a critical Blue Screen of Death error with stop code `0x00000116`. It indicates that the Windows Timeout Detection and Recovery (TDR) system detected that the GPU stopped responding within the allowed timeout period and could not recover. The TDR mechanism tries to reset the display driver before crashing, but when the reset fails, Windows triggers this bug check.

This BSOD is primarily a graphics driver issue and is most common with NVIDIA, AMD, and Intel GPUs. It frequently occurs during gaming, video playback, or any GPU-intensive workload.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: VIDEO_TDR_FAILURE
> What failed: [nvlddmkm.sys, atikmpag.sys, igdkmd64.sys]

The TDR system monitors GPU responsiveness. When a GPU command takes too long (typically more than 2 seconds), Windows attempts a driver reset. If the GPU is truly hung — due to overheating, driver bugs, or hardware failure — the reset fails and Windows crashes to prevent data loss.

Common scenarios for this BSOD:

- **During gaming or 3D rendering** — GPU under heavy load exceeds TDR timeout
- **While watching videos** — Hardware video decode fails on GPU
- **After GPU driver update** — New driver has bugs that cause GPU hangs
- **With overclocked GPUs** — Exceeding stable clock speeds causes GPU instability
- **With overheating GPUs** — Thermal throttling or shutdown causes TDR failures

## Common Causes

1. **Outdated or corrupted GPU driver** — The display driver has bugs that cause GPU hangs under load.
2. **GPU overheating** — Dust, failed fans, or dried thermal paste cause thermal issues.
3. **GPU hardware failure** — The graphics card is physically failing.
4. **Overclocking instability** — GPU clock speeds or memory timings exceed stable limits.

## Solutions

### Solution 1: Update GPU Drivers (NVIDIA)

NVIDIA GPUs are the most common victim of this BSOD. The nvlddmkm.sys driver is frequently the "What failed" name.

**Check current NVIDIA driver version:**

```powershell
nvidia-smi --query-gpu=driver_version,name --format=csv,noheader
```

**Download the latest stable driver:**

1. Go to [nvidia.com/drivers](https://www.nvidia.com/Download/index.aspx).
2. Select your GPU model and Windows version.
3. Download the driver.
4. During installation, check **Perform a clean installation**.
5. Restart your computer after installation completes.

**If the latest driver causes the BSOD, try the previous stable version:**

1. Boot into **Safe Mode** (force shutdown 3 times during boot > Advanced options > Startup Settings > press `4`).
2. Open **Device Manager** > **Display adapters**.
3. Right-click your GPU and select **Uninstall device**.
4. Check **Delete the driver software for this device**.
5. Restart and install the previous known-stable driver.

### Solution 2: Update GPU Drivers (AMD)

AMD GPUs can trigger this BSOD with the atikmpag.sys driver.

**Check current AMD driver version:**

```powershell
Get-WmiObject Win32_VideoController | Where-Object {$_.Name -like "*AMD*"} | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Download the latest AMD driver:**

1. Go to [amd.com/support](https://www.amd.com/en/support).
2. Select your GPU model.
3. Download AMD Software: Adrenalin Edition.
4. During installation, select **Factory Reset** for a clean install.
5. Restart your computer.

### Solution 3: Check GPU Temperature

Overheating is a common cause of GPU hangs.

**Monitor GPU temperature:**

```powershell
Get-WmiObject -Namespace root\wmi -Class MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Note: This reads from ACPI thermal zones. For accurate GPU temperature, use GPU-Z, HWiNFO, or your GPU manufacturer's software.

**Physical maintenance:**

1. Open your computer case and clean dust from GPU fans and heatsinks.
2. Use compressed air to blow dust out of the heatsink fins.
3. Check that all GPU fans are spinning.
4. If the GPU is more than 3 years old, consider replacing the thermal paste.

**Set a more generous TDR timeout in the registry:**

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" -Name "TdrDelay" -Value 8 -PropertyType DWORD -Force
```

This increases the TDR timeout from 2 seconds to 8 seconds, giving the GPU more time to respond. Restart after applying.

**To revert to default:**

```powershell
Remove-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" -Name "TdrDelay" -Force
```

### Solution 4: Reset GPU Overclocking

Overclocking beyond stable limits causes GPU hangs.

**Reset GPU to stock clocks (NVIDIA):**

```powershell
nvidia-smi -rac
```

**Reset GPU to stock clocks using software:**

1. Open MSI Afterburner, EVGA Precision, or your GPU overclocking tool.
2. Click **Reset** or **Default** to return to stock settings.
3. Apply changes and restart.

### Solution 5: Check GPU Hardware Health

If software fixes don't resolve the issue, the GPU hardware may be failing.

**Check for GPU errors in Event Viewer:**

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2; StartTime=(Get-Date).AddDays(-30)} | Where-Object {$_.ProviderName -like "*nvlddmkm*" -or $_.ProviderName -like "*atikmpag*"} | Select-Object TimeCreated, Id, Message | Format-Table -AutoSize
```

**Run a GPU stress test:**

1. Download FurMark or Unigine Heaven.
2. Run a stress test for 15-30 minutes.
3. Watch for artifacts, freezes, or crashes — these indicate hardware failure.

If the GPU fails stress tests consistently, it likely needs replacement.

## Related Errors

- **[BSOD VIDEO_SCHEDULER_INTERNAL_ERROR]({{< relref "/windows/bsod-video-scheduler" >}})** — Another GPU driver BSOD from the video scheduler
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — GPU driver memory access violations
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread crash from faulty GPU drivers
- **[BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/windows/bsod-whea2" >}})** — Hardware error that can be triggered by GPU failure
