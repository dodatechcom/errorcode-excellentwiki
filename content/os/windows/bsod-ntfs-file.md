---
title: "[Solution] BSOD NTFS_FILE_SYSTEM Windows 11/10 — Fixed"
description: "Fix Blue Screen NTFS_FILE_SYSTEM error on Windows 10 and 11. Resolve stop code 0x00000024 with disk checks, NTFS repair, and driver updates."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD NTFS_FILE_SYSTEM Windows 11/10 — Fixed

NTFS_FILE_SYSTEM is a critical Blue Screen of Death error with stop code `0x00000024`. It indicates a problem with the NTFS file system driver (Ntfs.sys) — the kernel component responsible for reading and writing NTFS volumes. The error occurs when NTFS encounters a condition it cannot handle, such as corrupted metadata, bad sectors on the system drive, or a failing storage device.

This BSOD typically appears when the hard drive or SSD is developing faults, file system metadata is damaged, or the storage controller driver has issues.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: NTFS_FILE_SYSTEM

NTFS is the primary file system used by Windows. The Ntfs.sys driver handles all file operations — reading, writing, permissions, and journaling. When NTFS encounters a corrupted Master File Table (MFT), damaged journal, or unreadable sectors, it cannot safely continue and triggers this bug check.

Common scenarios for this BSOD:

- **Failing hard drive or SSD** — Bad sectors prevent NTFS from reading critical metadata
- **After an improper shutdown** — Power loss during a write operation corrupts the NTFS journal
- **Corrupted file system** — Disk errors damage the MFT or boot sector
- **Outdated storage driver** — The storage controller miscommunicates with the drive

## Common Causes

1. **Bad sectors on the storage device** — Physical damage to the drive prevents NTFS from reading metadata.
2. **Corrupted NTFS metadata** — The MFT, journal, or boot sector is damaged.
3. **Failing hard drive or SSD** — Hardware degradation causes intermittent read/write errors.
4. **Outdated storage controller driver** — SATA, NVMe, or RAID drivers cause I/O errors.

## Solutions

### Solution 1: Run CHKDSK to Repair NTFS

CHKDSK is the primary tool for repairing NTFS file system corruption.

**Schedule a full disk check:**

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule for next restart, then reboot. CHKDSK will:
- Verify the NTFS file system structure
- Repair logical file system errors
- Scan for and map bad sectors
- Recover readable data from bad sectors

**Run CHKDSK in read-only mode to assess damage first:**

```cmd
chkdsk C: /r
```

**Check NTFS volume health:**

```powershell
Get-Volume | Where-Object {$_.FileSystem -eq "NTFS"} | Select-Object DriveLetter, FileSystemLabel, HealthStatus, SizeRemaining, Size | Format-Table -AutoSize
```

### Solution 2: Repair System Files

NTFS errors can be caused by or cause corruption in Windows system files.

```cmd
sfc /scannow
```

If SFC finds corruption it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes:

```cmd
sfc /scannow
```

Restart your computer after all scans complete.

### Solution 3: Update Storage Drivers

Storage controller driver issues can cause NTFS I/O errors.

**Check storage driver version:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC"} | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Update via Device Manager:**

1. Right-click **Start** and select **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers** or **Storage controllers**.
3. Right-click your storage controller and select **Update driver**.
4. Choose **Search automatically for drivers**.

For Intel systems, install the Intel Rapid Storage Technology (IRST) driver from [Intel's download center](https://www.intel.com/content/www/us/en/download-center/home.html).

### Solution 4: Check Drive Health

A failing drive is a common root cause. Check the SMART status for early warnings.

**Check SMART status:**

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal | Format-Table -AutoSize
```

**Get detailed disk information:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size, OperationalStatus | Format-Table -AutoSize
```

If Wear is above 90% or any ReadErrorsTotal/WriteErrorsTotal is greater than 0, back up your data immediately and replace the drive.

### Solution 5: Disable Indexing on the Affected Drive

NTFS indexing can cause additional I/O stress on a failing drive.

**Disable indexing for the C: drive:**

```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Temporary Files" -Name StateFlags0000 -ErrorAction SilentlyContinue
```

**Or disable the Windows Search service temporarily:**

```cmd
sc config WSearch start= disabled
net stop WSearch
```

Re-enable after the drive is healthy:

```cmd
sc config WSearch start= delayed-auto
net start WSearch
```

## Related Errors

- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage" >}})** — Disk read failures in kernel paging
- **[BSOD FAT_FILE_SYSTEM]({{< relref "/windows/bsod-fat-file" >}})** — Similar file system error for FAT32 volumes
- **[BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/windows/bsod-inaccessible-boot" >}})** — Boot drive inaccessible due to storage controller issues
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Storage driver timeout with similar disk root causes
