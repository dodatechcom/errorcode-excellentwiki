---
title: "[Solution] BitLocker UNLOCK — Drive Unlock Failed"
description: "Fix BitLocker unlock error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1009
---

# [Solution] BitLocker UNLOCK — Drive Unlock Failed

The BitLocker unlock error occurs when a BitLocker-encrypted drive cannot be unlocked using the configured method, leaving the data inaccessible. This commonly affects non-OS drives or drives where the TPM cannot validate the system integrity.

## Description

When a BitLocker-locked drive fails to unlock, the drive remains in a locked state and cannot be accessed through File Explorer or the command line. The error may appear as:

> "You must first unlock this drive before you can access its contents."

> "BitLocker Drive Encryption failed to unlock the drive. The PIN or password is incorrect."

> "An error occurred while attempting to start BitLocker Drive Encryption service."

## Common Causes

1. The drive was locked due to a security policy change.
2. The TPM detected a hardware or firmware change.
3. The USB key or smart card used for unlock is unavailable.
4. The BitLocker service is stopped or disabled.
5. The drive was encrypted on a different computer.
6. Incorrect unlock password or PIN was entered.
7. The drive's metadata is corrupted.

## Solutions

### Solution 1: Unlock with manage-bde Command

Use the command-line utility to unlock the drive:

```cmd
manage-bde -unlock D: -Password
```

With a recovery password:

```cmd
manage-bde -unlock D: -RecoveryPassword 111111-222222-333333-444444-555555-666666-777777-888888
```

### Solution 2: Check BitLocker Status

Verify the drive status before attempting unlock:

```powershell
Get-BitLockerVolume | Format-Table MountPoint, VolumeStatus, LockStatus, ProtectionStatus
manage-bde -status D:
```

### Solution 3: Start the BitLocker Service

Ensure the BitLocker service is running:

```powershell
Get-Service -Name "BDESVC"
Start-Service -Name "BDESVC"
Set-Service -Name "BDESVC" -StartupType Manual
```

### Solution 4: Unlock via PowerShell

Use PowerShell cmdlets to unlock:

```powershell
$securePassword = Read-Host -AsSecureString -Prompt "Enter BitLocker Password"
Unlock-BitLocker -MountPoint "D:" -Password $securePassword
```

### Solution 5: Remove and Re-add Key Protector

If the key protector is corrupted, remove and re-add it:

```powershell
Get-BitLockerVolume -MountPoint "D:" | Select-Object -ExpandProperty KeyProtector
Remove-BitLockerKeyProtector -MountPoint "D:" -KeyProtectorId "PROTECTOR-ID"
Add-BitLockerKeyProtector -MountPoint "D:" -PasswordProtector
```

### Solution 6: Check TPM Status

If the drive uses TPM for unlock, verify TPM is functional:

```powershell
Get-Tpm | Format-List TpmPresent, TpmReady, Owned
Get-TpmEndorsementKeyInfo
```

### Solution 7: Force Dismount and Remount

Force a clean re-mount of the locked volume:

```powershell
Dismount-BitLockerProtector -MountPoint "D:" -KeyProtectorId "PROTECTOR-ID"
Unlock-BitLocker -MountPoint "D:" -RecoveryPassword "YOUR-KEY"
```

## Related Errors

- [BitLocker Recovery Key Error]({{< relref "/os/windows/bitlocker-recovery-key-error" >}}) — Cannot unlock drive
- [BitLocker TPM Error]({{< relref "/os/windows/bitlocker-tpm-error" >}}) — TPM issue
- [BitLocker Mount Error]({{< relref "/os/windows/bitlocker-mount-error" >}}) — Cannot mount encrypted drive
