---
title: "[Solution] BSOD FAT_FILE_SYSTEM Windows 11/10 — Fixed"
description: "Fix Blue Screen FAT_FILE_SYSTEM error on Windows 10 and 11. Repair FAT32 volumes, check disk health, and update storage drivers to resolve this file system stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "fat-file-system", "storage", "stop-code"]
weight: 5
---

# [Solution] BSOD FAT_FILE_SYSTEM Windows 11/10 — Fixed

FAT_FILE_SYSTEM is a critical Blue Screen of Death error with stop code `0x00000022`. It occurs when the FAT (File Allocation Table) file system driver encounters a fatal error while performing file system operations. The FAT driver (`fastfat.sys`) has detected corruption or an invalid state in a FAT-formatted volume that it cannot recover from.

This BSOD affects both Windows 10 and 11 and typically involves USB drives, SD cards, or secondary drives formatted with FAT12, FAT16, or FAT32. It can also occur on the system drive if it uses a FAT partition.

## Common Causes

- **Corrupted FAT volume** — The File Allocation Table is damaged by bad sectors, sudden removal, or power loss.
- **Faulty removable media** — USB flash drives, SD cards, or external drives with physical defects cause read/write failures.
- **Improper device removal** — Removing a USB drive without safely ejecting it leaves the FAT volume in an inconsistent state.
- **Outdated storage controller drivers** — USB or SATA controller drivers with I/O handling bugs.

## How to Fix

### Run CHKDSK on the Affected Volume

```cmd
chkdsk D: /f /r
```

Replace `D:` with the drive letter of the FAT-formatted volume. The `/f` flag fixes file system errors, and `/r` locates bad sectors.

**If the system drive is FAT32**, boot from a Windows installation USB:

1. Select **Repair your computer**.
2. Go to **Troubleshoot > Advanced options > Command Prompt**.
3. Run:

```cmd
chkdsk C: /f /r
```

### Safely Remove and Rescan the Device

1. Safely eject the removable device.
2. Reseat the device firmly in its port.
3. Open **Disk Management** (`Win + X` > Disk Management) and verify the volume mounts correctly.

**Or rescan from PowerShell:**

```powershell
Update-Disk
Get-Disk | Select-Object Number, FriendlyName, OperationalStatus, Size | Format-Table -AutoSize
```

### Reformat the Corrupted Volume

If CHKDSK cannot repair the FAT volume, reformatting may be necessary:

1. Back up all data from the affected drive.
2. Open **Disk Management**.
3. Right-click the volume and select **Format**.
4. Choose **FAT32** (for drives under 32GB) or **exFAT** (for larger drives).
5. Perform a **Quick Format** first. If errors persist, use a full format.

**Or from Command Prompt:**

```cmd
format D: /fs:FAT32 /q
```

### Update USB and Storage Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "USB" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Update USB controller drivers from the motherboard manufacturer's website.

### Check the Removable Drive for Hardware Failure

```powershell
Get-PhysicalDisk | Where-Object { $_.MediaType -eq "Unspecified" } | Select-Object FriendlyName, HealthStatus, Size | Format-Table -AutoSize
```

If the drive reports `Unhealthy`, replace it. USB drives and SD cards have limited write cycles and can fail without warning.

### Use CHKDSK with Fix Options for Stubborn Corruption

```cmd
chkdsk D: /f /r /x
```

The `/x` flag forces the volume to dismount before checking, which can help with drives that refuse to release file handles.

## Examples

This error commonly occurs in these scenarios:

- **After pulling out a USB drive** — Removing a USB drive without safely ejecting it corrupts the FAT table.
- **With corrupted SD cards** — SD cards in cameras or phones develop bad sectors over time.
- **When formatting fails** — An interrupted format operation leaves the FAT volume in an inconsistent state.
- **On older USB flash drives** — Aged flash memory develops read/write errors that corrupt FAT structures.

## Related Errors

- [BSOD NTFS_FILE_SYSTEM]({{< relref "/os/windows/bsod-ntfs-file-system" >}}) — Similar file system error for NTFS volumes
- [BSOD MUP_FILE_SYSTEM]({{< relref "/os/windows/bsod-mup-file-system" >}}) — Multi-UNC Provider file system error
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault-in-nonpaged-area" >}}) — Memory page fault from storage corruption
- [BSOD DPC Watchdog Violation]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — Storage driver timeout
