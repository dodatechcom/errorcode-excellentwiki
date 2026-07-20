---
title: "[Solution] Error 19 — WRITE_PROTECT Fix"
description: "Fix Windows Error Code (WRITE_PROTECT) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 19
---

# [Solution] Error 19 — WRITE_PROTECT Fix

Win32 error 19 (`ERROR_WRITE_PROTECT`) occurs when the media is write protected. This prevents any write operations to a disk, drive, or removable media that has write protection enabled.

## Description

The WRITE_PROTECT error is returned when a write operation is attempted on a disk or storage device that is configured as read-only. This applies to physical write-protect switches, software write protection, and disk attributes. The error code is `ERROR_WRITE_PROTECT` (value 19). The full message reads:

> "The media is write protected."

## Common Causes

1. The removable media has a physical write-protect switch enabled.
2. The disk attributes are set to read-only via software.
3. The disk is a WORM (Write Once Read Many) media.
4. BitLocker or encryption is preventing write access.
5. Group Policy restricts writing to removable media.
6. The disk is corrupted and Windows mounted it as read-only.

## Solutions

### Solution 1: Check Write Protection Switch

Check for and disable the physical write-protect switch on removable media:

```powershell
# Check disk attributes
diskpart
list disk
select disk N
attributes disk
```

### Solution 2: Clear Read-Only Disk Attributes

Remove the software write protection:

```cmd
diskpart
list disk
select disk N
attributes disk clear readonly
exit
```

```powershell
# Clear read-only attribute via PowerShell
Set-Disk -Number N -IsReadOnly $false
```

### Solution 3: Format the Disk

If the disk needs to be reset, format it:

```cmd
:: Format the disk (WARNING: destroys all data)
format E: /fs:ntfs /q
```

```powershell
# Format via PowerShell
Clear-Disk -Number N -RemoveData -Confirm:$false
Initialize-Disk -Number N -PartitionStyle MBR
New-Partition -DiskNumber N -UseMaximumSize -DriveLetter E | Format-Volume -FileSystem NTFS -NewFileSystemLabel "Data"
```

### Solution 4: Check Group Policy

Ensure Group Policy is not restricting write access to removable disks:

```powershell
# Check for removable storage write restriction policy
Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices" -ErrorAction SilentlyContinue
```

### Solution 5: Use Registry to Remove Write Protection

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\StorageDevicePolicies]
"WriteProtect"=dword:00000000
```

Apply:

```cmd
reg import remove_writeprotect.reg
```

## Related Errors

- [Error 23 — CRC]({{< relref "/os/windows/win32-crc-error" >}}) — Data error (cyclic redundancy check)
- [Error 21 — NOT_READY]({{< relref "/os/windows/win32-not-ready" >}}) — The device is not ready
- [Error 112 — DISK_FULL]({{< relref "/os/windows/win32-disk-full" >}}) — There is not enough space on the disk
