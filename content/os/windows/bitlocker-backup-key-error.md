---
title: "[Solution] BitLocker BACKUP_KEY — Recovery Key Backup Error"
description: "Fix BitLocker backup key error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1014
---

# [Solution] BitLocker BACKUP_KEY — Recovery Key Backup Error

The BitLocker backup key error occurs when you cannot save or back up the recovery key to Active Directory, Azure AD, a file, or a USB drive. Without a backup, you risk permanent data loss if the drive becomes locked.

## Description

BitLocker provides multiple options for backing up recovery keys, including saving to Active Directory, Azure AD, a file, or printing. When backup operations fail, the key is not stored in any recoverable location. The error may appear as:

> "The recovery key could not be saved to Active Directory."

> "An error occurred while backing up the BitLocker recovery information."

> "Failed to save the recovery key. The operation could not be completed."

## Common Causes

1. The computer object does not have permission to write to Active Directory.
2. The Active Directory backup extension is not installed.
3. Azure AD is not configured for BitLocker recovery key backup.
4. The destination file path is not writable.
5. Group Policy prevents backup to certain locations.
6. The BitLocker management agent is not running.
7. The Active Directory schema is missing the required BitLocker attributes.

## Solutions

### Solution 1: Backup Recovery Key to Active Directory

Save the key to Active Directory using PowerShell:

```powershell
$RecoveryPassword = (Get-BitLockerVolume -MountPoint "C:").KeyProtector | Where-Object {$_.KeyProtectorType -eq 'RecoveryPassword'}
Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $RecoveryPassword.KeyProtectorId
```

### Solution 2: Backup Recovery Key to File

Save the key to a secure file location:

```powershell
$RecoveryPassword = (Get-BitLockerVolume -MountPoint "C:").KeyProtector | Where-Object {$_.KeyProtectorType -eq 'RecoveryPassword'}
Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $RecoveryPassword.KeyProtectorId -Path "E:\Backup\BitLockerKey.txt"
```

Or export via manage-bde:

```cmd
manage-bde -protectors -get C:
manage-bde -protectors -adbackup C: -id {PROTECTOR-ID}
```

### Solution 3: Save Key to USB Drive

Export the key to an external USB drive:

```powershell
$RecoveryPassword = (Get-BitLockerVolume -MountPoint "C:").KeyProtector | Where-Object {$_.KeyProtectorType -eq 'RecoveryPassword'}
Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $RecoveryPassword.KeyProtectorId -Path "F:\BitLockerRecoveryKey.txt"
```

### Solution 4: Configure AD Backup via Group Policy

Enable Active Directory backup through Group Policy:

```powershell
# Enable the policy to backup keys to AD
$regPath = "HKLM:\SOFTWARE\Policies\Microsoft\FVE"
New-Item -Path $regPath -Force
New-ItemProperty -Path $regPath -Name "ActiveDirectoryBackup" -Value 1 -PropertyType DWORD -Force
New-ItemProperty -Path $regPath -Name "ActiveDirectoryInfoToStore" -Value 1 -PropertyType DWORD -Force
```

### Solution 5: Backup All Key Protectors

Backup all recovery passwords on all volumes:

```powershell
Get-BitLockerVolume | ForEach-Object {
    $protectors = $_.KeyProtector | Where-Object { $_.KeyProtectorType -eq 'RecoveryPassword' }
    foreach ($protector in $protectors) {
        Backup-BitLockerKeyProtector -MountPoint $_.MountPoint -KeyProtectorId $protector.KeyProtectorId
        Write-Output "Backed up key for $($_.MountPoint): $($protector.KeyProtectorId)"
    }
}
```

### Solution 6: Display and Manually Record the Key

Show the recovery key for manual recording:

```powershell
(Get-BitLockerVolume -MountPoint "C:").KeyProtector | Where-Object {$_.KeyProtectorType -eq 'RecoveryPassword'} | Select-Object -ExpandProperty RecoveryPassword
```

### Solution 7: Install the AD BitLocker Recovery Password Viewer

Install the feature to view keys in Active Directory Users and Computers:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell"
```

## Related Errors

- [BitLocker Recovery Key Error]({{< relref "/os/windows/bitlocker-recovery-key-error" >}}) — Cannot unlock drive
- [BitLocker Suspend Error]({{< relref "/os/windows/bitlocker-suspend-error" >}}) — Suspend failed
- [BitLocker TPM Error]({{< relref "/os/windows/bitlocker-tpm-error" >}}) — TPM issue
