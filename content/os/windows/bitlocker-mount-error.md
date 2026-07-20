---
title: "[Solution] BitLocker MOUNT — Cannot Mount Encrypted Drive"
description: "Fix BitLocker mount error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1011
---

# [Solution] BitLocker MOUNT — Cannot Mount Encrypted Drive

The BitLocker mount error prevents an encrypted drive from being mounted and accessed in File Explorer. The drive may appear but remain inaccessible, or it may not appear at all as a mountable volume.

## Description

When a BitLocker-encrypted drive cannot be mounted, the operating system is unable to present the volume to the file system for access. This typically happens with external drives, secondary volumes, or drives moved between systems. The error may appear as:

> "This drive is locked by BitLocker Drive Encryption. You must unlock this drive before you can use it."

> "The volume does not contain a recognized file system."

> "Access is denied" when trying to access the drive.

## Common Causes

1. The drive was encrypted on a different computer and is not recognized.
2. The BitLocker drive letter assignment was removed.
3. The drive is in a raw or unallocated state due to corruption.
4. BitLocker metadata on the volume is damaged.
5. The removable drive was formatted while encrypted.
6. USB or SATA controller issues prevent the drive from being recognized.
7. Group Policy prevents mounting encrypted removable drives.

## Solutions

### Solution 1: Unlock the Drive First

Unlock the drive before mounting:

```powershell
Unlock-BitLocker -MountPoint "D:" -Password (Read-Host -AsSecureString "Password")
```

Using manage-bde:

```cmd
manage-bde -unlock D: -Password
```

### Solution 2: Check BitLocker Status

Verify the drive encryption and lock status:

```powershell
Get-BitLockerVolume | Format-Table MountPoint, VolumeStatus, LockStatus, CapacityRemaining
manage-bde -status
```

### Solution 3: Assign a Drive Letter

If the drive is missing a letter, assign one:

```powershell
Get-Disk | Where-Object PartitionStyle -ne "RAW" | Get-Partition | Format-Table DiskNumber, PartitionNumber, DriveLetter

# Assign drive letter
Get-Volume | Where-Object FileSystemLabel -like "*BitLocker*" | Get-Partition | Set-Partition -NewDriveLetter "D"
```

Or via diskpart:

```cmd
diskpart
list volume
select volume X
assign letter=D
exit
```

### Solution 4: Repair BitLocker Metadata

If the metadata is corrupted, repair it:

```powershell
Repair-BitLocker -MountPoint "D:" -VolumeProvisioningSizeKB 0
```

### Solution 5: Disable and Re-enable BitLocker

Decrypt and re-encrypt the drive:

```powershell
Disable-BitLocker -MountPoint "D:"
# Wait for decryption to complete
Get-BitLockerVolume -MountPoint "D:" | Select-Object EncryptionPercentage
Enable-BitLocker -MountPoint "D:" -EncryptionMethod Aes256 -UsedSpaceOnly
```

### Solution 6: Check Drive Health

Run diagnostics on the physical drive:

```powershell
# Check disk health
Get-PhysicalDisk | Select-Object FriendlyName, HealthStatus, OperationalStatus

# Run chkdsk after unlocking
chkdsk D: /f /r
```

### Solution 7: Use manage-bde to Force Access

Force access to the locked drive:

```cmd
manage-bde -lock D:
manage-bde -unlock D: -RecoveryPassword YOUR-RECOVERY-KEY
manage-bde -off D:
```

## Related Errors

- [BitLocker Unlock Error]({{< relref "/os/windows/bitlocker-unlock-error" >}}) — Drive unlock failed
- [BitLocker Recovery Key Error]({{< relref "/os/windows/bitlocker-recovery-key-error" >}}) — Cannot unlock drive
- [BitLocker TPM Error]({{< relref "/os/windows/bitlocker-tpm-error" >}}) — TPM issue
