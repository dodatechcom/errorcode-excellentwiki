---
title: "[Solution] BSOD CACHE_MANAGER Blue Screen Fix"
description: "Fix CACHE_MANAGER blue screen on Windows when the cache manager encounters a fatal error during file system caching operations on Windows 10/11."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] BSOD CACHE_MANAGER Blue Screen Fix

The CACHE_MANAGER blue screen indicates a failure in the Windows cache manager component responsible for file system caching. This component manages reading and writing cached file data to optimize disk I/O performance.

## Common Causes
- NTFS file system corruption affecting cache structures
- Faulty storage device failing during cache write-back
- Insufficient memory causing cache manager failure
- Third-party file system filter driver conflict
- Disk controller driver bug affecting cache operations

## How to Fix

### Solution 1: Run Check Disk

```cmd
chkdsk C: /f /r /x
```

Schedule the scan and restart your computer.

### Solution 2: Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 3: Check Storage Health

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus
```

### Solution 4: Increase Page File

Ensure the page file is set to system managed or at least 1.5 times your RAM size.

### Solution 5: Update Storage Drivers

```powershell
Get-WindowsDriver -Online | Where-Object { $_.ClassName -like '*Storage*' } | Sort-Object Date -Descending | Select-Object -First 5
```

## Examples
```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size
Get-Volume | Select-Object DriveLetter, FileSystem, SizeRemaining, Size
```
