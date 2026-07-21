---
title: "[Solution] Disk Offline Hardware RAID Configuration Fix"
description: "Fix Windows disk that goes offline due to hardware RAID configuration changes. Resolve disk offline issues after BIOS RAID reconfiguration."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Disk Offline Hardware RAID Configuration Fix

Disks connected through a hardware RAID controller may go offline when the RAID configuration changes or when the controller firmware is updated.

## Common Causes
- RAID array rebuilt with new configuration
- Controller firmware update changing disk signatures
- New disk added to RAID array changing virtual disk order
- HBA driver update re-enumerating disks
- Disk migration between RAID controllers

## How to Fix

### Solution 1: Bring Disks Online

```cmd
diskpart
list disk
select disk X
online disk
```

### Solution 2: Rescan for New Disks

```powershell
Update-Disk
Initialize-Disk -Number X -PartitionStyle GPT
```

### Solution 3: Check RAID Controller Status

Open the RAID controller management utility and verify all virtual disks are healthy.

### Solution 4: Update HBA Driver

```powershell
Get-WindowsDriver -Online | Where-Object { $_.ClassName -like '*SCSI*' -or $_.ClassName -like '*RAID*' } | Sort-Object Date -Descending
```

### Solution 5: Import Foreign Configuration

If disks show as foreign in Disk Management, right-click and select Import Foreign Disks.

## Examples
```powershell
Get-Disk | Select-Object Number, FriendlyName, PartitionStyle, IsOffline, Size
```
