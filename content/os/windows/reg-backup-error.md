---
title: "Registry Backup Failed Error - How to Fix"
description: "Fix 'Registry backup failed' errors on Windows 10 and 11. Resolve backup failures, configure automatic registry backups, and create manual backups."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Registry Backup Failed Error

This error occurs when Windows or a tool fails to back up the registry. The error may read:

> "Registry backup failed."

or

> "Unable to create registry backup."

Since Windows 10 version 1803, automatic registry backups are disabled by default, which causes this error when tools expect them to exist.

## Common Causes

- **Automatic backup disabled** — Windows 10 1803+ no longer backs up the registry automatically.
- **Insufficient disk space** — Not enough space to save backup files.
- **Permission issues** — Can't write to the backup destination.
- **Volume Shadow Copy disabled** — Required service for backups is not running.
- **Corrupted Volume Shadow Copy** — Existing shadow copies are damaged.

## How to Fix

### Enable Automatic Registry Backups (Windows 10/11)

```cmd
reg add "HKLM\System\CurrentControlSet\Control\Session Manager\Configuration Manager" /v EnablePeriodicBackup /t REG_DWORD /d 1 /f
```

Restart your computer after running this command.

### Create Manual Registry Backup

Export entire registry:

```cmd
reg export "HKLM" "C:\Backup\HKLM_backup.reg"
reg export "HKCU" "C:\Backup\HKCU_backup.reg"
```

Export specific keys:

```cmd
reg export "HKLM\SOFTWARE\Microsoft\Windows" "C:\Backup\windows_software.reg"
```

### Backup Using PowerShell

```powershell
$backupPath = "C:\RegistryBackup"
if (!(Test-Path $backupPath)) { New-Item -ItemType Directory -Path $backupPath }
reg export "HKLM\SOFTWARE" "$backupPath\HKLM_SOFTWARE.reg"
reg export "HKCU\SOFTWARE" "$backupPath\HKCU_SOFTWARE.reg"
```

### Check Volume Shadow Copy Service

```powershell
Get-Service vss | Select-Object Status, StartType
Start-Service vss -ErrorAction SilentlyContinue
```

### Use System Restore for Registry Protection

```powershell
Enable-ComputerRestore -Drive "C:\"
Checkpoint-Computer -Description "Registry Backup" -RestorePointType MODIFY_SETTINGS
```

## Related Errors

- [Registry Restore Error]({{< relref "/os/windows/reg-restore-error" >}}) — Restore from backup fails
- [Registry Export Error]({{< relref "/os/windows/reg-export-error" >}}) — Export operation fails
- [Registry Corrupted]({{< relref "/os/windows/reg-corrupted" >}}) — Registry requires repair
