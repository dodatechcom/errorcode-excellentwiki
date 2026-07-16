---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA Windows 11/10 — Fixed"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA error on Windows 10 and 11. Test RAM, check disk health, and update drivers to resolve this memory-related stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "page-fault", "memory", "stop-code"]
weight: 5
---

# [Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA Windows 11/10 — Fixed

PAGE_FAULT_IN_NONPAGED_AREA is a critical Blue Screen of Death error with stop code `0x00000050`. It occurs when Windows requests data from memory that cannot be found in the nonpaged area — a reserved region of RAM that must always remain in physical memory. This typically indicates faulty RAM, a disk error, or a corrupted driver.

This BSOD affects both Windows 10 and 11 and is closely linked to hardware failures, especially RAM and storage.

## Common Causes

- **Faulty RAM** — The most common cause. Physical memory defects cause data to be unreadable from the nonpaged pool.
- **Corrupted drivers** — A driver references memory that has been freed or corrupted.
- **Disk errors** — Bad sectors on the system drive prevent page files or system files from loading correctly.
- **Corrupted NTFS volume** — File system corruption causes Windows to reference invalid memory addresses.

## How to Fix

### Test RAM Thoroughly

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. After reboot, check results:

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -eq "Microsoft-Windows-MemoryDiagnostics-Results" } | Select-Object -First 5 Message
```

For comprehensive testing, use MemTest86 from a bootable USB for at least 4 passes. If errors are found, test each RAM stick individually to isolate the faulty module.

### Check and Repair Disk Errors

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule for next restart, then reboot. The `/r` flag locates bad sectors and recovers readable data.

**Check disk health:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus
Get-StorageReliabilityCounter -PhysicalDisk (Get-PhysicalDisk) | Select-Object Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal
```

### Update or Roll Back Drivers

Faulty drivers are the second most common cause. Focus on storage and GPU drivers:

```powershell
Get-WmiObject Win32_PnPEntity | Where-Object { $_.ConfigManagerErrorCode -ne 0 } | Select-Object Name, DeviceID, ConfigManagerErrorCode | Format-Table -AutoSize
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check for Faulty RAM with Extended Diagnostics

```powershell
Get-CimInstance -ClassName Win32_PhysicalMemory | Select-Object BankLabel, Capacity, Speed, ConfiguredClockSpeed, Manufacturer | Format-Table -AutoSize
```

Compare `Speed` and `ConfiguredClockSpeed`. If they differ significantly, the RAM may be running at incorrect timings. Verify XMP/DOCP profile settings in BIOS match your RAM's rated specifications.

### Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the dump file in WinDbg and run `!analyze -v` to identify the faulting driver.

## Examples

This error commonly occurs in these scenarios:

- **After installing new RAM** — New memory modules are faulty or incompatible with the motherboard.
- **During heavy memory usage** — Running multiple applications exposes latent RAM defects.
- **After a Windows Update** — Updated drivers reference invalid memory addresses.
- **With aging hardware** — RAM degradation over time leads to random data corruption.

## Related Errors

- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — Another memory-related BSOD caused by invalid IRQL access
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel-mode exception from memory or driver issues
- [BSOD SYSTEM_POOL_CORRUPTION]({{< relref "/os/windows/bsod-system-pool-corruption" >}}) — Kernel memory pool corruption
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — Driver memory access at invalid IRQL
