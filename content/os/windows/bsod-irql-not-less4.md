---
title: "[Solution] BSOD IRQL_NOT_LESS_OR_EQUAL — 0xA ntfs.sys Windows 11/10"
description: "Fix Blue Screen IRQL_NOT_LESS_OR_EQUAL stop code 0xA caused by ntfs.sys file system driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "irql", "ntfs", "filesystem", "stop-0xa"]
weight: 5
---

# BSOD IRQL_NOT_LESS_OR_EQUAL — 0xA ntfs.sys

The `IRQL_NOT_LESS_OR_EQUAL` stop code `0xA` with `ntfs.sys` indicates the NTFS file system driver accessed paged memory at an elevated IRQL. This is caused by file system corruption, disk errors, or antivirus minifilter conflicts.

## Common Causes

- **NTFS file system corruption** — Damaged metadata causes NTFS to access invalid memory.
- **Disk bad sectors** — Bad sectors cause NTFS to reference invalid memory pages.
- **Antivirus minifilter interference** — Third-party antivirus filters interfere with NTFS operations.
- **Failing storage device** — Hardware defects cause intermittent file system errors.

## How to Fix

### Run Check Disk

```cmd
chkdsk C: /f /r
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Disable Antivirus Temporarily

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*antivirus*" } | Select-Object Name, Version
```

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

### Test RAM

```cmd
mdsched.exe
```

### Check SATA Connection

Reseat SATA cables and try different ports.

## Examples

```text
IRQL_NOT_LESS_OR_EQUAL (a)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.

MODULE_NAME: ntfs
IMAGE_NAME:  ntfs.sys
```

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntfs.sys]({{< relref "/os/windows/bsod-page-fault-in-npaged" >}}) — NTFS page fault
- [BSOD NTFS_FILE_SYSTEM]({{< relref "/os/windows/bsod-ntfs-file-system" >}}) — NTFS file system error
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED ntfs.sys]({{< relref "/os/windows/bsod-system-thread-exception5" >}}) — NTFS thread exception
