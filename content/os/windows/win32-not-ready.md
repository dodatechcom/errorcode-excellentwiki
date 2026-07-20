---
title: "[Solution] Error 21 — NOT_READY Fix"
description: "Fix Windows Error Code (NOT_READY) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 21
---

# [Solution] Error 21 — NOT_READY Fix

Win32 error 21 (`ERROR_NOT_READY`) occurs when the device is not ready. This error is returned when the system attempts to access a storage device or drive that is not in a ready state, such as an uninitialized disk or a drive that has not spun up.

## Description

The NOT_READY error is returned when a storage device cannot complete the requested operation because it is not in a ready state. This commonly occurs with optical drives without a disc, external drives that are disconnected, or uninitialized hard disks. The error code is `ERROR_NOT_READY` (value 21). The full message reads:

> "The device is not ready."

## Common Causes

1. An optical drive has no disc inserted.
2. An external drive is disconnected or powered off.
3. A hard drive has not finished initializing or spinning up.
4. The drive firmware is stuck in a busy state.
5. The disk has not been initialized or formatted.
6. A virtual disk or VHD is not properly mounted.

## Solutions

### Solution 1: Check Drive Connection

Verify the drive is properly connected and powered:

```powershell
# Check disk status
Get-Disk | Select-Object Number, FriendlyName, OperationalStatus, Size, PartitionStyle

# Check physical disks
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, MediaType, ConnectionType
```

### Solution 2: Initialize the Disk

Initialize an uninitialized disk:

```powershell
# Initialize a new disk
Get-Disk | Where-Object { $_.PartitionStyle -eq "RAW" } | Initialize-Disk -PartitionStyle GPT

# Create a partition and format
New-Partition -DiskNumber N -UseMaximumSize -DriveLetter E | Format-Volume -FileSystem NTFS
```

### Solution 3: Run Disk Management

Open Disk Management to visually inspect drive status:

```powershell
# Open Disk Management
diskmgmt.msc
```

### Solution 4: Check Hardware Status

Verify the hardware is functioning:

```powershell
# Check for errors in event log
Get-WinEvent -LogName System -MaxEvents 50 | Where-Object { $_.ProviderName -like "*disk*" -or $_.LevelDisplayName -eq "Error" } | Select-Object TimeCreated, Id, Message

# Check SMART status
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus
```

### Solution 5: Re-seat or Replace the Drive

For internal drives, power off and re-seat the drive connections. For external drives:

```powershell
# Eject and reconnect external drive
$drive = Get-WmiObject -Class Win32_DiskDrive | Where-Object { $_.MediaType -like "External*" }
$drive | Select-Object Model, Status, Size
```

## Related Errors

- [Error 19 — WRITE_PROTECT]({{< relref "/os/windows/win32-file-readonly" >}}) — The media is write protected
- [Error 23 — CRC]({{< relref "/os/windows/win32-crc-error" >}}) — Data error (cyclic redundancy check)
- [Error 112 — DISK_FULL]({{< relref "/os/windows/win32-disk-full" >}}) — There is not enough space on the disk
