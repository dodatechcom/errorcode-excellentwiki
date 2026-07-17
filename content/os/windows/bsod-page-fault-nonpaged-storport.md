---
title: "[Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA storport.sys Fix"
description: "Fix Blue Screen PAGE_FAULT_IN_NONPAGED_AREA caused by storport.sys on Windows 10 and 11. Resolve storage port driver errors with disk and driver diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD PAGE_FAULT_IN_NONPAGED_AREA storport.sys Fix

PAGE_FAULT_IN_NONPAGED_AREA with `storport.sys` as the failing driver is a critical Blue Screen caused by the storage port driver attempting to access memory that does not exist or is paged out. This indicates a problem with the storage subsystem or the storage driver.

This error commonly occurs during disk-intensive operations, with RAID arrays, or when storage drivers are outdated or corrupted.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: PAGE_FAULT_IN_NONPAGED_AREA
> What failed: storport.sys

`storport.sys` is the Windows storage port driver that communicates with storage controllers (SATA, NVMe, RAID). A page fault in non-paged area means the driver tried to access memory that was not available in physical RAM, indicating either a bug in the storage driver or insufficient memory resources.

Common triggers include:

- **Outdated storage controller driver** — Storport driver bugs causing invalid memory access
- **RAID array degradation** — Failed disks in a RAID array causing driver errors
- **Faulty SATA/NVMe controller** — Hardware issues on the storage controller
- **Insufficient memory** — System running low on physical RAM during disk operations

## Common Causes

1. **Outdated storage controller driver** — The storport driver is incompatible with the current Windows version.
2. **RAID array issues** — Degraded or failing RAID arrays cause storage driver errors.
3. **Faulty SATA/NVMe controller** — Hardware failure on the storage controller.
4. **Corrupted Windows system files** — Damaged storage-related system files.
5. **Insufficient RAM** — Memory pressure during heavy disk I/O operations.

## How to Fix

### Solution 1: Update Storage Controller Driver

**Check storage controller driver:**

```powershell
Get-WmiObject Win32_SCSIController | Select-Object Name, DriverName, DriverVersion, Status | Format-Table -AutoSize
```

Update via Device Manager:

1. Open **Device Manager**.
2. Expand **Storage controllers** or **IDE ATA/ATAPI controllers**.
3. Right-click the storage controller and select **Update driver**.
4. Choose **Search automatically for drivers**.

### Solution 2: Run CHKDSK

```cmd
chkdsk C: /f /r
```

Schedule for next restart if prompted. Check disk health:

```powershell
Get-PhysicalDisk | Select-Object DeviceId, FriendlyName, HealthStatus, OperationalStatus | Format-Table -AutoSize
```

### Solution 3: Check for Faulty RAM

Memory issues can cause page faults in storport.sys:

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Consider running MemTest86 for extended testing.

### Solution 4: Update BIOS/UEFI

Outdated BIOS can cause storage controller compatibility issues:

1. Check your motherboard manufacturer's website for BIOS updates.
2. Download and install the latest BIOS version.
3. Restart your computer.

### Solution 5: Check SATA/NVMe Cables

1. Shut down the computer.
2. Reseat SATA data cables on both the motherboard and drive.
3. Try different SATA ports.
4. For NVMe drives, reseat the M.2 drive.
5. Replace cables if damaged.

### Solution 6: Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Related Errors

- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/windows/bsod-page-fault" >}})** — Generic page fault error
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage-error" >}})** — Failed page read from disk
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Storage driver timeout errors
