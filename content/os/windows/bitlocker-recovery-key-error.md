---
title: "[Solution] BitLocker RECOVERY_KEY — Cannot Unlock Drive"
description: "Fix BitLocker Recovery Key error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 1008
---

# [Solution] BitLocker RECOVERY_KEY — Cannot Unlock Drive

The BitLocker Recovery Key error occurs when you cannot unlock an encrypted drive because the recovery key is unavailable, incorrect, or the drive cannot locate the key stored in Active Directory or Azure AD.

## Description

When BitLocker cannot verify the normal unlock method (TPM, PIN, or USB key), it falls back to the 48-digit recovery key. If the recovery key is unavailable or not accepted, the drive remains locked and inaccessible. The error message may read:

> "This drive is BitLocker-protected. The recovery key is required to unlock this drive."

> "BitLocker Recovery: Enter the recovery key for this drive."

> "Unable to unlock drive. The recovery key could not be verified."

## Common Causes

1. The recovery key was not backed up or saved during BitLocker setup.
2. The TPM has been cleared or reset.
3. BIOS/UEFI settings were changed, triggering BitLocker recovery.
4. Boot order or startup configuration changed.
5. The recovery key stored in Active Directory is not accessible.
6. The recovery key was saved to the wrong Microsoft account.
7. Hardware changes caused a TPM validation failure.

## Solutions

### Solution 1: Retrieve Recovery Key from Active Directory

Query Active Directory for the recovery key:

```powershell
# Import the AD module
Import-Module ActiveDirectory

# Get recovery key for a computer
$computer = Get-ADComputer -Identity "ComputerName"
Get-ADObject -SearchBase "CN=$($computer.DistinguishedName),CN=Computers" -Filter {objectClass -eq 'msFVE-RecoveryInformation'} -Properties msFVE-RecoveryPassword | Select-Object -ExpandProperty msFVE-RecoveryPassword
```

### Solution 2: Use the Recovery Key from Microsoft Account

If the key was saved to a Microsoft account, retrieve it from https://account.microsoft.com/devices/recoverykey.

### Solution 3: Use manage-bde to Unlock

Unlock the drive using the command-line tool:

```cmd
manage-bde -unlock C: -RecoveryPassword YOUR-48-DIGIT-KEY
```

Or with the recovery key file:

```cmd
manage-bde -unlock C: -RecoveryKey "F:\RecoveryKey.bek"
```

### Solution 4: Suspend BitLocker and Reboot

Temporarily suspend BitLocker to allow drive access:

```powershell
Suspend-BitLocker -MountPoint "C:" -RebootCount 1
```

### Solution 5: Backup Recovery Key to Active Directory

Prevent future issues by backing up the current key:

```powershell
$RecoveryPassword = (Get-BitLockerVolume -MountPoint "C:").KeyProtector | Where-Object {$_.KeyProtectorType -eq 'RecoveryPassword'}
Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $RecoveryPassword.KeyProtectorId
```

### Solution 6: Add Recovery Key to TPM

If the TPM lost its measurements, re-add the key protector:

```powershell
Add-BitLockerKeyProtector -MountPoint "C:" -TpmAndPinProtector
```

### Solution 7: Check BitLocker Status

Verify the current encryption and lock status:

```powershell
Get-BitLockerVolume | Format-Table MountPoint, VolumeStatus, ProtectionStatus, EncryptionMethod
manage-bde -status C:
```

## Related Errors

- [BitLocker Unlock Error]({{< relref "/os/windows/bitlocker-unlock-error" >}}) — Drive unlock failed
- [BitLocker TPM Error]({{< relref "/os/windows/bitlocker-tpm-error" >}}) — TPM issue
- [BitLocker Mount Error]({{< relref "/os/windows/bitlocker-mount-error" >}}) — Cannot mount encrypted drive
