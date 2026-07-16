---
title: "[Solution] BSOD NTFS_FILE_SYSTEM Windows 11/10 — Fixed"
description: "Fix Blue Screen NTFS_FILE_SYSTEM error on Windows 10 and 11. Run CHKDSK, update storage drivers, and repair the NTFS volume to resolve this file system stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "ntfs", "file-system", "storage", "stop-code"]
weight: 5
---

# [Solution] BSOD NTFS_FILE_SYSTEM Windows 11/10 — Fixed

NTFS_FILE_SYSTEM is a critical Blue Screen of Death error with stop code `0x00000024`. It occurs when the NTFS file system driver encounters a fatal error while performing file system operations. This means the NTFS driver (`ntfs.sys`) has detected an internal inconsistency, corruption, or I/O failure that it cannot recover from.

This BSOD affects both Windows 10 and 11 and is almost always related to disk corruption, storage driver issues, or failing hard drives.

## Common Causes

- **Disk corruption** — Bad sectors on the system drive prevent NTFS from reading critical file system structures.
- **Failing hard drive** — Physical degradation of the disk causes intermittent read/write failures.
- **Outdated storage drivers** — AHCI, NVMe, or SATA controller drivers with bugs in their I/O handling.
- **Sudden power loss** — Unexpected shutdowns during write operations leave NTFS metadata in an inconsistent state.

## How to Fix

### Run CHKDSK

This is the primary fix for NTFS file system errors:

```cmd
chkdsk C: /f /r /x
```

Press `Y` to schedule for next restart, then reboot. The `/r` flag locates bad sectors and recovers readable data. The `/x` forces the volume to dismount first.

**If you cannot boot normally**, boot from a Windows installation USB or recovery drive:

1. Select **Repair your computer**.
2. Go to **Troubleshoot > Advanced options > Command Prompt**.
3. Run:

```cmd
chkdsk C: /f /r /x
```

Replace `C:` with the correct drive letter if Windows is on a different partition.

### Update Storage Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest storage drivers from the motherboard or system manufacturer's website:
- **Intel**: Intel Rapid Storage Technology (IRST)
- **AMD**: AMD StoreMI or SATA/NVMe driver
- **NVMe**: Check the NVMe drive manufacturer's website

### Check Disk Health

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus
Get-StorageReliabilityCounter -PhysicalDisk (Get-PhysicalDisk) | Select-Object Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal
```

A `HealthStatus` of `Unhealthy` or any `ReadErrorsTotal`/`WriteErrorsTotal` greater than 0 indicates a failing drive. Back up data immediately and replace the drive.

**Check SMART status:**

```powershell
Get-WmiObject -Namespace root\wmi -Class MSStorageDriver_FailurePredictStatus | Select-Object PredictFailure, Reason
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Repair the NTFS Volume with DISM

If NTFS corruption persists after CHKDSK:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

### Check for Write Caching Issues

Write caching can cause NTFS corruption during sudden power loss:

1. Open **Device Manager**.
2. Expand **Disk drives**.
3. Right-click your system drive and select **Properties**.
4. Go to the **Policies** tab.
5. Uncheck **Enable write caching on the device** if you experience frequent power loss.

## Examples

This error commonly occurs in these scenarios:

- **After a sudden power loss** — The computer lost power during a write operation, leaving NTFS metadata corrupted.
- **With a failing hard drive** — Bad sectors on the disk prevent NTFS from reading the MFT (Master File Table).
- **After connecting a corrupted external drive** — A damaged USB drive triggers NTFS errors when Windows scans it.
- **Following a failed Windows Update** — An interrupted update corrupts NTFS system files.

## Related Errors

- [BSOD FAT_FILE_SYSTEM]({{< relref "/os/windows/bsod-fat-file-system" >}}) — Similar file system error for FAT-formatted volumes
- [BSOD MUP_FILE_SYSTEM]({{< relref "/os/windows/bsod-mup-file-system" >}}) — Multi-UNC Provider file system error
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault-in-nonpaged-area" >}}) — Memory page fault often caused by disk corruption
- [BSOD KERNEL_SECURITY_CHECK_FAILURE]({{< relref "/os/windows/bsod-kernel-security-check-failure" >}}) — Kernel security structure corruption from disk errors
