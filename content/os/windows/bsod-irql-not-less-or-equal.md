---
title: "[Solution] BSOD IRQL_NOT_LESS_OR_EQUAL — 0xA ntoskrnl.exe Windows 11/10"
description: "Fix Blue Screen IRQL_NOT_LESS_OR_EQUAL stop code 0xA caused by ntoskrnl.exe kernel on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "irql", "ntoskrnl", "kernel", "stop-0xa"]
weight: 5
---

# BSOD IRQL_NOT_LESS_OR_EQUAL — 0xA ntoskrnl.exe

The `IRQL_NOT_LESS_OR_EQUAL` stop code `0xA` with `ntoskrnl.exe` indicates a kernel-mode component attempted to access memory at an IRQL that was too high. When ntoskrnl.exe is the reported module, the issue may be in the kernel itself, a memory corruption, or a faulty driver that corrupted kernel structures.

## Common Causes

- **Memory corruption** — Bad RAM overwrites kernel data structures, causing IRQL violations.
- **Faulty or incompatible driver** — A third-party driver corrupts kernel memory visible at the ntoskrnl level.
- **Disk corruption** — Damaged system files cause the kernel to reference invalid memory.
- **Overheating system** — Thermal issues cause memory bit-flips that corrupt kernel structures.

## How to Fix

### Test RAM Thoroughly

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 for extended testing (8+ passes).

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Analyze Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open in WinDbg with `!analyze -v`. Even when ntoskrnl.exe is the module, look at the call stack for the actual faulty driver.

### Update All Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DriverDate } | Sort-Object DriverDate -Descending | Select-Object -First 20 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Check System Temperature

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Clean dust from heatsinks and ensure proper cooling.

### Update BIOS

Download the latest BIOS from your motherboard manufacturer.

### Disable Driver Verifier

If Driver Verifier is enabled, it may cause additional BSODs during testing:

```cmd
verifier /reset
```

## Examples

```text
IRQL_NOT_LESS_OR_EQUAL (a)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.

MODULE_NAME: ntoskrnl
IMAGE_NAME:  ntoskrnl.exe
```

## Related Errors

- [BSOD IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-irql-not-less2" >}}) — NDIS related IRQL
- [BSOD IRQL_NOT_LESS_OR_EQUAL dxgkrnl.sys]({{< relref "/os/windows/bsod-irql-not-less3" >}}) — DirectX related IRQL
- [BSOD IRQL_NOT_LESS_OR_EQUAL ntfs.sys]({{< relref "/os/windows/bsod-irql-not-less4" >}}) — NTFS related IRQL
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — Driver-specific IRQL
