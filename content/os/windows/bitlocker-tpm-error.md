---
title: "[Solution] BitLocker TPM — TPM Validation Error"
description: "Fix BitLocker TPM error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1010
---

# [Solution] BitLocker TPM — TPM Validation Error

The BitLocker TPM error occurs when BitLocker cannot validate the Trusted Platform Module, causing the system to enter recovery mode or preventing drive encryption. This is commonly triggered by firmware updates, hardware changes, or TPM misconfiguration.

## Description

BitLocker relies on the TPM to store encryption keys and verify system integrity during boot. When the TPM validation fails, BitLocker cannot confirm that the system has not been tampered with, and it locks the drive. The error appears as:

> "BitLocker cannot use the Trusted Platform Module because its firmware is inconsistent with the expected TPM state."

> "The TPM has not been initialized. BitLocker requires the TPM to be initialized."

> "A TPM command failed to complete. TPM is in a failed state."

## Common Causes

1. BIOS or UEFI firmware was updated, changing TPM measurements.
2. The TPM was cleared or reset intentionally or by malware.
3. Hardware changes (new motherboard, GPU, or RAM) altered boot measurements.
4. TPM drivers are outdated or missing.
5. TPM is disabled in BIOS/UEFI settings.
6. TPM firmware is incompatible with the current Windows version.
7. A TPM lockout occurred after too many failed authentication attempts.

## Solutions

### Solution 1: Clear and Re-initialize the TPM

Clear the TPM to start fresh (WARNING: this removes all TPM-stored keys):

```powershell
# Check TPM status first
Get-Tpm | Format-List

# Clear TPM via PowerShell (requires reboot)
Clear-Tpm -OwnerAuth (Get-TpmOwnerAuth)
```

Or clear through the TPM Management console:

```cmd
tpm.msc
```

### Solution 2: Update BIOS and TPM Firmware

Check for BIOS and TPM firmware updates from your manufacturer:

```powershell
# Check current BIOS version
Get-WmiObject -Class Win32_BIOS | Select-Object Manufacturer, SMBIOSBIOSVersion, ReleaseDate

# Check TPM version
Get-Tpm | Format-List ManufacturerId, ManufacturerVersion
```

### Solution 3: Enable TPM in BIOS

Reboot and enter BIOS/UEFI to enable TPM:

1. Restart the computer and press the BIOS key (usually F2, F10, or Del).
2. Navigate to Security or Advanced settings.
3. Enable Intel PTT (Platform Trust Technology) or AMD fTPM.
4. Save and exit.

### Solution 4: Remove BitLocker Key from TPM

Remove the TPM key protector and use an alternative:

```powershell
Get-BitLockerVolume -MountPoint "C:" | Select-Object -ExpandProperty KeyProtector
Remove-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId "TPM-ID"
Add-BitLockerKeyProtector -MountPoint "C:" -RecoveryPasswordProtector
```

### Solution 5: Suspend BitLocker Before Hardware Changes

Always suspend BitLocker before BIOS updates or hardware changes:

```powershell
Suspend-BitLocker -MountPoint "C:" -RebootCount 1
```

Resume after the change:

```powershell
Resume-BitLocker -MountPoint "C:"
```

### Solution 6: Install TPM Updates

Install the latest TPM driver from Windows Update:

```powershell
# Check for TPM driver
Get-PnpDevice | Where-Object { $_.FriendlyName -like "*TPM*" }

# Update drivers
pnputil /scan-devices
```

### Solution 7: Reset TPM Lockout

If the TPM is in lockout due to failed attempts:

```powershell
# Check lockout status
Get-Tpm | Format-List TpmReady, LockedOut

# Reset TPM lockout with owner auth
Reset-TpmOwnerAuth
```

## Related Errors

- [BitLocker Recovery Key Error]({{< relref "/os/windows/bitlocker-recovery-key-error" >}}) — Cannot unlock drive
- [BitLocker Unlock Error]({{< relref "/os/windows/bitlocker-unlock-error" >}}) — Drive unlock failed
- [BitLocker Suspend Error]({{< relref "/os/windows/bitlocker-suspend-error" >}}) — Suspend failed
