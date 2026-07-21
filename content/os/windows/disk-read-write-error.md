---
title: "[Solution] Disk Read Write Error Cyclic Redundancy Fix"
description: "Fix disk read write error with cyclic redundancy check on Windows. Resolve CRC disk errors and data corruption issues with chkdsk on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Disk Read Write Error Cyclic Redundancy Fix

A disk read write error with cyclic redundancy check (CRC) means the data read from the disk does not match the stored checksum. This indicates physical disk degradation or data corruption.

## Common Causes
- Failing hard drive with bad sectors
- Loose or damaged SATA/NVMe cable
- Corrupted file system from unexpected power loss
- Overheating disk causing read errors
- Disk reaching end of life with excessive reallocated sectors

## How to Fix

### Solution 1: Run Check Disk

```cmd
chkdsk C: /f /r /x
```

### Solution 2: Check Disk Health

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus, Size
```

### Solution 3: View SMART Data

```powershell
Get-WmiObject -Namespace root\wmi -Class MSStorageDriver_FailurePredictStatus | Select-Object PredictFailure, Reason
```

### Solution 4: Reseat Cables

Power down and reseat the SATA or NVMe data and power cables.

### Solution 5: Backup and Replace

If the disk shows unhealthy status, immediately back up data and replace the drive.

## Examples
```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size
```
