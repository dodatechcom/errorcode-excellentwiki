---
title: "[Solution] BitLocker TPM Unlock Failed Error Fix"
description: "Fix BitLocker TPM unlock failure on Windows when the Trusted Platform Module cannot release the encryption key to unlock the drive."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] BitLocker TPM Unlock Failed Error Fix

BitLocker TPM unlock failures prevent the encrypted drive from unlocking automatically at boot. The TPM chip cannot validate the boot environment and refuses to release the encryption key.

## Common Causes
- BIOS or UEFI update changing boot measurements
- Secure Boot configuration modified after BitLocker was enabled
- TPM firmware update clearing stored keys
- Boot configuration data (BCD) modified
- BIOS update or hardware change invalidating TPM measurements

## How to Fix

### Solution 1: Enter Recovery Key

At the BitLocker recovery screen, enter your 48-digit recovery key from your Microsoft account, USB drive, or printed backup.

### Solution 2: Suspend BitLocker Before Changes

```powershell
Suspend-BitLocker -MountPoint "C:" -RebootCount 1
```

Suspend BitLocker before making BIOS, boot, or hardware changes.

### Solution 3: Clear and Re-enable TPM

```powershell
Clear-Tpm
Enable-Tpm
```

Back up BitLocker recovery keys before clearing the TPM.

### Solution 4: Update BIOS and TPM

Ensure both BIOS and TPM firmware are updated to the latest versions.

### Solution 5: Disable Secure Boot Temporarily

Enter BIOS and disable Secure Boot to test if boot measurements are causing the TPM unlock failure.

## Examples
```powershell
Get-Tpm | Select-Object TpmPresent, TpmReady, TpmEnabled
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus
```
