---
title: "[Solution] Error 23 — CRC Fix"
description: "Fix Windows Error Code (CRC) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 23
---

# [Solution] Error 23 — CRC Fix

Win32 error 23 (`ERROR_CRC`) occurs when there is a data error detected by a cyclic redundancy check. This error indicates that data read from a disk or during transmission is corrupted and does not match its expected checksum.

## Description

The CRC error is returned when the cyclic redundancy check algorithm detects that data read from storage media or received over a network does not match the expected checksum. This typically indicates disk corruption, bad sectors, failing hardware, or data transmission errors. The error code is `ERROR_CRC` (value 23). The full message reads:

> "Data error (cyclic redundancy check)."

## Common Causes

1. Bad sectors on the hard drive.
2. Corrupted data on the disk surface.
3. Failing hard drive or SSD.
4. Damaged SATA, USB, or network cables.
5. Data corruption during file transfer.
6. Faulty disk controller or memory modules.

## Solutions

### Solution 1: Run chkdsk

Use Check Disk to scan for and repair file system errors:

```cmd
:: Run check disk with fix and repair bad sectors
chkdsk C: /f /r
```

```powershell
# Schedule chkdsk for the system drive on next restart
chkdsk C: /f /r /x
```

### Solution 2: Check Cables and Connections

Inspect physical connections for damage:

```powershell
# Check disk connection status
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, ConnectionType

# Check for disk errors in event log
Get-WinEvent -LogName System -MaxEvents 50 | Where-Object { $_.ProviderName -like "*disk*" -or $_.ProviderName -like "*Ntfs*" } | Select-Object TimeCreated, Id, Message
```

### Solution 3: Replace a Failing Drive

If chkdsk cannot repair the errors or the drive is failing:

```powershell
# Check disk health
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus, Size

# Get disk S.M.A.R.T. status
Get-WmiObject -Namespace "root\wmi" -Class MSStorageDriver_FailurePredictStatus | Select-Object PredictFailure
```

### Solution 4: Scan the System File

Run System File Checker to repair corrupted system files:

```cmd
sfc /scannow
```

```cmd
:: If SFC finds irreparable errors, run DISM
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 5: Test Memory

Faulty RAM can cause data corruption that manifests as CRC errors:

```cmd
:: Run Windows Memory Diagnostic
mdsched.exe
```

## Related Errors

- [Error 999 — SWAPERROR]({{< relref "/os/windows/win32-swaperror" >}}) — Error performing inpage operation
- [Error 21 — NOT_READY]({{< relref "/os/windows/win32-not-ready" >}}) — The device is not ready
- [Error 19 — WRITE_PROTECT]({{< relref "/os/windows/win32-file-readonly" >}}) — The media is write protected
