---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E ntfs.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by ntfs.sys NTFS file system driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E ntfs.sys

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `ntfs.sys` indicates the NTFS file system driver encountered an unhandled exception in a system thread. This is caused by file system corruption, disk errors, or antivirus minifilter conflicts.

## Common Causes

- **NTFS file system corruption** — Damaged file system metadata causes the driver to encounter invalid states.
- **Disk bad sectors** — Bad sectors on the drive cause NTFS to fail during read operations.
- **Antivirus minifilter conflict** — Third-party antivirus filters interfere with NTFS operations.
- **Corrupted ntfs.sys** — The NTFS driver file itself is damaged.

## How to Fix

### Run Check Disk

```cmd
chkdsk C: /f /r
```

Allow chkdsk to complete fully at next restart.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Update or Remove Antivirus

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*antivirus*" -or $_.Name -like "*security*" } | Select-Object Name, Version
```

Temporarily uninstall third-party antivirus to test.

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Health, Wear
```

Replace failing drives immediately.

### Boot into Safe Mode and Uninstall Recent Changes

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

### Verify ntfs.sys Integrity

```cmd
sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: ntfs
IMAGE_NAME:  ntfs.sys
FOLLOWUP_NAME:  ntfs!NtfsFcbTable
```

## Related Errors

- [BSOD NTFS_FILE_SYSTEM]({{< relref "/os/windows/bsod-ntfs-file-system" >}}) — NTFS file system error
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntfs.sys]({{< relref "/os/windows/bsod-page-fault-in-npaged" >}}) — NTFS page fault
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED fltmgr.sys]({{< relref "/os/windows/bsod-system-thread-exception4" >}}) — Filter manager exception
