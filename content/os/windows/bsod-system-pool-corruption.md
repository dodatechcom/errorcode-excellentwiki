---
title: "[Solution] BSOD SYSTEM_POOL_CORRUPTION Windows 11/10 — Fixed"
description: "Fix Blue Screen SYSTEM_POOL_CORRUPTION error on Windows 10 and 11. Update drivers, check RAM, and run kernel pool diagnostics to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD SYSTEM_POOL_CORRUPTION Windows 11/10 — Fixed

SYSTEM_POOL_CORRUPTION is a critical Blue Screen of Death error with stop code `0x000000C2`. It occurs when the Windows kernel detects corruption in the system memory pool — the kernel's private memory allocator. Pool corruption indicates that a driver has written data beyond the bounds of its allocated memory, overwriting adjacent kernel structures.

This BSOD affects both Windows 10 and 11 and is almost always caused by a buggy driver performing invalid memory operations.

## Common Causes

- **Buggy device drivers** — A driver writes beyond its allocated pool memory, corrupting adjacent data structures.
- **Faulty RAM** — Physical memory errors corrupt the kernel pool at random locations.
- **Overheating hardware** — Thermal issues cause memory bits to flip, corrupting pool data.
- **Malware** — Kernel-mode malware manipulating pool allocations for code injection.

## How to Fix

### Enable Driver Verifier to Find the Bad Driver

Driver Verifier monitors drivers for illegal memory operations:

1. Open **Command Prompt as Administrator**.
2. Run the following command:

```cmd
verifier /standard /all
```

3. Restart your computer. Windows will monitor all drivers.
4. When the BSOD occurs again, the minidump will identify the specific driver.

**To stop Driver Verifier when done troubleshooting:**

```cmd
verifier /reset
```

### Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the dump file in WinDbg and run `!analyze -v`. The **MODULE_NAME** and **IMAGE_NAME** lines identify the corrupting driver. Pool corruption bugs are often identified by the `!poolval` extension in WinDbg.

### Update All Device Drivers

Focus on recently updated or installed drivers:

```powershell
Get-WmiObject Win32_PnPSignedDriver | Sort-Object DriverDate -Descending | Select-Object -First 20 DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Update GPU, network, and storage drivers from the manufacturer's website.

### Test RAM for Errors

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 from a bootable USB for thorough testing with at least 4 passes. Pool corruption can be caused by random bit flips from faulty RAM.

### Run SFC and DISM

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check for Overheating

```powershell
Get-WmiObject -Namespace root\wmi -Class MSAcpi_ThermalZoneTemperature | Select-Object CurrentTemperature
```

Ensure all system fans are functioning. Clean dust from heatsinks and ventilation ports. Monitor temperatures during load using HWMonitor or similar tools.

## Examples

This error commonly occurs in these scenarios:

- **After installing a new driver** — The driver has a buffer overflow bug that corrupts pool memory.
- **With aging hardware** — Failing RAM randomly corrupts kernel pool structures.
- **During heavy system load** — Increased memory pressure exposes latent driver bugs.
- **After running memory-intensive applications** — Pool exhaustion combined with driver bugs triggers corruption.

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault-in-nonpaged-area" >}}) — Invalid memory page reference
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — Driver accessing memory at invalid IRQL
- [BSOD DRIVER_OVERRAN_STACK_BUFFER]({{< relref "/os/windows/bsod-driver-overran-stack-buffer" >}}) — Driver buffer overflow on the stack
- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — General IRQL violation from memory issues
