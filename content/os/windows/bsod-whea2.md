---
title: "[Solution] BSOD WHEA_UNCORRECTABLE_ERROR (CPU/GPU) Windows 11/10 — Fixed"
description: "Fix Blue Screen WHEA_UNCORRECTABLE_ERROR on Windows 10 and 11. Resolve stop code 0x124 with CPU and GPU hardware diagnostics and temperature fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD WHEA_UNCORRECTABLE_ERROR (CPU/GPU) Windows 11/10 — Fixed

WHEA_UNCORRECTABLE_ERROR is a critical Blue Screen of Death error with stop code `0x00000124`. It indicates that the Windows Hardware Error Architecture (WHEA) detected an uncorrectable hardware error from the CPU, GPU, RAM, motherboard, or other critical component. Unlike correctable errors (which can be logged and ignored), uncorrectable errors force an immediate system crash.

This BSOD is almost always a hardware problem. It typically points to CPU instability (overheating, overvolting, failing silicon), GPU failure, or motherboard issues. Software fixes are limited — the root cause is physical hardware.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: WHEA_UNCORRECTABLE_ERROR

WHEA is Microsoft's standardized framework for reporting hardware errors. When a CPU detects a machine check exception (MCE), a GPU reports a critical error, or memory encounters uncorrectable ECC errors, WHEA captures the event and, if the error is severe enough, triggers this BSOD.

Common scenarios for this BSOD:

- **With overclocked CPUs** — Exceeding stable voltage or frequency limits
- **During heavy CPU/GPU load** — Gaming, rendering, or stress testing
- **With overheating components** — CPU or GPU thermal throttling fails
- **With failing hardware** — Degrading CPU, GPU, or motherboard components
- **After BIOS changes** — Modified CPU voltage or memory timings

## Common Causes

1. **CPU instability** — Overclocking, undervolting, or failing CPU silicon causes machine check exceptions.
2. **GPU hardware failure** — The graphics card has physical defects or overheating issues.
3. **Overheating** — CPU or GPU temperatures exceed safe operating limits.
4. **Failing motherboard** — VRM (Voltage Regulator Module) issues or capacitor degradation.

## Solutions

### Solution 1: Reset CPU to Stock Settings

Overclocking is the most common cause. Return the CPU to its default specifications.

**Reset BIOS to defaults:**

1. Restart and enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Select **Load Optimized Defaults** or **Load Fail-Safe Defaults**.
3. Save and exit.

**Reset software overclocking:**

1. Open Intel XTU, Ryzen Master, or your overclocking tool.
2. Click **Reset** or **Default**.
3. Apply changes and restart.

**Check current CPU clock speed:**

```powershell
Get-CimInstance -ClassName Win32_Processor | Select-Object Name, CurrentClockSpeed, MaxClockSpeed, NumberOfCores, NumberOfLogicalProcessors | Format-Table -AutoSize
```

If `CurrentClockSpeed` exceeds `MaxClockSpeed`, the CPU is overclocked.

### Solution 2: Monitor and Fix CPU/GPU Temperatures

Overheating is the second most common cause of this BSOD.

**Check CPU temperature (requires third-party tools):**

The best tools for temperature monitoring are:
- **HWiNFO64** — Comprehensive hardware monitoring
- **Core Temp** — Lightweight CPU temperature monitor
- **Open Hardware Monitor** — Open-source hardware monitor

**Safe temperature ranges:**

- **CPU idle**: 30-45°C
- **CPU under load**: 60-85°C (above 90°C is dangerous)
- **GPU idle**: 30-45°C
- **GPU under load**: 65-85°C (above 95°C is dangerous)

**Physical fixes for overheating:**

1. Clean dust from CPU cooler and GPU heatsinks.
2. Ensure all fans are spinning properly.
3. Check that the CPU cooler is properly mounted with adequate thermal paste.
4. Improve case airflow by adding or repositioning fans.
5. For laptops, clean the vents and consider a cooling pad.

### Solution 3: Run CPU Stress Tests

Test CPU stability to identify if the processor is the problem.

**Run a built-in stress test with PowerShell:**

```powershell
# Run a basic CPU stress test using built-in tools
Start-Process "cmd" -ArgumentList "/c start /high cmd /c for /L %i in (1,1,0) do echo test > nul" -WindowStyle Hidden
```

**Recommended stress testing tools:**

1. **Prime95** — The gold standard for CPU stability testing. Run the "Small FFTs" test for 30 minutes.
2. **Intel Burn Test** — Aggressive CPU stress test.
3. **OCCT** — Comprehensive CPU, GPU, and PSU testing.

If the CPU fails any stress test, it is unstable — either due to overclocking, voltage issues, or hardware degradation.

### Solution 4: Check GPU Hardware

GPU failure can also trigger WHEA errors.

**Check GPU temperature and load:**

```powershell
Get-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, AdapterRAM | Format-Table -AutoSize
```

**Run GPU stress tests:**

1. Download **FurMark** or **Unigine Heaven**.
2. Run the stress test for 15-30 minutes.
3. Watch for artifacts, visual glitches, or crashes.

If the GPU fails stress tests, it may need replacement.

**Reset GPU to stock clocks:**

```powershell
nvidia-smi -rac
```

### Solution 5: Check for Failing Motherboard Components

VRM failure or capacitor degradation can cause unstable voltage delivery to the CPU.

**Visual inspection:**

1. Open the computer case.
2. Look for bulging or leaking capacitors near the CPU socket.
3. Check that all power connectors (24-pin ATX, 8-pin CPU) are firmly seated.
4. Look for burn marks or discoloration on the motherboard.

**Run system stability tests:**

If the system passes CPU and GPU stress tests individually but crashes under combined load, the PSU or motherboard VRM may be failing.

### Solution 6: Check Event Viewer for Hardware Errors

Windows logs WHEA errors with detailed information.

**Find WHEA errors in Event Viewer:**

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=41} -MaxEvents 10 | Select-Object TimeCreated, Id, Message | Format-Table -AutoSize
```

**Check for machine check exceptions:**

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'} -MaxEvents 10 | Select-Object TimeCreated, Id, Message | Format-Table -AutoSize
```

The error details often identify the specific hardware component that failed (CPU Core, GPU, Memory Channel, etc.).

## Related Errors

- **[BSOD VIDEO_TDR_FAILURE]({{< relref "/windows/bsod-video-tdr-failure" >}})** — GPU timeout from the same hardware failure
- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault2" >}})** — Memory errors from faulty RAM or CPU memory controller
- **[BSOD SYSTEM_PFN_LIST_CORRUPTED]({{< relref "/windows/bsod-system-pfn-corrupted" >}})** — Memory management corruption from hardware failure
- **[BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — Memory access violations from hardware instability
