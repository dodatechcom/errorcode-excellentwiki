---
title: "[Solution] BSOD UNEXPECTED_KERNEL_MODE_TRAP WHEA Error Fix"
description: "Fix Blue Screen UNEXPECTED_KERNEL_MODE_TRAP caused by WHEA errors on Windows 10 and 11. Resolve hardware error traps with BIOS updates, hardware diagnostics, and cooling fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "unexpected-kernel-mode", "whea", "hardware", "trap"]
weight: 5
---

# [Solution] BSOD UNEXPECTED_KERNEL_MODE_TRAP WHEA Error Fix

UNEXPECTED_KERNEL_MODE_TRAP caused by WHEA errors is a critical Blue Screen indicating that the CPU encountered a hardware trap that the kernel could not handle. This error is reported through the Windows Hardware Error Architecture (WHEA).

This BSOD typically indicates a serious hardware problem with the CPU, motherboard, or memory. It requires hardware diagnostics to identify the root cause.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: UNEXPECTED_KERNEL_MODE_TRAP

A kernel mode trap is an interrupt that switches the processor from user mode to kernel mode for handling. When the trap cannot be handled (often due to a hardware error reported by WHEA), Windows crashes.

Common triggers include:

- **CPU hardware error** — Processor internal error detected by WHEA
- **Memory errors** — RAM failures causing trap exceptions
- **Motherboard issues** — Faulty VRM or capacitors causing unstable operation
- **Overheating** — Thermal shutdown of CPU components

## Common Causes

1. **CPU hardware failure** — Processor silicon degradation or failure.
2. **Memory errors** — Faulty RAM causing trap exceptions.
3. **Motherboard issues** — Faulty VRM, capacitors, or traces.
4. **Overheating** — Insufficient cooling causing thermal issues.
5. **BIOS bugs** — Outdated BIOS with incorrect hardware configuration.

## How to Fix

### Solution 1: Update BIOS

1. Check your motherboard manufacturer's website for BIOS updates.
2. Download and install the latest version.
3. BIOS updates often fix hardware initialization bugs.

### Solution 2: Run Memory Diagnostics

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use [MemTest86](https://www.memtest86.com/) for extended testing.

### Solution 3: Check CPU Temperature

```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSAcpi_ThermalZoneTemperature | Select-Object InstanceName, CurrentTemperature
```

Ensure temperatures are within normal ranges. Reapply thermal paste if needed.

### Solution 4: Reset CPU to Stock Settings

If overclocked:

1. Enter BIOS/UEFI.
2. Load **Optimized Defaults**.
3. Save and exit.

### Solution 5: Check Hardware Connections

1. Reseat CPU cooler (check mounting pressure).
2. Reseat RAM modules.
3. Check all power connectors (24-pin, 8-pin CPU).
4. Verify no loose cables inside the case.

### Solution 6: Check WHEA Error Events

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*WHEA*" -or $_.Id -eq 41 } | Select-Object -First 10 TimeCreated, Id, Message | Format-List
```

## Related Errors

- **[BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/windows/bsod-whea-uncorrectable-error" >}})** — WHEA uncorrectable hardware error
- **[BSOD UNEXPECTED_KERNEL_MODE_TRAP CPU]({{< relref "/windows/bsod-unexpected-kernel-mode-cpu" >}})** — CPU double fault variant
- **[BSOD CLOCK_WATCHDOG_TIMEOUT]({{< relref "/windows/bsod-clock-watchdog-timeout" >}})** — CPU watchdog timeout
