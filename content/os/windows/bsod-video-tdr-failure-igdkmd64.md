---
title: "[Solution] BSOD VIDEO_TDR_FAILURE igdkmd64.sys Intel GPU Fix"
description: "Fix Blue Screen VIDEO_TDR_FAILURE caused by igdkmd64.sys on Windows 10 and 11. Resolve Intel integrated graphics driver timeouts with driver updates and BIOS fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "intel", "igdkmd64", "gpu", "tdr", "integrated-graphics"]
weight: 5
---

# [Solution] BSOD VIDEO_TDR_FAILURE igdkmd64.sys Intel GPU Fix

VIDEO_TDR_FAILURE with `igdkmd64.sys` is a Blue Screen error caused by the Intel Graphics kernel-mode driver failing to respond to the Timeout Detection and Recovery (TDR) mechanism. This affects systems with Intel integrated graphics, which are present in most laptops and many desktops.

This error commonly occurs during video playback, web browsing with hardware acceleration, or when the integrated GPU shares system memory under heavy load.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: VIDEO_TDR_FAILURE
> What failed: igdkmd64.sys

`igdkmd64.sys` is Intel's kernel-mode display driver for integrated graphics. The driver manages GPU operations on Intel HD, UHD, and Iris graphics processors. When it fails to respond within the TDR timeout window, Windows crashes.

Common triggers include:

- **Outdated Intel GPU driver** — Driver incompatibility with Windows updates
- **Shared memory pressure** — Integrated GPU shares RAM with the system; high memory usage causes GPU hangs
- **BIOS settings** — Incorrect GPU memory allocation in BIOS
- **Dual GPU conflicts** — Conflicts between Intel integrated and NVIDIA/AMD discrete GPUs

## Common Causes

1. **Outdated or corrupted Intel GPU driver** — The most common cause, especially on laptops.
2. **Shared memory pressure** — The integrated GPU has no dedicated VRAM and can starve under memory pressure.
3. **BIOS GPU memory allocation** — Insufficient DVMT pre-allocated memory in BIOS.
4. **Dual GPU conflicts** — Laptops with both Intel and NVIDIA/AMD GPUs experience driver switching issues.
5. **Overheating** — Laptop cooling systems that are clogged or failing.

## How to Fix

### Solution 1: Update Intel GPU Driver

**Check current driver version:**

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*Intel*" } | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest driver from [intel.com/support](https://www.intel.com/content/www/us/en/support.html):

1. Enter your GPU model or let the Intel Driver Support Assistant detect it.
2. Download and install the recommended driver.
3. Restart your computer.

### Solution 2: Increase DVMT Pre-Allocated Memory in BIOS

Integrated GPUs use system RAM as video memory. If not enough is pre-allocated, the driver can crash:

1. Restart your computer and enter **BIOS/UEFI** (usually `Del`, `F2`, or `F12` during boot).
2. Navigate to **Advanced > Graphics Configuration** or **Video Configuration**.
3. Find **DVMT Pre-Allocated** or **Internal Graphics Memory Size**.
4. Set to **128MB** or **256MB** (or the maximum available).
5. Save and exit.

### Solution 3: Disable Hardware Acceleration in Browsers

Browser hardware acceleration frequently triggers igdkmd64.sys crashes on Intel GPUs:

**Chrome:**
1. Open **Settings > System**.
2. Toggle off **Use hardware acceleration when available**.
3. Restart Chrome.

**Firefox:**
1. Open **Settings > General > Performance**.
2. Uncheck **Use recommended performance settings**.
3. Uncheck **Use hardware acceleration when available**.
4. Restart Firefox.

### Solution 4: Resolve Dual GPU Conflicts (Laptops)

Laptops with both Intel and NVIDIA/AMD GPUs use switching technology (Optimus, Enduro) that can cause driver conflicts:

1. Open **Device Manager**.
2. Expand **Display adapters**.
3. Right-click the Intel GPU and select **Disable device** (temporarily for testing).
4. If the BSOD stops, the issue is with the Intel driver or switching mechanism.

**Update both GPU drivers:**

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

Ensure both Intel and the discrete GPU have the latest drivers installed.

### Solution 5: Clean Install Intel Driver with DDU

1. Download **DDU** from [wagnardsoft.com](https://www.wagnardsoft.com/display-driver-uninstaller-DDU).
2. Download the latest Intel GPU driver.
3. Boot into **Safe Mode**.
4. Run DDU and select **Clean and restart**.
5. Install the Intel driver after reboot.

### Solution 6: Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the most recent `.dmp` file in **WinDbg** and run `!analyze -v`. The `igdkmd64` module name confirms the Intel GPU driver as the culprit.

## Related Errors

- **[BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/windows/bsod-video-tdr-failure-nvlddmkm2" >}})** — NVIDIA GPU version of this error
- **[BSOD VIDEO_TDR_FAILURE atikmpag.sys]({{< relref "/windows/bsod-video-tdr-failure-atikmpag" >}})** — AMD GPU version of this error
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — Generic system thread exception error
