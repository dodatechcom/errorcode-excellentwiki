---
title: "[Solution] Windows Update Error Retry Loop Fix"
description: "Fix Windows Update that fails and retries endlessly without completing installation on Windows 10 and 11. Break the update retry loop on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Update Error Retry Loop Fix

Windows Update enters a retry loop when an update repeatedly fails to install, triggers a rollback, and then attempts to install again. This wastes resources and prevents other updates from installing.

## Common Causes
- Corrupted update package in the SoftwareDistribution cache
- Pending reboot blocking update installation
- Windows Update components in a confused state
- Disk space exhaustion during installation
- System file corruption preventing update completion

## How to Fix

### Solution 1: Clear SoftwareDistribution Completely

```cmd
net stop wuauserv
net stop bits
rd /s /q C:\Windows\SoftwareDistribution
mkdir C:\Windows\SoftwareDistribution
net start bits
net start wuauserv
```

### Solution 2: Run DISM and SFC

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 3: Hide the Problematic Update

Use Microsoft wushowhide.diagcab tool to hide the failing update and install it later.

### Solution 4: In-Place Upgrade

Download the Windows Media Creation Tool and perform an in-place upgrade repair.

### Solution 5: Check CBS Logs for Specific Errors

```powershell
Get-Content C:\Windows\Logs\CBS\CBS.log -Tail 100 | Select-String -Pattern "error|fail"
```

## Examples
```powershell
Get-WindowsUpdate | Select-Object Title, KB, Size
```
