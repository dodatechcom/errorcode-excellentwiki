---
title: "[Solution] BSOD KERNEL_DATA_INPAGE_ERROR — 0x7A Disk Error Windows 11/10"
description: "Fix Blue Screen KERNEL_DATA_INPAGE_ERROR stop code 0x7A caused by disk read errors on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD KERNEL_DATA_INPAGE_ERROR — 0x7A Disk Error

The `KERNEL_DATA_INPAGE_ERROR` stop code `0x7A` indicates Windows failed to read a page of kernel data from the paging file or disk into memory. This points to a storage subsystem failure — the disk cannot provide the data the kernel needs.

## Common Causes

- **Failing hard drive** — Bad sectors prevent reading critical kernel data from disk.
- **Corrupted file system** — NTFS corruption causes invalid disk reads for page file operations.
- **Failing SSD** — SSD controller errors or bad NAND blocks cause read failures.
- **SATA cable or controller issues** — Physical connection problems cause intermittent read errors.
- **Insufficient disk space** — Not enough free space for the page file to expand.

## How to Fix

### Check Disk Health with SMART

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
Get-Disk | Select-Object Number, FriendlyName, OperationalStatus, HealthStatus
```

### Run Check Disk

```cmd
chkdsk C: /f /r
```

Schedule for next restart and allow it to complete fully.

### Verify Page File Size

```powershell
# Check current page file configuration
Get-WmiObject Win32_ComputerSystem | Select-Object AutomaticManagedPagefile
Get-WmiObject Win32_PageFileSetting | Select-Object Name, InitialSize, MaximumSize
```

Ensure the page file is at least 1.5x your RAM size.

### Test Storage Hardware

```powershell
# Check disk errors in Event Viewer
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*disk*" -or $_.ProviderName -like "*ntfs*" } | Select-Object -First 10 TimeCreated, Id, Message | Format-Table -Wrap
```

### Replace Failing Drive

If SMART reports failing health or chkdsk finds unfixable bad sectors, replace the drive immediately.

### Repair File System

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

## Examples

```text
KERNEL_DATA_INPAGE_ERROR (7a)
The requested page of kernel data could not be read in.

Arg1: c03e14b8, error status
Arg2: 00000001, lock type that was held
Arg3: 00000000, read operation
Arg4: 87013860, memory address
```

## Related Errors

- [BSOD KERNEL_DATA_INPAGE_ERROR ataport.SYS]({{< relref "/os/windows/bsod-kernel-data-inpage-error2" >}}) — ATA port driver error
- [BSOD KERNEL_DATA_INPAGE_ERROR disk.sys]({{< relref "/os/windows/bsod-kernel-data-inpage-error3" >}}) — Disk class driver error
- [BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/os/windows/bsod-inaccessible-boot" >}}) — Cannot access boot device
