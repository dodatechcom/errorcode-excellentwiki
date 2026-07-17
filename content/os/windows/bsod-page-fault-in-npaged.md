---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 ntfs.sys Windows 11/10"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA stop code 0x50 caused by ntfs.sys file system driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "page-fault", "ntfs", "filesystem", "stop-0x50"]
weight: 5
---

# BSOD PAGE_FAULT_IN_NONPAGED_AREA — 0x50 ntfs.sys

The `PAGE_FAULT_IN_NONPAGED_AREA` stop code `0x50` with `ntfs.sys` indicates the NTFS file system driver attempted to access a non-paged memory page that is invalid. This points to file system corruption, disk errors, or a faulty storage device.

## Common Causes

- **NTFS file system corruption** — Damaged MFT (Master File Table) or directory structures cause invalid memory references.
- **Disk bad sectors** — Bad sectors on the disk cause NTFS to reference invalid memory pages.
- **Failing storage device** — SSD or HDD hardware failure causes intermittent read errors.
- **Abrupt shutdown or power loss** — Sudden power loss corrupts NTFS metadata structures.
- **Antivirus minifilter interference** — Third-party file system filters conflict with ntfs.sys.

## How to Fix

### Run Check Disk

```cmd
chkdsk C: /f /r
```

Allow chkdsk to complete fully. This scans for and repairs file system corruption and bad sectors.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -eq "disk" } | Select-Object -First 10 TimeCreated, Id, Message | Format-Table -Wrap
```

### Disable Antivirus Temporarily

Temporarily uninstall third-party antivirus to test if a minifilter driver is causing the conflict.

### Check SATA Cables and Ports

Reseat SATA cables and try different ports. For NVMe drives, try a different M.2 slot.

### Verify NTFS Integrity

```cmd
fsutil dirty query C:
```

If the volume is dirty, restart and let chkdsk run.

## Examples

```text
PAGE_FAULT_IN_NONPAGED_AREA (50)
Invalid system memory was referenced.

MODULE_NAME: ntfs
IMAGE_NAME:  ntfs.sys
FOLLOWUP_NAME:  ntfs!NtfsReadRetry
```

## Related Errors

- [BSOD PAGE_FAULT_IN_NONPAGED_AREA ntoskrnl.exe]({{< relref "/os/windows/bsod-page-fault3" >}}) — Kernel page fault
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA Ntfs.sys]({{< relref "/os/windows/bsod-page-fault5" >}}) — NTFS variant page fault
- [BSOD NTFS_FILE_SYSTEM]({{< relref "/os/windows/bsod-ntfs-file-system" >}}) — NTFS file system error
