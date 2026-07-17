---
title: "[Solution] BSOD UNEXPECTED_KERNEL_MODE_TRAP CPU Double Fault Fix"
description: "Fix Blue Screen UNEXPECTED_KERNEL_MODE_TRAP caused by CPU double faults on Windows 10 and 11. Resolve CPU errors with overclock resets, thermal fixes, and hardware diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD UNEXPECTED_KERNEL_MODE_TRAP CPU Double Fault Fix

UNEXPECTED_KERNEL_MODE_TRAP caused by a CPU double fault is a critical Blue Screen indicating that the CPU generated a fault while trying to handle a previous fault. This is a severe hardware error that typically points to CPU instability, overheating, or memory corruption.

This BSOD often occurs during heavy CPU workloads, overclocking, or when the CPU encounters an unrecoverable error condition.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: UNEXPECTED_KERNEL_MODE_TRAP

A double fault occurs when the CPU encounters an exception while trying to handle a previous exception. The CPU cannot recover from this state and triggers a triple fault, which causes Windows to crash.

Common triggers include:

- **Unstable CPU overclock** — Overclocked beyond stable voltage limits
- **CPU overheating** — Thermal protection causing the CPU to malfunction
- **Faulty RAM** — Memory errors causing exception cascades
- **Motherboard VRM failure** — Unstable power delivery to the CPU

## Common Causes

1. **Unstable CPU overclock** — Clock speeds or voltage beyond stable limits.
2. **CPU overheating** — Thermal shutdown causing double faults.
3. **Faulty RAM** — Memory errors causing cascading exceptions.
4. **Motherboard issues** — Faulty VRM or capacitors.
5. **BIOS bugs** — Outdated BIOS with incorrect CPU configuration.

## How to Fix

### Solution 1: Reset CPU to Stock Settings

**For BIOS overclocks:**

1. Enter BIOS/UEFI during boot.
2. Load **Optimized Defaults** or **Fail-Safe Defaults**.
3. Save and exit.

**For software overclocks:**

1. Open Intel XTU or AMD Ryzen Master.
2. Click **Reset to Default**.
3. Apply and restart.

### Solution 2: Check CPU Temperature

```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSAcpi_ThermalZoneTemperature | Select-Object InstanceName, CurrentTemperature
```

Keep temperatures below **85°C** under load. Reapply thermal paste if the CPU cooler is more than 3 years old.

### Solution 3: Run Memory Diagnostics

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use [MemTest86](https://www.memtest86.com/) for extended testing (4+ passes).

### Solution 4: Update BIOS

1. Check your motherboard manufacturer's website.
2. Download and install the latest BIOS version.
3. BIOS updates often fix CPU power management and stability issues.

### Solution 5: Check Power Supply

1. Ensure PSU wattage meets CPU requirements.
2. Check that the 8-pin CPU power connector is firmly seated.
3. Try a different PSU if possible.

### Solution 6: Reset CMOS

1. Shut down and unplug the computer.
2. Locate the CMOS clear jumper on the motherboard.
3. Move the jumper to the clear position for 30 seconds.
4. Move it back and restart.

## Related Errors

- **[BSOD UNEXPECTED_KERNEL_MODE_TRAP WHEA]({{< relref "/windows/bsod-unexpected-kernel-mode-whea" >}})** — WHEA hardware error variant
- **[BSOD WHEA_UNCORRECTABLE_ERROR CPU]({{< relref "/windows/bsod-whea-uncorrectable-cpu" >}})** — CPU voltage related WHEA error
- **[BSOD CLOCK_WATCHDOG_TIMEOUT]({{< relref "/windows/bsod-clock-watchdog-timeout" >}})** — CPU watchdog timeout
