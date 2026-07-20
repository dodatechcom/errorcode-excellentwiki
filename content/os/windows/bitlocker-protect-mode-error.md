---
title: "[Solution] BitLocker PROTECT_MODE — Protection Mode Error"
description: "Fix BitLocker protect mode error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1012
---

# [Solution] BitLocker PROTECT_MODE — Protection Mode Error

The BitLocker protection mode error occurs when the drive's protection status is inconsistent or when BitLocker transitions between protected and unprotected states unexpectedly. This can leave the drive partially encrypted or vulnerable.

## Description

BitLocker protection mode determines whether a volume is actively protected by encryption and key validation. When the protection mode encounters errors, the drive may show as unprotected even though encryption is present, or protection may fail to activate after being suspended. Errors include:

> "BitLocker is not using any key protectors for volume C:. Recovery and hardware key protectors are disabled."

> "The drive is not protected. BitLocker cannot encrypt the volume because protection mode is not active."

> "Protection is suspended for this volume. Data on this volume is not encrypted."

## Common Causes

1. BitLocker protection was suspended and not resumed.
2. All key protectors were removed from the volume.
3. Group Policy disabled BitLocker protection.
4. The TPM protector was removed or failed validation.
5. Encryption was interrupted and not completed.
6. The system was moved to a different hardware configuration.
7. The BitLocker service encountered an error during state transition.

## Solutions

### Solution 1: Check Current Protection Status

Verify the current BitLocker protection state:

```powershell
Get-BitLockerVolume | Select-Object MountPoint, ProtectionStatus, VolumeStatus, KeyProtector
manage-bde -status C:
```

### Solution 2: Resume BitLocker Protection

Resume protection if it was suspended:

```powershell
Resume-BitLocker -MountPoint "C:"
```

Check if resume is possible:

```powershell
Get-BitLockerVolume -MountPoint "C:" | Select-Object MountPoint, ProtectionStatus
```

### Solution 3: Suspend and Resume Protection

Reset the protection state by suspending and resuming:

```powershell
Suspend-BitLocker -MountPoint "C:" -RebootCount 0
Resume-BitLocker -MountPoint "C:"
```

### Solution 4: Re-add Key Protectors

If key protectors are missing, add them back:

```powershell
# Add TPM protector
Add-BitLockerKeyProtector -MountPoint "C:" -TpmProtector

# Add recovery password protector
Add-BitLockerKeyProtector -MountPoint "C:" -RecoveryPasswordProtector

# Verify protectors are present
Get-BitLockerVolume -MountPoint "C:" | Select-Object -ExpandProperty KeyProtector
```

### Solution 5: Enable BitLocker Protection via manage-bde

Use the command line to manage protection:

```cmd
manage-bde -protectors -enable C:
manage-bde -protectors -get C:
```

### Solution 6: Check Group Policy Settings

Verify that Group Policy is not disabling BitLocker:

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\FVE" -ErrorAction SilentlyContinue
```

Key registry values to check:

```powershell
# Disable BitLocker
Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\FVE" -Name "DisableExternalDMAEncryption" -ErrorAction SilentlyContinue
```

### Solution 7: Force Re-encryption

If the volume is partially encrypted, restart the encryption process:

```powershell
Resume-BitLocker -MountPoint "C:"
Start-BitLockerEncryption -MountPoint "C:"
```

## Related Errors

- [BitLocker Suspend Error]({{< relref "/os/windows/bitlocker-suspend-error" >}}) — Suspend failed
- [BitLocker Unlock Error]({{< relref "/os/windows/bitlocker-unlock-error" >}}) — Drive unlock failed
- [BitLocker TPM Error]({{< relref "/os/windows/bitlocker-tpm-error" >}}) — TPM issue
