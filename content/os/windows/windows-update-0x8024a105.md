---
title: "[Solution] Windows Update Error 0x8024a105 Fix"
description: "Fix Windows Update error 0x8024a105 WU_E_UH_POSTREBOOTSTILLPENDING when a post-reboot operation is still pending on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Update Error 0x8024a105 Fix

Windows Update error 0x8024a105 (WU_E_UH_POSTREBOOTSTILLPENDING) indicates the update handler requires a reboot to complete a previous installation, but the reboot has not yet been performed.

## Common Causes
- A previous update requires a restart that was not completed
- Pending file rename operations blocking update processing
- Windows Installer waiting for a reboot before committing changes
- Group Policy update requiring restart for enforcement

## How to Fix

### Solution 1: Restart Your Computer

Perform a full restart using the Restart option (not Shut down then Power on).

### Solution 2: Check Pending File Rename Operations

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" /v PendingFileRenameOperations
```

### Solution 3: Force Pending Operations to Complete

```cmd
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" /v PendingFileRenameOperations /f
```

Only do this if you are certain no critical updates are pending.

### Solution 4: Clear the SoftwareDistribution Folder

```cmd
net stop wuauserv
rd /s /q C:\Windows\SoftwareDistribution
net start wuauserv
```

### Solution 5: Run DISM Repair

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples
```powershell
Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager" -Name PendingFileRenameOperations -ErrorAction SilentlyContinue
```
