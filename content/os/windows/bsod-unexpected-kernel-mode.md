---
title: "[Solution] BSOD UNEXPECTED_KERNEL_MODE_TRAP — 0x7F Windows 11/10"
description: "Fix Blue Screen UNEXPECTED_KERNEL_MODE_TRAP stop code 0x7F on Windows 10 and 11. Resolve hardware failures and kernel trap exceptions."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "unexpected-kernel-mode", "trap", "hardware", "stop-0x7f"]
weight: 5
---

# BSOD UNEXPECTED_KERNEL_MODE_TRAP — 0x7F

The `UNEXPECTED_KERNEL_MODE_TRAP` stop code `0x7F` means the CPU generated an unexpected trap (exception) that the kernel was not prepared to handle. This is most commonly caused by hardware failures, particularly RAM or CPU issues.

## Common Causes

- **Failing RAM** — Memory errors cause the CPU to generate unexpected exceptions.
- **CPU overheating** — Thermal throttling or shutdown causes the CPU to generate traps.
- **Faulty CPU or motherboard** — Hardware defects cause unpredictable CPU behavior.
- **Overclocking instability** — Aggressive CPU or RAM clocks cause intermittent exceptions.
- **Driver causing hardware-level error** — A driver triggers an instruction that causes a CPU trap.

## How to Fix

### Test RAM Thoroughly

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Run MemTest86 for at least 8 passes.

### Monitor CPU Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Ensure CPU stays below 85°C under load. Clean heatsink and replace thermal paste if needed.

### Reset BIOS to Defaults

Enter BIOS/UEFI and load optimized defaults. Disable all overclocking:
- CPU core multiplier
- RAM XMP/DOCP profile
- BCLK frequency

### Check Event Viewer for Hardware Errors

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*WHEA*" -or $_.Id -eq 18 } | Select-Object -First 10 TimeCreated, Message | Format-Table -Wrap
```

### Run CPU Stress Test

Use Prime95 or Intel Burn Test to stress the CPU and check for errors. Watch temperatures closely.

### Check for Driver Verifier

```cmd
verifier /query
```

If Driver Verifier is running, it may be causing additional traps:

```cmd
verifier /reset
shutdown /r /t 0
```

### Update BIOS

Download and install the latest BIOS from the motherboard manufacturer.

## Examples

```text
UNEXPECTED_KERNEL_MODE_TRAP (7f)
This means a trap occurred in kernel mode, and it's not caught by the kernel
error handler. A hardware error is the most common cause.

Arg1: 0000000000000008, Exception double fault
```

## Related Errors

- [BSOD UNEXPECTED_KERNEL_MODE_TRAP WHEA]({{< relref "/os/windows/bsod-unexpected-kernel-mode2" >}}) — WHEA-related trap
- [BSOD UNEXPECTED_KERNEL_MODE_TRAP nvlddmkm.sys]({{< relref "/os/windows/bsod-unexpected-kernel-mode3" >}}) — GPU driver trap
- [BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/os/windows/bsod-whea-uncorrectable-error" >}}) — Hardware error
