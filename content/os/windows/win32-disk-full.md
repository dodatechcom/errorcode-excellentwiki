---
title: "[Solution] Error 112 — DISK_FULL Fix"
description: "Fix Windows Error Code (DISK_FULL) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 112
---

# [Solution] Error 112 — DISK_FULL Fix

Win32 error 112 (`ERROR_DISK_FULL`) occurs when there is not enough space on the disk. This error prevents file creation, writing, and sometimes even deletion operations from completing successfully.

## Description

The DISK_FULL error is returned when a write operation fails because the target disk volume has no remaining free space. This affects file creation, application installations, downloads, and system operations like updates and logging. The error code is `ERROR_DISK_FULL` (value 112). The full message reads:

> "There is not enough space on the disk."

## Common Causes

1. The disk volume has run out of free space.
2. Temporary files have consumed available space.
3. The disk quota for the user has been reached.
4. A disk quota or reservation limits the available space.
5. The recycle bin is consuming a large amount of space.
6. System restore points have consumed available space.

## Solutions

### Solution 1: Free Disk Space

Check current disk usage and identify large files:

```powershell
# Check disk space
Get-PSDrive C | Select-Object Used, Free

# Find the largest files on the drive
Get-ChildItem C:\ -Recurse -File -ErrorAction SilentlyContinue |
    Sort-Object Length -Descending |
    Select-Object -First 20 FullName, @{Name="SizeMB";Expression={[math]::Round($_.Length/1MB,2)}}
```

### Solution 2: Clean Temp Files

Use Disk Cleanup or manually remove temporary files:

```powershell
# Remove Windows temp files
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue

# Run Disk Cleanup silently
cleanmgr /sagerun:1
```

```cmd
:: Remove temp files via command line
del /q /f /s "%TEMP%\*.*"
del /q /f /s "C:\Windows\Temp\*.*"
```

### Solution 3: Extend the Partition

Extend the volume using disk management or DiskPart:

```cmd
diskpart
list volume
select volume C
extend
exit
```

### Solution 4: Empty the Recycle Bin

```powershell
# Empty the recycle bin
Clear-RecycleBin -Force
```

```cmd
:: Or via command line
rd /s /q C:\$Recycle.Bin
```

### Solution 5: Remove System Restore Points

```powershell
# Remove old restore points
vssadmin delete shadows /for=C: /oldest
```

## Related Errors

- [Error 1122 — NO_STREAM]({{< relref "/os/windows/win32-no-stream" >}}) — No stream exists
- [Error 112 — DISK_FULL]({{< relref "/os/windows/win32-disk-full" >}}) — Not enough disk space
- [Error 145 — DIR_NOT_EMPTY]({{< relref "/os/windows/win32-dir-not-empty" >}}) — Directory is not empty
