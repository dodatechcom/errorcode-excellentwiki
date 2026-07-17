---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED Ntfs.sys Fix"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED caused by Ntfs.sys on Windows 10 and 11. Repair NTFS file system driver errors with CHKDSK, SFC, and disk diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "ntfs", "file-system", "disk", "driver"]
weight: 5
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED Ntfs.sys Fix

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED with `Ntfs.sys` as the failing driver is a critical Blue Screen error caused by the NT file system driver. This driver manages all read/write operations on NTFS-formatted volumes, and a failure here indicates severe disk or file system corruption.

This BSOD commonly occurs during file operations, disk-intensive workloads, or when the file system encounters corrupted metadata. It can lead to data loss if not addressed promptly.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
> What failed: Ntfs.sys

`Ntfs.sys` is the core Windows file system driver responsible for managing NTFS volumes. When this driver crashes, it means the operating system detected an unrecoverable error while reading or writing to disk. Common triggers include:

- **Bad sectors on disk** — Physical disk damage causes the file system driver to encounter read errors
- **Corrupted file system metadata** — MFT (Master File Table) or directory index corruption
- **Failing hard drive** — Degraded disk hardware causes intermittent I/O errors
- **Improper shutdown** — Power loss during write operations corrupts file system structures

## Common Causes

1. **Corrupted file system** — Damaged MFT, boot sector, or directory structures on the NTFS volume.
2. **Failing hard drive or SSD** — Bad sectors, read errors, or firmware issues.
3. **Loose or faulty SATA/NVMe cables** — Intermittent disk connections cause I/O errors.
4. **Improper system shutdown** — Power loss during disk writes corrupts file system metadata.
5. **Disk write caching issues** — Enabled write cache causes data loss on unexpected power loss.

## How to Fix

### Solution 1: Run CHKDSK to Repair File System Errors

CHKDSK scans the volume for logical errors and repairs file system metadata:

```cmd
chkdsk C: /f /r
```

If prompted to schedule the check on next restart, type **Y** and restart.

The `/r` parameter locates bad sectors and recovers readable data. This can take 1–4 hours depending on disk size.

**Check disk health status:**

```powershell
Get-PhysicalDisk | Select-Object DeviceId, FriendlyName, HealthStatus, OperationalStatus | Format-Table -AutoSize
```

### Solution 2: Run System File Checker

```cmd
sfc /scannow
```

If SFC finds errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 3: Check Disk SMART Health

Determine if the physical disk is failing:

```powershell
Get-WmiObject -Namespace root\wmi -ClassName MSStorageDriver_FailurePredictStatus | Select-Object InstanceName, PredictFailure
```

**Check SMART attributes with CrystalDiskInfo:**

1. Download [CrystalDiskInfo](https://crystalmark.info/en/software/crystaldiskinfo/).
2. Run the application and check the health status of each drive.
3. Look for **Caution** or **Bad** status on any attribute, especially:
   - Reallocated Sector Count
   - Current Pending Sector
   - Uncorrectable Sector Count

### Solution 4: Check Disk Cables and Connections

Loose or faulty cables can cause intermittent I/O errors that crash Ntfs.sys:

1. Shut down the computer and open the case.
2. Reseat the SATA data cable on both the motherboard and drive ends.
3. Try a different SATA port on the motherboard.
4. If using NVMe, reseat the M.2 drive in its slot.
5. Replace cables if any show physical damage.

### Solution 5: Disable Write Caching (If Power Losses Are Frequent)

```powershell
Get-Disk | Where-Object { $_.BusType -eq "ATA" -or $_.BusType -eq "NVMe" } | Set-Disk -IsWriteCachingEnabled $false
```

Re-enable after resolving power issues:

```powershell
Get-Disk | Where-Object { $_.BusType -eq "ATA" -or $_.BusType -eq "NVMe" } | Set-Disk -IsWriteCachingEnabled $true
```

### Solution 6: Backup Data Immediately

If Ntfs.sys crashes persist, back up critical data before the disk fails completely:

```powershell
wbadmin start backup -backupTarget:E: -include:C: -quiet
```

Replace `E:` with your backup drive letter. Consider replacing the disk if SMART reports degradation.

## Related Errors

- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault" >}})** — Memory management error often caused by failing hardware
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage-error" >}})** — Failed page read from disk, related to disk or file system issues
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED nvlddmkm.sys]({{< relref "/windows/bsod-system-thread-exception-nvlddmkm" >}})** — NVIDIA driver version of this BSOD
