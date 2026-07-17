---
title: "[Solution] BSOD CLOCK_WATCHDOG_TIMEOUT Windows 11/10 — Fixed"
description: "Fix Blue Screen CLOCK_WATCHDOG_TIMEOUT error on Windows 10 and 11. Update BIOS, check CPU health, and disable overclocking to resolve this processor-related stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD CLOCK_WATCHDOG_TIMEOUT Windows 11/10 — Fixed

CLOCK_WATCHDOG_TIMEOUT is a critical Blue Screen of Death error with stop code `0x00000101`. It occurs when a designated processor core fails to service the clock interrupt within the expected timeout period. The Windows kernel uses clock interrupts for scheduling and timing — when a processor stops responding to these interrupts, the system crashes to prevent indefinite hangs.

This BSOD affects both Windows 10 and 11 and is closely tied to CPU issues, motherboard firmware, and overclocking instability.

## Common Causes

- **CPU overclocking instability** — Overclocked processors fail to respond to clock interrupts at extreme frequencies.
- **Outdated or corrupted BIOS/UEFI** — Motherboard firmware bugs in CPU power management or interrupt handling.
- **CPU hardware failure** — Degraded processor cores that intermittently stop responding.
- **Incompatible CPU microcode** — A Windows update installs microcode that conflicts with the specific CPU model.

## How to Fix

### Disable CPU Overclocking

This is the most common fix. Reset all CPU and memory overclocking settings.

**Reset BIOS to defaults:**

1. Restart and enter BIOS/UEFI (press `Del`, `F2`, or `F12` during boot).
2. Select **Load Optimized Defaults** or **Load Fail-Safe Defaults**.
3. Save and exit.

**Reset software overclocking:**

```powershell
# Check current CPU clock speed
Get-CimInstance -ClassName Win32_Processor | Select-Object Name, CurrentClockSpeed, MaxClockSpeed, NumberOfCores | Format-Table -AutoSize
```

If `CurrentClockSpeed` exceeds `MaxClockSpeed`, the CPU is overclocked. Reset using Intel XTU, Ryzen Master, or BIOS settings.

### Update BIOS/UEFI

An outdated BIOS can cause clock interrupt handling bugs:

```cmd
wmic baseboard get product,Manufacturer,version
```

Visit your motherboard manufacturer's website (ASUS, MSI, Gigabyte, ASRock, Dell, HP) and download the latest BIOS version. Follow the manufacturer's flashing instructions exactly — do not interrupt the process.

### Check CPU Temperature

Overheating causes cores to throttle and miss clock interrupts:

```powershell
Get-WmiObject -Namespace root\wmi -Class MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

The value is in tenths of a Kelvin. Subtract 2732 and divide by 10 for Celsius. Normal operating temperature under load should be below 85°C.

Clean dust from the CPU cooler and heatsink. Ensure the thermal paste is not dried out. Verify that the CPU fan is spinning at the correct speed.

### Update Windows and CPU Microcode

Windows updates include CPU microcode patches that fix known processor bugs:

```powershell
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

### Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Test for CPU Hardware Failure

If overclocking is disabled, BIOS is updated, and temperatures are normal:

1. Run a CPU stress test (Prime95, AIDA64) for at least 30 minutes.
2. Monitor for crashes, thermal throttling, or computation errors.
3. If the CPU consistently fails stress tests at stock settings, the processor may be physically failing.

## Examples

This error commonly occurs in these scenarios:

- **With aggressive CPU overclocks** — Pushing CPU frequencies beyond stable limits causes cores to miss clock interrupts.
- **After BIOS update** — A new BIOS version changes CPU power management behavior.
- **During heavy multi-threaded workloads** — All cores under maximum stress expose CPU instabilities.
- **With aging hardware** — Degraded CPU or motherboard components cause intermittent interrupt failures.

## Related Errors

- [BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/os/windows/bsod-whea-uncorrectable-error" >}}) — Another CPU and hardware-related uncorrectable error
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel exception from CPU or driver issues
- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — Invalid memory access often caused by overclocking
- [BSOD DPC Watchdog Violation]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — Another watchdog timeout BSOD
