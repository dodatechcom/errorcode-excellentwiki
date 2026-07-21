---
title: "[Solution] Disk Signature Collision Error Fix"
description: "Fix Windows disk signature collision error when two disks have the same MBR signature. Resolve disk conflicts and offline disk issues on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Disk Signature Collision Error Fix

A disk signature collision occurs when two or more disks have identical MBR disk signatures. Windows cannot distinguish between them and marks one disk offline to prevent data corruption.

## Common Causes
- Cloning a disk without generating a new signature
- Restoring a disk image that duplicates the original signature
- Virtual machine snapshots sharing the same base disk
- Connecting a backup drive that was cloned from the system disk

## How to Fix

### Solution 1: Change Disk Signature with Diskpart

```cmd
diskpart
select disk X
uniqueid disk id=NEW_SIGNATURE
```

### Solution 2: Use Windows Disk Management

1. Open diskmgmt.msc
2. Right-click the offline disk
3. Select Online to prompt Windows to initialize with a new signature

### Solution 3: Use PowerShell to Generate New Signature

```powershell
Set-Disk -Number X -UniqueId (New-Guid)
```

### Solution 4: Check for Conflicting Disks

```powershell
Get-Disk | Select-Object Number, FriendlyName, PartitionStyle, UniqueId | Format-Table -AutoSize
```

### Solution 5: Convert to GPT

Convert the disk to GPT partition style which uses GUIDs instead of MBR signatures, avoiding collisions entirely.

## Examples
```powershell
Get-Disk | Select-Object Number, FriendlyName, UniqueId
```
