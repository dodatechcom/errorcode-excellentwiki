---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION volsnap.sys Fix"
description: "Fix SYSTEM_THREAD_EXCEPTION caused by volsnap.sys on Windows. Resolve Volume Shadow Copy driver crash and snapshot operation BSOD failures."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION volsnap.sys Fix

The SYSTEM_THREAD_EXCEPTION referencing volsnap.sys indicates a crash in the Volume Shadow Copy driver. This driver manages point-in-time snapshots of disk volumes for backup and restore operations.

## Common Causes
- Corrupted volume shadow copy storage area
- Third-party backup software conflicting with VSS
- Insufficient disk space for shadow copy operations
- Disk I/O errors during snapshot creation
- Windows update corrupting the volsnap driver

## How to Fix

### Solution 1: Check Shadow Copy Storage

```cmd
vssadmin list shadowstorage
vssadmin resize shadowstorage /for=C: /on=C: /maxsize=10%
```

### Solution 2: Delete Old Shadow Copies

```cmd
vssadmin delete shadows /all /quiet
```

### Solution 3: Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Solution 4: Check Disk Health

```cmd
chkdsk C: /f /r
```

### Solution 5: Update Backup Software

Ensure your backup application is updated to the latest version compatible with your Windows build.

## Examples
```powershell
vssadmin list shadows
vssadmin list shadowstorage
Get-Service VSS | Select-Object Status, StartType
```
