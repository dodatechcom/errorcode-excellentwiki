---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED nvlddmkm.sys NVIDIA Fix"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED caused by nvlddmkm.sys on Windows 10 and 11. Resolve NVIDIA driver crashes with clean installs, DDU, and driver rollbacks."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED nvlddmkm.sys NVIDIA Fix

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED with `nvlddmkm.sys` as the failing driver is a critical Blue Screen of Death error indicating that the NVIDIA kernel-mode driver generated an unhandled exception. This is one of the most common GPU-related BSODs on Windows 10 and 11.

This error typically appears during GPU-intensive tasks such as gaming, video editing, or running multiple monitors. The system crashes to prevent hardware damage when the NVIDIA driver encounters a fatal error in kernel mode.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
> What failed: nvlddmkm.sys

The `nvlddmkm.sys` file is NVIDIA's Display Driver Kernel Mode component. When this driver executes an invalid operation or encounters memory corruption, Windows halts the system immediately. Common triggers include:

- **GPU overheating** — Thermal throttling fails and the driver crashes under load
- **Overclocked GPU** — Unstable memory or core clock speeds cause driver exceptions
- **Corrupted driver installation** — Partial driver updates or failed installations
- **Faulty GPU hardware** — Failing VRAM or GPU die causes unpredictable behavior

## Common Causes

1. **Corrupted or outdated NVIDIA driver** — The most common cause, especially after a failed driver update.
2. **GPU overheating** — Inadequate cooling leads to thermal shutdown of the GPU driver.
3. **Unstable overclock** — Memory or core clock speeds exceed stable limits.
4. **Faulty GPU hardware** — Degraded VRAM or power delivery issues.
5. **Windows update conflicts** — A Windows update overwrites or conflicts with the NVIDIA driver.

## How to Fix

### Solution 1: Clean NVIDIA Driver Installation with DDU

The most reliable fix is a complete driver removal and clean reinstall using Display Driver Uninstaller:

1. Download **DDU** from [wagnardsoft.com](https://www.wagnardsoft.com/display-driver-uninstaller-DDU).
2. Download the latest NVIDIA driver from [nvidia.com/drivers](https://www.nvidia.com/Download/index.aspx).
3. Disconnect from the internet to prevent Windows from auto-installing a driver.
4. Boot into **Safe Mode**:
   ```cmd
   shutdown /r /o /t 0
   ```
   Navigate to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
5. Run DDU and select **Clean and restart**.
6. After reboot, install the NVIDIA driver you downloaded.

**Check your current NVIDIA driver version:**

```powershell
Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*NVIDIA*" } | Select-Object Name, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Solution 2: Monitor GPU Temperature

Overheating is a frequent cause of nvlddmkm.sys crashes under load.

**Check GPU temperature in real time:**

```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSAcpi_ThermalZoneTemperature | Select-Object InstanceName, CurrentTemperature
```

**Check GPU temperature with NVIDIA SMI (if installed):**

```cmd
nvidia-smi --query-gpu=name,temperature.gpu,fan.speed,power.draw --format=csv
```

If temperatures exceed **85°C** under load:
- Clean dust from GPU heatsinks and case fans
- Replace thermal paste on the GPU if it is more than 3 years old
- Improve case airflow with additional fans

### Solution 3: Reset GPU Overclock

If you have overclocked your GPU using MSI Afterburner or similar tools:

1. Open **MSI Afterburner** or your overclocking utility.
2. Reset all settings to **defaults** (usually a circular arrow icon).
3. Apply and save.

**Check for unstable overclock artifacts:**

```cmd
nvidia-smi --query-gpu=clocks.gr,clocks.mem --format=csv
```

Compare against your GPU's stock clock speeds listed on the manufacturer's website.

### Solution 4: Roll Back the NVIDIA Driver

If the BSOD started after a driver update, roll back to the previous version:

1. Right-click the **Start** button and select **Device Manager**.
2. Expand **Display adapters**.
3. Right-click your NVIDIA GPU and select **Properties**.
4. Go to the **Driver** tab and click **Roll Back Driver**.
5. Select a reason and follow the prompts.
6. Restart your computer.

### Solution 5: Test GPU Hardware

If software fixes do not resolve the issue, the GPU hardware may be failing.

**Run a GPU stress test:**

1. Download **FurMark** from [geeks3d.com](https://www.geeks3d.com/furmark/).
2. Run the stress test for 15–30 minutes.
3. Watch for artifacts, flickering, or system crashes.

**Check for VRAM errors:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. After the test completes, check Event Viewer under **Windows Logs > System** for memory errors.

### Solution 6: Analyze the Minidump

Identify the exact point of failure in the NVIDIA driver:

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the most recent `.dmp` file in **WinDbg** and run:

```
!analyze -v
```

Look for `nvlddmkm` in the **MODULE_NAME** and **IMAGE_NAME** fields. A faulting offset in the driver confirms a driver or hardware issue.

## Related Errors

- **[BSOD VIDEO_TDR_FAILURE nvlddmkm.sys]({{< relref "/windows/bsod-video-tdr-failure" >}})** — NVIDIA driver timeout detection and recovery failure
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — Generic SYSTEM_THREAD_EXCEPTION error with various drivers
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception" >}})** — Another kernel-mode exception error with similar driver causes
