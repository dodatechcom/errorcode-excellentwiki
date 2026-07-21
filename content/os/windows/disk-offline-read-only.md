---
title: "[Solution] Disk Set to Offline Read-Only Mode Fix"
description: "Fix Windows disk that shows as offline or read-only in Disk Management. Resolve disk access issues and bring disks back online on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Disk Set to Offline Read-Only Mode Fix

A disk set to offline or read-only mode cannot be written to. Windows marks disks offline when there are configuration conflicts, SAN policy restrictions, or driver issues preventing safe access.

## Common Causes
- SAN policy set to Offline All in diskpart
- Disk reserved by another system in a cluster
- File system corruption triggering read-only protection
- Write-protected disk or hardware write-protect switch
- Group Policy restricting disk access

## How to Fix

### Solution 1: Bring Disk Online with Diskpart

```cmd
diskpart
list disk
select disk X
online disk
attributes disk clear readonly
```

### Solution 2: Change SAN Policy

```cmd
diskpart
san
san policy OnlineAll
```

### Solution 3: Use PowerShell to Manage Disks

```powershell
Set-Disk -Number X -IsOffline $false
Set-Disk -Number X -IsReadOnly $false
```

### Solution 4: Check Disk for Errors

```cmd
chkdsk X: /f /r
```

### Solution 5: Update Storage Controller Driver

Open Device Manager and update the storage controller driver.

## Examples
```powershell
Get-Disk | Select-Object Number, FriendlyName, IsOffline, IsReadOnly, OperationalStatus | Format-Table -AutoSize
```
