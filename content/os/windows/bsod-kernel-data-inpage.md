---
title: "[Solution] BSOD KERNEL_DATA_INPAGE_ERROR Windows 11/10 — Fixed"
description: "Fix Blue Screen KERNEL_DATA_INPAGE_ERROR on Windows 10 and 11. Resolve stop code 0x0000007A with disk checks, driver updates, and memory diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD KERNEL_DATA_INPAGE_ERROR Windows 11/10 — Fixed

KERNEL_DATA_INPAGE_ERROR is a critical Blue Screen of Death error with stop code `0x0000007A`. It indicates that the kernel could not locate a page of kernel data in the paging file — the data was requested but not found in memory or on disk. This points to a failure in reading data from the hard drive or SSD into system memory.

This BSOD typically strikes when the storage device is failing, has bad sectors, or when the disk controller driver is malfunctioning. It can also appear with faulty RAM or corrupted page file settings.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: KERNEL_DATA_INPAGE_ERROR

The Windows kernel maintains a page file on disk that stores data temporarily moved out of physical RAM. When the kernel requests a specific page of data and the I/O operation fails — either because the disk cannot read the sector, the page file is corrupted, or the storage driver has malfunctioned — Windows triggers this bug check.

Common scenarios for this BSOD:

- **Failing hard drive or SSD** — Bad sectors or dying NAND cells prevent data reads
- **Corrupted page file** — The page file is damaged or incorrectly configured
- **Faulty SATA/NVMe cables** — Physical connection issues interrupt disk reads
- **Outdated storage drivers** — The storage controller cannot properly handle I/O requests

## Common Causes

1. **Failing storage device** — Hard drives with bad sectors or SSDs with failing NAND cells.
2. **Corrupted or missing page file** — The virtual memory file is damaged or deleted.
3. **Faulty storage controller driver** — SATA, NVMe, or RAID drivers are outdated or corrupted.
4. **Bad RAM causing read failures** — Memory errors prevent proper data transfer from disk.

## Solutions

### Solution 1: Check Disk Health with CHKDSK

Run a thorough disk scan to identify and repair bad sectors.

**Schedule a disk check on next restart:**

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule the check for the next restart, then reboot your computer. CHKDSK will scan the entire disk, repair file system errors, and mark bad sectors.

**Run CHKDSK in read-only mode first to assess damage:**

```cmd
chkdsk C: /r
```

**Check disk SMART status for early warning signs:**

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal | Format-Table -AutoSize
```

A high Wear value (above 90%) or any ReadErrorsTotal/WriteErrorsTotal greater than 0 indicates a failing drive.

### Solution 2: Rebuild the Page File

A corrupted or incorrectly sized page file can cause this BSOD.

**Reset the page file to automatic management:**

```powershell
wmic computersystem set AutomaticManagedPagefile=True
wmic pagefileset where name="C:\\pagefile.sys" delete
```

Restart your computer. Windows will automatically recreate the page file.

**Manually set a fixed page file size if automatic management fails:**

1. Press `Win + R`, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab.
3. Under **Performance**, click **Settings**.
4. Go to the **Advanced** tab.
5. Under **Virtual memory**, click **Change**.
6. Check **Automatically manage paging file size for all drives**.
7. Click **OK** and restart.

### Solution 3: Update Storage Drivers

Outdated or corrupted storage drivers are a common cause of I/O failures.

**Check current storage driver version:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC"} | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Update drivers via Device Manager:**

1. Right-click the **Start** button and select **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers** or **Storage controllers**.
3. Right-click your storage controller and select **Update driver**.
4. Choose **Search automatically for drivers**.

For Intel systems, install the Intel Rapid Storage Technology (IRST) driver from [Intel's download center](https://www.intel.com/content/www/us/en/download-center/home.html).

### Solution 4: Run System File Checker

Corrupted system files can cause the kernel to request invalid pages.

```cmd
sfc /scannow
```

If SFC finds errors it cannot fix:

```cmd
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Run SFC again after DISM completes and restart.

### Solution 5: Test RAM for Errors

Faulty RAM can corrupt data as it's being read from disk.

**Run Windows Memory Diagnostic:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Results appear in Event Viewer under **Windows Logs > System** with source `MemoryDiagnostics-Results`.

**Extended test with MemTest86:**

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB and boot from it.
3. Let the test run for at least **4 full passes**.
4. Any single error confirms faulty RAM.

## Related Errors

- **[BSOD INACCESSIBLE_BOOT_DEVICE]({{< relref "/windows/bsod-inaccessible-boot" >}})** — Storage controller failure preventing Windows from accessing the boot drive
- **[BSOD NTFS_FILE_SYSTEM]({{< relref "/windows/bsod-ntfs-file" >}})** — NTFS file system corruption on the system drive
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Storage driver timeout with similar disk I/O root causes
- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault" >}})** — Memory page errors often linked to the same storage or RAM issues
