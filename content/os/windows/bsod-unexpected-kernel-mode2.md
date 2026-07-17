---
title: "[Solution] BSOD UNEXPECTED_KERNEL_MODE_TRAP — 0x7F WHEA Windows 11/10"
description: "Fix Blue Screen UNEXPECTED_KERNEL_MODE_TRAP stop code 0x7F caused by WHEA hardware error on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD UNEXPECTED_KERNEL_MODE_TRAP — 0x7F WHEA

The `UNEXPECTED_KERNEL_MODE_TRAP` stop code `0x7F` with WHEA (Windows Hardware Error Architecture) involvement indicates the CPU encountered a hardware error that triggered an unexpected trap. This combines CPU exception handling with hardware error reporting, typically pointing to CPU or motherboard issues.

## Common Causes

- **CPU hardware error** — Physical CPU defects cause the WHEA subsystem to report uncorrectable errors.
- **Motherboard VRM failure** — Faulty voltage regulation causes unstable CPU operation.
- **PCIe device errors** — A PCIe device generates machine check exceptions handled by WHEA.
- **Overheating CPU** — Extreme temperatures cause hardware errors reported through WHEA.

## How to Fix

### Check WHEA Error Source

```powershell
Get-WinEvent -LogName System | Where-Object { $_.Id -eq 18 -or $_.ProviderName -like "*WHEA*" } | Select-Object -First 10 TimeCreated, Message | Format-Table -Wrap
```

### Reset BIOS to Defaults

Load optimized defaults in BIOS/UEFI and disable all overclocking.

### Monitor CPU Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Clean heatsink and replace thermal paste if needed.

### Test RAM

```cmd
mdsched.exe
```

Run MemTest86 for extended testing.

### Check PCIe Devices

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*WHEA*" } | Where-Object { $_.Message -like "*PCI*" } | Select-Object -First 5 TimeCreated, Message | Format-Table -Wrap
```

Reseat PCIe cards and check for defective devices.

### Update BIOS

Download the latest BIOS from the motherboard manufacturer.

### Disable Driver Verifier

```cmd
verifier /reset
shutdown /r /t 0
```

## Examples

```text
UNEXPECTED_KERNEL_MODE_TRAP (7f)
A trap occurred in kernel mode.

Arg1: 0000000000000008, Double fault
```

## Related Errors

- [BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/os/windows/bsod-whea-uncorrectable-error" >}}) — WHEA uncorrectable error
- [BSOD WHEA_UNCORRECTABLE_ERROR CPU/GPU]({{< relref "/os/windows/bsod-whea2-uncorrectable" >}}) — CPU/GPU voltage error
- [BSOD UNEXPECTED_KERNEL_MODE_TRAP]({{< relref "/os/windows/bsod-unexpected-kernel-mode" >}}) — General kernel trap
