---
title: "[Solution] BSOD FAT_FILE_SYSTEM Windows 11/10 — Fixed"
description: "Fix Blue Screen FAT_FILE_SYSTEM error on Windows 10 and 11. Resolve stop code 0x00000026 with disk checks, USB drive fixes, and file system repair."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "fat", "file-system", "usb", "disk"]
weight: 5
---

# [Solution] BSOD FAT_FILE_SYSTEM Windows 11/10 — Fixed

FAT_FILE_SYSTEM is a critical Blue Screen of Death error with stop code `0x00000026`. It indicates a problem with the FAT file system driver (Fastfat.sys) — the kernel component responsible for reading and writing FAT12, FAT16, and FAT32 volumes. The error occurs when the driver encounters corrupted file allocation tables, bad sectors, or invalid directory structures on a FAT-formatted volume.

This BSOD is less common on modern systems because Windows primarily uses NTFS. However, it can appear when accessing USB drives, SD cards, external hard drives, or legacy storage devices formatted with FAT32.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: FAT_FILE_SYSTEM

The Fastfat.sys driver handles all file operations on FAT-formatted volumes. When the File Allocation Table (FAT) is corrupted — due to improper removal of USB media, bad sectors, or drive failure — the driver cannot locate files and triggers this bug check.

Common scenarios for this BSOD:

- **After inserting a USB drive** — The USB drive has a corrupted FAT32 file system
- **When accessing an SD card** — The SD card's FAT32 table is damaged
- **With external hard drives** — External drives formatted as FAT32 have file system errors
- **After improper drive removal** — Unplugging a drive without safely ejecting corrupts the FAT

## Common Causes

1. **Corrupted FAT32 file system** — The File Allocation Table is damaged on a USB or external drive.
2. **Bad sectors on removable media** — USB drives and SD cards develop physical faults.
3. **Improper drive removal** — Unplugging a drive without safely ejecting corrupts write operations.
4. **Outdated USB or storage driver** — The driver cannot properly handle FAT volume I/O.

## Solutions

### Solution 1: Remove the Problematic Drive and Run CHKDSK

If the BSOD was triggered by an external drive, remove it first, then check it on another system.

**Check the external drive on another computer:**

```cmd
chkdsk E: /f /r
```

Replace `E:` with the correct drive letter. This repairs the FAT file system and maps bad sectors.

**If you can access Windows, check all FAT volumes:**

```powershell
Get-Volume | Where-Object {$_.FileSystem -eq "FAT32" -or $_.FileSystem -eq "FAT"} | Select-Object DriveLetter, FileSystemLabel, FileSystem, HealthStatus, Size | Format-Table -AutoSize
```

### Solution 2: Safely Eject and Replace Faulty Drives

Prevent future occurrences by always safely ejecting removable media.

**Safely eject a drive using PowerShell:**

```powershell
# Find the drive's device ID
Get-Disk | Where-Object {$_.FriendlyName -like "*USB*"} | Select-Object Number, FriendlyName, Size

# Remove the device safely
Remove-Disk -Number 1
```

Or use the **Safely Remove Hardware** icon in the system tray before unplugging any drive.

**If the drive causes repeated BSODs, replace it** — USB drives and SD cards are inexpensive and unreliable once they develop bad sectors.

### Solution 3: Reformat the Problematic Drive

If CHKDSK cannot repair the FAT file system, reformat the drive.

**Reformat as FAT32 (for drives under 32GB):**

```cmd
format E: /fs:FAT32 /q
```

Replace `E:` with the correct drive letter. The `/q` flag performs a quick format.

**Reformat as exFAT (for drives over 32GB):**

```cmd
format E: /fs:exFAT /q
```

exFAT supports larger file sizes and is more resilient than FAT32.

**Warning:** Formatting erases all data on the drive. Back up important files first.

### Solution 4: Update USB Drivers

Outdated USB drivers can cause file system I/O errors on removable media.

**Check USB controller driver version:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceClass -eq "USB"} | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Update USB drivers via Device Manager:**

1. Right-click **Start** and select **Device Manager**.
2. Expand **Universal Serial Bus controllers**.
3. Right-click each **USB Root Hub** and **USB Host Controller** and select **Update driver**.
4. Choose **Search automatically for drivers**.
5. Restart your computer after updating.

### Solution 5: Check Drive Health

USB drives and SD cards have limited write endurance and can fail without warning.

**Check the physical disk status:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size, OperationalStatus | Format-Table -AutoSize
```

**Run a diagnostic scan on the drive:**

```cmd
chkdsk E: /r
```

Replace `E:` with the drive letter. If CHKDSK reports uncorrectable errors, the drive is failing and should be replaced.

## Related Errors

- **[BSOD NTFS_FILE_SYSTEM]({{< relref "/windows/bsod-ntfs-file" >}})** — Similar file system error for NTFS volumes
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures from bad sectors
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Storage driver timeouts from I/O failures
- **[BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/windows/bsod-inaccessible-boot" >}})** — Boot drive inaccessible due to storage issues
