---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 Ntfs.sys Windows 11/10"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA stop code 0x50 caused by Ntfs.sys file system driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 Ntfs.sys (2nd variant)

The `PAGE_FAULT_IN_NONPAGED_AREA` stop code `0x50` with `Ntfs.sys` indicates the NTFS file system driver attempted to access an invalid non-paged memory page. This variant specifically occurs during high-throughput disk operations.

## Common Causes

- **Heavy disk I/O load** — High-volume file operations cause NTFS to access invalid memory pages.
- **File system corruption** — Damaged NTFS metadata causes the driver to reference invalid addresses.
- **Disk bad sectors** — Bad sectors on the drive cause read operations to fail.
- **Failing storage device** — Hardware defects cause intermittent read errors.

## How to Fix

### Run Check Disk

```cmd
chkdsk C: /f /r
```

Allow to complete fully at next restart.

### Reduce Disk I/O Load

Temporarily close applications generating heavy disk I/O:
```powershell
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, WorkingSet64, IOOtherBytes | Format-Table -AutoSize
```

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

### Disable Antivirus Minifilter

Temporarily uninstall third-party antivirus to test if a filter is interfering.

### Check SATA Connection

Reseat SATA cables and try different ports.

## Examples

```text
PAGE_FAULT_IN_NONPAGED_AREA (50)
Invalid system memory was referenced.

MODULE_NAME: Ntfs
IMAGE_NAME:  Ntfs.sys
```

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntfs.sys]({{< relref "/os/windows/bsod-page-fault-in-npaged" >}}) — NTFS first variant
- [BSOD NTFS_FILE_SYSTEM]({{< relref "/os/windows/bsod-ntfs-file-system" >}}) — NTFS file system error
- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — Kernel data read error
