---
title: "[Solution] Error 999 — SWAPERROR Fix"
description: "Fix Windows Error Code (SWAPERROR) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 999
---

# [Solution] Error 999 — SWAPERROR Fix

Win32 error 999 (`ERROR_SWAPERROR`) occurs when there is an error performing an inpage operation. This error indicates that the system failed to read or write a page of data from or to the swap file (page file) on disk.

## Description

The SWAPERROR error is returned when Windows cannot perform a page-in or page-out operation, meaning it fails to move memory pages between physical RAM and the page file on disk. This is typically caused by disk failures, corrupted page files, or disk space issues. The error code is `ERROR_SWAPERROR` (value 999). The full message reads:

> "Error performing inpage operation."

## Common Causes

1. The hard drive has bad sectors where the page file resides.
2. The disk is failing or experiencing read/write errors.
3. The page file is corrupted.
4. The disk is full and cannot accommodate page file operations.
5. A disk driver is outdated or malfunctioning.
6. SATA/SCSI cables are loose or damaged.

## Solutions

### Solution 1: Check Disk Health

Run S.M.A.R.T. diagnostics on the drive:

```powershell
# Check disk health status
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus

# Check disk errors
Get-Volume | Select-Object FileSystemLabel, HealthStatus, SizeRemaining
```

### Solution 2: Run chkdsk

Check the disk for file system errors and bad sectors:

```cmd
:: Run check disk (requires restart for system drive)
chkdsk C: /f /r
```

```powershell
# Schedule chkdsk for next restart
chkdsk C: /f /r /x
```

### Solution 3: Replace a Failing Drive

If the drive is failing, back up data and replace it:

```powershell
# Get detailed disk info
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size

# Check for disk errors in event log
Get-WinEvent -LogName System -MaxEvents 100 | Where-Object { $_.ProviderName -like "*disk*" } | Select-Object TimeCreated, Id, Message
```

### Solution 4: Reset the Page File

Delete and recreate the page file:

```cmd
:: Disable page file temporarily (admin required)
wmic computersystem set AutomaticManagedPagefile=False
wmic pagefileset set InitialSize=0,MaximumSize=0
```

```powershell
# Re-enable automatic page file management
wmic computersystem set AutomaticManagedPagefile=True
```

### Solution 5: Check Disk Space

Ensure there is adequate free space on the system drive:

```powershell
# Check free space
Get-PSDrive C | Select-Object @{Name="FreeGB";Expression={[math]::Round($_.Free/1GB,2)}}, @{Name="UsedGB";Expression={[math]::Round($_.Used/1GB,2)}}
```

```cmd
:: Clean up disk space
cleanmgr /sagerun:1
```

## Related Errors

- [Error 995 — OPERATION_ABORTED]({{< relref "/os/windows/win32-operation-aborted" >}}) — I/O operation was aborted
- [Error 112 — DISK_FULL]({{< relref "/os/windows/win32-disk-full" >}}) — There is not enough space on the disk
- [Error 23 — CRC]({{< relref "/os/windows/win32-crc-error" >}}) — Data error (cyclic redundancy check)
