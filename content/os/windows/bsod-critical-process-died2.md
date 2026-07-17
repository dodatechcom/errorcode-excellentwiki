---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED — 0xEF Disk Failure Windows 11/10"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED stop code 0xEF caused by disk failure on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "critical-process-died", "disk", "storage", "stop-0xef"]
weight: 5
---

# BSOD CRITICAL_PROCESS_DIED — 0xEF Disk Failure

The `CRITICAL_PROCESS_DIED` stop code `0xEF` with a disk failure indicates a critical system process terminated unexpectedly because the disk could not provide the data it needed. When the storage device fails, processes that depend on reading system files from disk crash and trigger this BSOD.

## Common Causes

- **Failing hard drive or SSD** — Physical drive failure prevents critical processes from reading system files.
- **Corrupted file system** — Damaged NTFS metadata prevents process-critical file reads.
- **Failing storage controller** — SATA/NVMe controller errors cause intermittent read failures.
- **Disk driver corruption** — Storage driver issues prevent proper disk access.
- **Insufficient disk space** — System partition has no free space for critical operations.

## How to Fix

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
Get-Disk | Select-Object Number, FriendlyName, OperationalStatus, HealthStatus
```

### Run Check Disk

```cmd
chkdsk C: /f /r
```

Allow chkdsk to complete fully at next restart.

### Check Event Viewer for Disk Errors

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*disk*" } | Select-Object -First 20 TimeCreated, Id, Message | Format-Table -Wrap
```

Look for Event IDs 7, 11, 15, and 51 indicating disk errors.

### Ensure Adequate Disk Space

```powershell
Get-Volume | Select-Object DriveLetter, FileSystemLabel, SizeRemaining, Size | Format-Table -AutoSize
```

Free up space if the system drive has less than 10% free space.

### Test with Different Cables and Ports

Swap SATA cables and try different motherboard SATA ports. For NVMe drives, try a different M.2 slot.

### Run Startup Repair

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

### Replace Failing Drive

If the drive fails SMART tests or chkdsk cannot fix errors, replace the drive and restore from backup.

## Examples

```text
CRITICAL_PROCESS_DIED (ef)
A critical system process terminated unexpectedly.

Arg1: ffffc08123456789, Process or thread object
Arg2: 0000000000000000, Exit status
Arg3: ffffc08123456000, PEPROCESS address
Arg4: 0000000000000000, Reserved
```

## Related Errors

- [BSOD CRITICAL_PROCESS_DIED storport.sys]({{< relref "/os/windows/bsod-critical-process-died3" >}}) — Storage port driver failure
- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — Disk read failure
- [BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/os/windows/bsod-inaccessible-boot" >}}) — Boot device inaccessible
