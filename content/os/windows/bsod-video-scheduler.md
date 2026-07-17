---
title: "[Solution] BSOD VIDEO_SCHEDULER_INTERNAL_ERROR Windows 11/10 — Fixed"
description: "Fix Blue Screen VIDEO_SCHEDULER_INTERNAL_ERROR on Windows 10 and 11. Resolve stop code 0x119 with GPU driver fixes, hardware diagnostics, and system repairs."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "video-scheduler", "gpu", "graphics", "display"]
weight: 5
---

# [Solution] BSOD VIDEO_SCHEDULER_INTERNAL_ERROR Windows 11/10 — Fixed

VIDEO_SCHEDULER_INTERNAL_ERROR is a critical Blue Screen of Death error with stop code `0x00000119`. It indicates that the video scheduler — the kernel component that manages GPU scheduling and resource allocation — has encountered an internal error. The scheduler cannot safely manage GPU operations and must crash the system.

This BSOD is directly related to the GPU subsystem and is almost always caused by a faulty or corrupted graphics driver. It affects NVIDIA, AMD, and Intel GPUs and typically appears during gaming, video playback, or any GPU-intensive workload.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: VIDEO_SCHEDULER_INTERNAL_ERROR

The video scheduler is responsible for managing GPU execution, allocating video memory, and scheduling graphics operations. When it encounters an internal inconsistency — such as a driver sending invalid commands, GPU hardware failing, or video memory corruption — it triggers this bug check.

Common scenarios for this BSOD:

- **During gaming** — GPU scheduler fails under heavy graphics load
- **While watching videos** — Hardware video decode causes scheduler errors
- **After GPU driver update** — New driver has scheduler-related bugs
- **With multiple monitors** — Multi-display setups stress the scheduler
- **After Windows update** — Updated graphics components conflict with existing driver

## Common Causes

1. **Faulty GPU driver** — The display driver contains bugs in the scheduler interaction code.
2. **GPU hardware failure** — Physical defects in the graphics card cause scheduling errors.
3. **Video memory corruption** — VRAM errors cause the scheduler to read invalid data.
4. **Corrupted Windows graphics components** — DirectX or WDDM components are damaged.

## Solutions

### Solution 1: Clean Reinstall GPU Drivers

The video scheduler is tightly coupled with the GPU driver. A clean reinstall resolves most cases.

**Perform a clean driver reinstall with DDU:**

1. Download the latest GPU driver from your manufacturer (NVIDIA, AMD, or Intel).
2. Download [DDU (Display Driver Uninstaller)](https://www.guru3d.com/files-details/display-driver-uninstaller-download.html).
3. Boot into **Safe Mode**.
4. Run DDU and select **Clean and restart**.
5. After restart, install the fresh driver.
6. Restart again.

**NVIDIA specific — check driver version:**

```powershell
nvidia-smi --query-gpu=driver_version,name --format=csv,noheader
```

**AMD specific — check driver version:**

```powershell
Get-WmiObject Win32_VideoController | Where-Object {$_.Name -like "*AMD*"} | Select-Object Name, DriverVersion | Format-Table -AutoSize
```

Download the latest stable driver from:
- **NVIDIA**: [nvidia.com/drivers](https://www.nvidia.com/Download/index.aspx)
- **AMD**: [amd.com/support](https://www.amd.com/en/support)
- **Intel**: [intel.com/support](https://www.intel.com/content/www/us/en/support.html)

### Solution 2: Check GPU Hardware Health

If the BSOD persists across clean driver installs, the GPU hardware may be failing.

**Run a GPU stress test:**

1. Download **FurMark** or **Unigine Heaven**.
2. Run the test for 15-30 minutes.
3. Watch for visual artifacts, screen glitches, or crashes — these indicate hardware failure.

**Check GPU error logs:**

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=(Get-Date).AddDays(-30)} | Where-Object {$_.ProviderName -like "*nvlddmkm*" -or $_.ProviderName -like "*atikmpag*" -or $_.ProviderName -like "*dxgkrnl*"} | Select-Object TimeCreated, Id, Message | Format-Table -AutoSize
```

**Check GPU temperature under load:**

Use HWiNFO64 or GPU-Z to monitor GPU temperature during stress testing. Temperatures above 95°C indicate cooling problems.

### Solution 3: Disable GPU Overclocking

Overclocking beyond stable limits causes video scheduler errors.

**Reset GPU to stock clocks (NVIDIA):**

```powershell
nvidia-smi -rac
```

**Reset using overclocking software:**

1. Open MSI Afterburner, EVGA Precision, or AMD Radeon Software.
2. Click **Reset** or **Default**.
3. Apply changes and restart.

**Disable GPU hardware acceleration in applications:**

Some applications with hardware acceleration can trigger scheduler errors. Disable it in:
- Web browsers (Chrome, Edge, Firefox)
- Discord
- Microsoft Teams
- Video players

### Solution 4: Repair Windows Graphics Components

Corrupted DirectX or WDDM components can cause scheduler errors.

**Run System File Checker:**

```cmd
sfc /scannow
```

**Repair the Windows image:**

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

**Re-register DirectX components:**

```cmd
regsvr32 /u d3d11.dll
regsvr32 /i d3d11.dll
```

**Reset DirectX:**

1. Press `Win + R`, type `dxdiag`, and press Enter.
2. Check the **Display** tab for any reported errors.
3. If errors appear, reinstall DirectX from Microsoft's website.

### Solution 5: Check VRAM for Errors

Video RAM (VRAM) corruption can cause the scheduler to read invalid data.

**Note:** There is no built-in Windows tool to test VRAM. Use third-party tools:

1. **MemtestG80** or **MemtestCL** — Test VRAM for errors.
2. Download from [ocbase.com](https://www.ocbase.com/).
3. Run the test for at least 1 full pass.
4. Any errors indicate faulty VRAM.

If VRAM errors are found, the GPU likely needs replacement — VRAM is soldered to the card and not user-replaceable.

### Solution 6: Update Windows

Microsoft patches graphics components in Windows Update.

**Check for Windows updates:**

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate
Install-WindowsUpdate -AcceptAll -AutoReboot
```

Windows updates often include updated WDDM (Windows Display Driver Model) components that fix scheduler compatibility issues.

## Related Errors

- **[BSOD VIDEO_TDR_FAILURE]({{< relref "/windows/bsod-video-tdr-failure" >}})** — GPU hang timeout from the same graphics subsystem
- **[BSOD SYSTEM_SERVICE_EXCEPTION (win32kfull.sys)]({{< relref "/windows/bsod-system-service-exception2" >}})** — Graphics subsystem crash from win32kfull.sys
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Driver memory access violations from GPU drivers
- **[BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/windows/bsod-whea2" >}})** — Hardware error from GPU failure
