---
title: "[Solution] BSOD KERNEL_DATA_INPAGE_ERROR — 0x7A ataport.SYS Windows 11/10"
description: "Fix Blue Screen KERNEL_DATA_INPAGE_ERROR stop code 0x7A caused by ataport.SYS ATA port driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD KERNEL_DATA_INPAGE_ERROR — 0x7A ataport.SYS

The `KERNEL_DATA_INPAGE_ERROR` stop code `0x7A` with `ataport.SYS` indicates the ATA port driver failed to read kernel data from the disk into memory. This points to a storage subsystem failure on SATA/IDE drives.

## Common Causes

- **Failing SATA hard drive or SSD** — Physical drive failure prevents reading kernel pages.
- **SATA cable or port issues** — Loose connections cause intermittent read errors.
- **Corrupted file system** — NTFS corruption causes invalid disk reads.
- **BIOS SATA mode mismatch** — Incorrect SATA mode causes driver communication failures.

## How to Fix

### Check Drive Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

### Run Check Disk

```cmd
chkdsk C: /f /r
```

### Check SATA Cables

Reseat all SATA cables and try different ports.

### Verify BIOS SATA Mode

Enter BIOS and verify SATA mode matches the installed driver:
- AHCI for modern systems
- IDE for legacy compatibility

### Update SATA Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC" } | Select-Object DeviceName, DriverVersion | Format-Table -AutoSize
```

### Check Disk Space

```powershell
Get-Volume | Select-Object DriveLetter, FileSystemLabel, SizeRemaining, Size | Format-Table -AutoSize
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

## Examples

```text
KERNEL_DATA_INPAGE_ERROR (7a)
The requested page of kernel data could not be read in.

MODULE_NAME: ataport
IMAGE_NAME:  ataport.SYS
```

## Related Errors

- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — General disk read failure
- [BSOD KERNEL_DATA_INPAGE_ERROR disk.sys]({{< relref "/os/windows/bsod-kernel-data-inpage-error3" >}}) — Disk class driver error
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ataport.SYS]({{< relref "/os/windows/bsod-irql-driver4" >}}) — ATA port IRQL error
