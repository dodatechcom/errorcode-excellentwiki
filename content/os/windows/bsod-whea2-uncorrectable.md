---
title: "[Solution] BSOD WHEA_UNCORRECTABLE_ERROR — 0x124 CPU/GPU Voltage Windows 11/10"
description: "Fix Blue Screen WHEA_UNCORRECTABLE_ERROR stop code 0x124 caused by CPU/GPU voltage issues on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD WHEA_UNCORRECTABLE_ERROR — 0x124 CPU/GPU Voltage

The `WHEA_UNCORRECTABLE_ERROR` stop code `0x124` with CPU/GPU voltage involvement indicates the hardware error is caused by insufficient or unstable voltage delivery to the CPU or GPU. This is a power delivery issue that causes the processor to generate machine check exceptions.

## Common Causes

- **Insufficient CPU voltage** — Undervolting causes CPU instability under load.
- **PSU failing or undersized** — Power supply cannot deliver stable voltage to CPU/GPU.
- **Motherboard VRM failure** — Faulty voltage regulator modules cause unstable power delivery.
- **CPU/GPU degradation** — Aging processors require higher voltage to maintain stability.
- **Aggressive power limit** — BIOS power limits prevent adequate voltage during boost.

## How to Fix

### Reset BIOS to Defaults

Load optimized defaults in BIOS/UEFI to restore default voltages.

### Check CPU Voltage Settings

In BIOS, verify:
- CPU core voltage is set to Auto
- LLC (Load-Line Calibration) is at default
- No manual undervolt is applied

### Check PSU Health

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Test with a known-good PSU if possible.

### Monitor Voltages Under Load

Use HWiNFO or similar tool to monitor:
- CPU Vcore under load
- +12V rail voltage
- GPU power delivery

### Update BIOS

Download the latest BIOS from the motherboard manufacturer for improved voltage regulation.

### Check WHEA Error Details

```powershell
Get-WinEvent -LogName System | Where-Object { $_.Id -eq 18 } | Select-Object -First 5 TimeCreated, Message | Format-Table -Wrap
```

### Disable Overclocking

Remove all CPU, GPU, and RAM overclocks.

## Examples

```text
WHEA_UNCORRECTABLE_ERROR (124)
A fatal hardware error has occurred.

Arg1: 0000000000000000, Machine Check Exception
Arg2: ffffc80123456780, WHEA_ERROR_RECORD structure
Arg3: be00000000000000, MCi_STATUS MSR
```

## Related Errors

- [BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/os/windows/bsod-whea-uncorrectable-error" >}}) — General WHEA error
- [BSOD UNEXPECTED_KERNEL_MODE_TRAP WHEA]({{< relref "/os/windows/bsod-unexpected-kernel-mode2" >}}) — WHEA trap
- [BSOD CLOCK_WATCHDOG_TIMEOUT]({{< relref "/os/windows/bsod-clock-watchdog-timeout" >}}) — Clock watchdog timeout
