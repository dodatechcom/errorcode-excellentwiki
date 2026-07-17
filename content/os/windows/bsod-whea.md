---
title: "[Solution] BSOD WHEA_UNCORRECTABLE_ERROR Windows 11/10 — Fixed"
description: "Fix Blue Screen WHEA_UNCORRECTABLE_ERROR error on Windows 10 and 11. Reset overclocking, update BIOS, test CPU and RAM, and check hardware to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD WHEA_UNCORRECTABLE_ERROR Windows 11/10 — Fixed

WHEA_UNCORRECTABLE_ERROR is a critical Blue Screen of Death error with stop code `0x00000124`. It occurs when the Windows Hardware Error Architecture (WHEA) detects a hardware error that cannot be corrected. The system has encountered a fatal hardware fault — typically in the CPU, RAM, motherboard, or power delivery — and halts immediately to prevent data corruption.

This BSOD affects both Windows 10 and 11 and is one of the most hardware-focused blue screens. It almost always points to a physical component failure or extreme overclocking instability.

## Common Causes

- **CPU overclocking instability** — The most common cause. Aggressive CPU, cache, or memory overclocks push hardware beyond its error-correcting capabilities.
- **Failing CPU or motherboard** — Physical degradation of processor cores, VRMs, or motherboard traces causes uncorrectable hardware faults.
- **Faulty RAM** — Memory errors that exceed the error-correcting code (ECC) capability of the system.
- **Inadequate power delivery** — PSU instability or failing VRM components cause voltage irregularities to the CPU.

## How to Fix

### Remove All Overclocking

Reset every overclocked component to stock settings.

**Reset BIOS to defaults:**

1. Restart and enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Select **Load Optimized Defaults** or **Load Fail-Safe Defaults**.
3. Disable XMP/DOCP/EXPO memory profiles.
4. Save and exit.

**Verify stock settings:**

```powershell
Get-CimInstance -ClassName Win32_Processor | Select-Object Name, CurrentClockSpeed, MaxClockSpeed, CurrentVoltage | Format-Table -AutoSize
```

If the current clock speed exceeds the rated max, the CPU is still overclocked.

**Reset GPU overclock as well:**

```powershell
nvidia-smi -rac
```

### Update BIOS/UEFI

A BIOS update can fix CPU microcode issues and hardware error handling:

```cmd
wmic baseboard get product,Manufacturer,version
```

Visit your motherboard manufacturer's website and download the latest BIOS. Follow the flashing instructions exactly and ensure uninterrupted power during the update.

### Check CPU and System Temperatures

```powershell
Get-WmiObject -Namespace root\wmi -Class MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Values are in tenths of Kelvin. Subtract 2732 and divide by 10 for Celsius.

**Normal operating temperatures:**
- **CPU idle**: 30–45°C
- **CPU under load**: 60–85°C
- **Danger zone**: Above 95°C

Clean the CPU cooler, reapply thermal paste if needed, and ensure all case fans are operational.

### Test RAM

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 from a bootable USB for thorough testing with at least 8 passes. WHEA errors can be caused by RAM that fails at extreme frequencies but appears stable at lower speeds.

### Check Power Supply

A failing PSU causes voltage irregularities that trigger WHEA errors:

1. Monitor the +12V, +5V, and +3.3V rails using HWMonitor or similar tools.
2. Voltages should remain within ±5% of their rated values.
3. If voltages fluctuate significantly under load, replace the PSU.

### Update Windows

Windows updates include hardware-related fixes and microcode patches:

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

### Test for Hardware Failure

If the error persists at stock settings with a fresh BIOS:

1. Run a CPU stress test (Prime95, AIDA64) for at least 1 hour.
2. Run MemTest86 for at least 8 passes.
3. If the system crashes during stress tests at stock settings, the CPU, motherboard, or PSU is likely failing.
4. Test with known-good components to isolate the faulty hardware.

## Examples

This error commonly occurs in these scenarios:

- **With extreme CPU overclocks** — Pushing CPU frequencies beyond the silicon's stable limits.
- **During sustained heavy workloads** — Extended rendering, compilation, or scientific computing exposes hardware instabilities.
- **After adding new RAM** — New memory modules that are incompatible or run at unstable timings.
- **With aging hardware** — CPU VRMs or motherboard traces degrade over time, causing intermittent faults.

## Related Errors

- [BSOD CLOCK_WATCHDOG_TIMEOUT]({{< relref "/os/windows/bsod-clock-watchdog-timeout" >}}) — Clock interrupt timeout from CPU issues
- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — Invalid memory access from hardware instability
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault" >}}) — Memory page fault from faulty RAM
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel exception from hardware or driver failure
