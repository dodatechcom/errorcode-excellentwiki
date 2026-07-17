---
title: "[Solution] BSOD NTFS_FILE_SYSTEM — 0x24 Ntfs.sys Windows 11/10"
description: "Fix Blue Screen NTFS_FILE_SYSTEM stop code 0x24 caused by Ntfs.sys file system driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "ntfs-file-system", "ntfs", "filesystem", "stop-0x24"]
weight: 5
---

# BSOD NTFS_FILE_SYSTEM — 0x24 Ntfs.sys

The `NTFS_FILE_SYSTEM` stop code `0x24` indicates a problem occurred in the NTFS file system driver. The driver encountered a condition it could not handle, typically caused by file system corruption, disk errors, or bad sectors on the drive.

## Common Causes

- **NTFS file system corruption** — Damaged MFT, directory entries, or file metadata.
- **Disk bad sectors** — Bad sectors on critical NTFS structures cause the driver to fail.
- **Failing storage device** — Hardware defects prevent reliable file system operations.
- **Abrupt power loss** — Sudden shutdowns corrupt NTFS journal and metadata.
- **Antivirus minifilter interference** — Third-party antivirus conflicts with NTFS operations.

## How to Fix

### Run Check Disk

```cmd
chkdsk C: /f /r
```

Allow chkdsk to complete fully at next restart. This is the most important fix for NTFS_FILE_SYSTEM errors.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

### Disable Antivirus Temporarily

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*antivirus*" } | Select-Object Name, Version
```

### Check NTFS Volume

```cmd
fsutil dirty query C:
```

### Check SATA Connection

Reseat SATA cables and try different ports.

### Verify File System

```cmd
chkdsk C: /scan
```

## Examples

```text
NTFS_FILE_SYSTEM (24)
A problem occurred in the NTFS file system driver.

MODULE_NAME: Ntfs
IMAGE_NAME:  Ntfs.sys
```

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntfs.sys]({{< relref "/os/windows/bsod-page-fault-in-npaged" >}}) — NTFS page fault
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED ntfs.sys]({{< relref "/os/windows/bsod-system-thread-exception5" >}}) — NTFS thread exception
- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — Kernel data read failure
