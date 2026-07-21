---
title: "[Solution] BitLocker Recovery Key Space Running Out Fix"
description: "Fix BitLocker error about insufficient space for recovery key backup on Windows. Resolve TPM storage and recovery key backup failures."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] BitLocker Recovery Key Space Running Out Fix

When BitLocker reports insufficient space for recovery key backup, the TPM chip or recovery key storage location has run out of capacity. This prevents new recovery passwords from being saved.

## Common Causes
- TPM chip has limited key storage slots
- Too many BitLocker recovery passwords stored in AD
- TPM firmware not clearing old keys properly
- Multiple operating systems consuming TPM key slots
- Group Policy forcing recovery key backup when storage is full

## How to Fix

### Solution 1: Backup and Clear Old Recovery Passwords

```powershell
Backup-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId (Get-BitLockerVolume -MountPoint "C:").KeyProtectors[0].KeyProtectorId
```

### Solution 2: Check TPM Capacity

```powershell
Get-Tpm | Select-Object TpmPresent, TpmReady
```

### Solution 3: Update TPM Firmware

Download and install the latest TPM firmware from your system manufacturer.

### Solution 4: Remove Unnecessary Key Protectors

```powershell
Get-BitLockerVolume -MountPoint "C:" | Select-Object -ExpandProperty KeyProtectors
Remove-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId <ID>
```

### Solution 5: Clear TPM and Re-enable

```powershell
Clear-Tpm
```

Back up all BitLocker recovery keys before clearing the TPM.

## Examples
```powershell
Get-Tpm | Select-Object *
Manage-BDE -Protectors -Get C:
```
