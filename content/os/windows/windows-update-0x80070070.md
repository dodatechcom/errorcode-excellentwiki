---
title: "[Solution] Windows Update Error 0x80070070 — Insufficient Disk Space Fix"
description: "Fix Windows Update error 0x80070070 (insufficient disk space) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Error 0x80070070 — Insufficient Disk Space Fix

Windows Update error 0x80070070 means the system does not have enough disk space to download or install updates. Windows requires free space on the system drive for temporary update files and the installation process.

## Description

The full error message reads:

> "There were problems installing some updates, but we'll try again later. Error 0x80070070"

Error 0x80070070 maps to `ERROR_DISK_FULL` or `ERROR_NOT_ENOUGH_SERVER_MEMORY`, indicating the system drive has insufficient free space for the update operation.

## Common Causes

1. **Low free disk space** — System drive has less than the required 20 GB free for updates.
2. **Temp folder bloat** — Accumulated temporary files consuming disk space.
3. **Full Windows Installer cache** — Old installer files occupying space.
4. **Partition too small** — System partition too small for modern Windows updates.

## Solutions

### Solution 1: Free Disk Space Using Disk Cleanup

```cmd
cleanmgr /d C:
```

Select **Clean up system files** and check all boxes, especially:

- Windows Update Cleanup
- Temporary Internet Files
- Recycle Bin
- Temporary files

### Solution 2: Clean Temporary Files Manually

```cmd
del /q/f/s %TEMP%\*
del /q/f/s C:\Windows\Temp\*
```

### Solution 3: Remove Old Windows Update Files

```cmd
net stop wuauserv
del /q/f/s C:\Windows\SoftwareDistribution\Download\*
net start wuauserv
```

### Solution 4: Extend System Partition

If the system partition is too small, use Disk Management to extend it:

```powershell
Get-Partition -DiskNumber 0 | Select-Object PartitionNumber, DriveLetter, Size, @{N='SizeGB';E={[math]::Round($_.Size/1GB,2)}}
```

Use `diskmgmt.msc` to shrink an adjacent partition and extend the system partition, or use third-party partition tools.

## Related Errors

- [Error 0x8007000E]({{< relref "/os/windows/windows-update-0x8007000e" >}}) — Out of memory
- [Error 0x80070008]({{< relref "/os/windows/windows-update-0x80070008" >}}) — Not enough memory
- [Error 0x80073712]({{< relref "/os/windows/windows-update-0x80073712" >}}) — Component store corrupted
