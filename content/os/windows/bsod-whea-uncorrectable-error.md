---
title: "[Solution] BSOD WHEA_UNCORRECTABLE_ERROR — 0x124 WHEA Windows 11/10"
description: "Fix Blue Screen WHEA_UNCORRECTABLE_ERROR stop code 0x124 caused by Windows Hardware Error Architecture on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "whea", "hardware-error", "cpu", "stop-0x124"]
weight: 5
---

# BSOD WHEA_UNCORRECTABLE_ERROR — 0x124 WHEA

The `WHEA_UNCORRECTABLE_ERROR` stop code `0x124` indicates the Windows Hardware Error Architecture (WHEA) detected an uncorrectable hardware error. This is a severe hardware fault that cannot be corrected by the system — typically CPU, motherboard, or RAM failure.

## Common Causes

- **CPU failure or degradation** — Physical CPU defects cause uncorrectable hardware errors.
- **Motherboard VRM failure** — Faulty voltage regulation causes unstable CPU operation.
- **RAM failure** — Severe memory errors that ECC cannot correct.
- **Overclocking instability** — Aggressive CPU or RAM overclocks cause hardware-level errors.
- **CPU overheating** — Extreme temperatures cause the CPU to generate hardware errors.

## How to Fix

### Check WHEA Error Source

```powershell
Get-WinEvent -LogName System | Where-Object { $_.Id -eq 18 } | Select-Object -First 10 TimeCreated, Message | Format-Table -Wrap
```

Look for WHEA Logger Event ID 18 which identifies the error source (CPU, memory, PCIe, etc.).

### Reset BIOS to Defaults

Enter BIOS/UEFI and load optimized defaults. Disable all overclocking:
- CPU core multiplier and voltage
- RAM XMP/DOCP/EXPO profiles
- BCLK frequency
- GPU overclock

### Monitor CPU Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Clean heatsink, replace thermal paste, ensure proper cooling.

### Test RAM

```cmd
mdsched.exe
```

Run MemTest86 for extended testing. Replace defective modules.

### Check CPU Voltage Settings

In BIOS, verify:
- CPU core voltage is set to Auto or a safe value
- Load-Line Calibration is not too aggressive
- No manual voltage overrides beyond spec

### Update BIOS

Download and install the latest BIOS from the motherboard manufacturer.

### Check for PCIe Device Errors

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*WHEA*" } | Select-Object -First 20 TimeCreated, Id, Message | Format-Table -Wrap
```

## Examples

```text
WHEA_UNCORRECTABLE_ERROR (124)
A fatal hardware error has occurred.

Arg1: 0000000000000000, Machine Check Exception
Arg2: ffffc80123456780, Address of the WHEA_ERROR_RECORD structure
Arg3: 00000000be000000, High 32 bits of MCi_STATUS MSR
Arg4: 0000000000000000, Low 32 bits of MCi_STATUS MSR
```

## Related Errors

- [BSOD WHEA_UNCORRECTABLE_ERROR CPU/GPU]({{< relref "/os/windows/bsod-whea2-uncorrectable" >}}) — CPU/GPU voltage error
- [BSOD UNEXPECTED_KERNEL_MODE_TRAP]({{< relref "/os/windows/bsod-unexpected-kernel-mode" >}}) — CPU trap exception
- [BSOD UNEXPECTED_KERNEL_MODE_TRAP WHEA]({{< relref "/os/windows/bsod-unexpected-kernel-mode2" >}}) — WHEA-related trap
