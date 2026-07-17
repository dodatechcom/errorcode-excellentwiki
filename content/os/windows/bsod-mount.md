---
title: "[Solution] BSOD MOUNT_NOT_SUPPORTED Windows 11/10 — Fixed"
description: "Fix Blue Screen MOUNT_NOT_SUPPORTED error on Windows 10 and 11. Resolve stop code 0x000000EA with volume mount fixes and storage configuration."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "mount", "volume", "storage", "ntfs"]
weight: 5
---

# [Solution] BSOD MOUNT_NOT_SUPPORTED Windows 11/10 — Fixed

MOUNT_NOT_SUPPORTED is a critical Blue Screen of Death error with stop code `0x000000EA`. It indicates that the Windows mount manager failed to mount a file system volume. This is an unusual BSOD that typically occurs when Windows cannot properly initialize or attach a storage volume during the boot process or when a new volume is being mounted.

This error is rare on standard desktop systems and more commonly seen in enterprise environments with complex storage configurations, virtual machines, or when using unusual disk partitioning schemes.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: MOUNT_NOT_SUPPORTED

The Windows mount manager is responsible for assigning drive letters and mount points to volumes. When it encounters a volume it cannot mount — due to file system corruption, partition table issues, or incompatible volume formats — the kernel cannot proceed and triggers this bug check.

Common scenarios for this BSOD:

- **After partitioning changes** — Modifying partitions confused the mount manager
- **With dynamic disks** — Dynamic disk configurations cause mount failures
- **In virtual machine environments** — Virtual disk formats incompatible with Windows mount
- **After cloning disks** — Cloned partitions have conflicting GUIDs or signatures

## Common Causes

1. **Corrupted partition table** — The disk's partition table is damaged or inconsistent.
2. **Conflicting volume signatures** — Two disks share the same disk signature after cloning.
3. **Dynamic disk errors** — Dynamic volume configurations are corrupted.
4. **Mount point conflicts** — Duplicate or invalid mount points cause the mount manager to fail.

## Solutions

### Solution 1: Use DiskPart to Fix Volume Issues

DiskPart can repair partition and volume issues that cause mount failures.

**Open DiskPart:**

```cmd
diskpart
```

**List all disks and volumes:**

```diskpart
list disk
list volume
```

**Check for conflicting disk signatures:**

```diskpart
select disk 0
detail disk
```

If two disks have the same signature, one needs a new signature. In Disk Management (diskmgmt.msc), right-click the disk and select **Change Online/Offline** to resolve conflicts.

**Clean and reformat a problematic non-system disk:**

```diskpart
select disk 1
clean
create partition primary
format fs=ntfs quick
assign letter=D
```

**Warning:** This erases all data on the selected disk. Only use on non-system disks.

### Solution 2: Rebuild the BCD Store

A corrupted Boot Configuration Data store can cause mount failures during startup.

**Boot into Recovery Environment and run:**

```cmd
bootrec /fixmbr
bootrec /fixboot
bootrec /rebuildbcd
```

**Rebuild BCD from scratch:**

```cmd
bcdboot C:\Windows /s C: /f ALL
```

**If bootrec cannot find Windows installations:**

```cmd
bcdedit /export C:\BCD_Backup
cd /d C:\Boot
ren BCD BCD.old
bootrec /rebuildbcd
```

### Solution 3: Run CHKDSK on the System Drive

File system corruption can prevent the mount manager from initializing volumes.

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule for next restart, then reboot.

**Check all volumes for errors:**

```powershell
Get-Volume | Where-Object {$_.DriveLetter -ne $null} | Select-Object DriveLetter, FileSystem, FileSystemLabel, HealthStatus | Format-Table -AutoSize
```

### Solution 4: Fix Disk Signatures After Cloning

If you cloned a disk, both disks may have the same MBR signature, causing mount conflicts.

**Identify duplicate signatures:**

```powershell
Get-Disk | Select-Object Number, FriendlyName, PartitionStyle, IsSystem, IsBoot | Format-Table -AutoSize
```

**Clear the disk signature on the secondary disk (non-system):**

1. Open **Disk Management** (diskmgmt.msc).
2. Right-click the cloned disk (not the system disk).
3. Select **Offline** then **Online** to force a new signature.
4. If that doesn't work, use DiskPart to clean the disk and recreate partitions.

### Solution 5: Check for Virtual Disk Issues

In virtual machine environments, disk format mismatches can cause mount failures.

**For Hyper-V:**

```powershell
Get-VHD -Path "C:\Users\Public\Documents\Hyper-V\Virtual Hard Disks\VM.vhdx" | Select-Object VhdType, FileSize, Size | Format-Table -AutoSize
```

Ensure the virtual disk format is compatible with your Hyper-V version. Convert VHD to VHDX if needed.

**For VMware/VirtualBox:**

Export the virtual disk to a compatible format and re-import it.

## Related Errors

- **[BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/windows/bsod-inaccessible-boot" >}})** — Boot drive access failure from storage driver issues
- **[BSOD NTFS_FILE_SYSTEM]({{< relref "/windows/bsod-ntfs-file" >}})** — NTFS corruption on the system drive
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures from corrupted volumes
- **[BSOD CRITICAL_PROCESS_DIED]({{< relref "/windows/bsod-critical-process" >}})** — Critical process failure from disk mount issues
