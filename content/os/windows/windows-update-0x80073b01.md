---
title: "[Solution] Windows Update Error 0x80073b01 Fix"
description: "Fix Windows Update error 0x80073b01 when the update service encounters a database or store corruption error on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Update Error 0x80073b01 Fix

Windows Update error 0x80073b01 indicates the Windows Update database or store has become corrupted. The update agent cannot read or write to its internal database, preventing all update operations.

## Common Causes
- Windows Update database file corruption from interrupted updates
- SoftwareDistribution folder containing corrupted cache files
- Catroot2 folder corruption preventing signature verification
- Disk errors corrupting the Windows Update data store
- Third-party cleanup tools removing critical update files

## How to Fix

### Solution 1: Reset Windows Update Components

```cmd
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
```

### Solution 2: Run DISM Repair

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 3: Delete Update Cache Manually

```cmd
del /q /s C:\Windows\SoftwareDistribution\Download\*
del /q /s C:\Windows\SoftwareDistribution\DataStore\*
del /q /s C:\Windows\System32\catroot2\*
```

### Solution 4: Run Windows Update Troubleshooter

Go to Settings > System > Troubleshoot > Other troubleshooters and run the Windows Update troubleshooter.

### Solution 5: Check Disk Health

```cmd
chkdsk C: /f /r
```

Disk corruption can cause the update database to become corrupted.

## Examples
```powershell
Get-Service wuauserv | Select-Object Name, Status, StartType
Get-Content C:\Windows\Logs\CBS\CBS.log -Tail 30
```
