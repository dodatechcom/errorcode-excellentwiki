---
title: "[Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ataport.SYS Fix"
description: "Fix Blue Screen DRIVER_IRQL_NOT_LESS_OR_EQUAL caused by ataport.SYS on Windows 10 and 11. Resolve ATA port driver errors with storage driver updates and disk diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ataport.SYS Fix

DRIVER_IRQL_NOT_LESS_OR_EQUAL with `ataport.SYS` as the failing driver is a critical Blue Screen caused by the ATA port driver accessing memory at an incorrect interrupt request level. This driver manages communication with ATA/SATA storage devices.

This error commonly occurs during disk-intensive operations, when storage devices are failing, or when storage drivers are outdated.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: DRIVER_IRQL_NOT_LESS_OR_EQUAL
> What failed: ataport.SYS

`ataport.SYS` is the Windows ATA port driver that handles communication with ATA and SATA storage controllers. An IRQL violation here means the storage driver attempted to access memory at an invalid processor interrupt level.

Common triggers include:

- **Failing hard drive or SSD** — Degraded storage devices causing driver errors
- **Outdated storage driver** — ATA port driver incompatible with Windows version
- **SATA cable issues** — Loose or faulty cables causing I/O errors
- **DMA transfer errors** — Direct memory access failures during disk operations

## Common Causes

1. **Failing storage device** — SSD or HDD with degraded hardware causing driver errors.
2. **Outdated storage driver** — ATA port driver incompatible with Windows updates.
3. **SATA cable issues** — Loose or faulty data cables causing I/O errors.
4. **BIOS settings** — Incorrect SATA operation mode in BIOS.

## How to Fix

### Solution 1: Check Storage Health

```powershell
Get-PhysicalDisk | Select-Object DeviceId, FriendlyName, HealthStatus, OperationalStatus | Format-Table -AutoSize
```

**Check SMART status:**

```powershell
Get-WmiObject -Namespace root\wmi -ClassName MSStorageDriver_FailurePredictStatus | Select-Object InstanceName, PredictFailure
```

If any drive shows degradation, back up data immediately.

### Solution 2: Update Storage Driver

1. Open **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers**.
3. Right-click the ATA controller and select **Update driver**.
4. Choose **Search automatically for drivers**.

### Solution 3: Check SATA Cables

1. Shut down the computer.
2. Reseat SATA data cables on both the motherboard and drive.
3. Try different SATA ports.
4. Replace cables if damaged.

### Solution 4: Run CHKDSK

```cmd
chkdsk C: /f /r
```

Schedule for next restart if prompted.

### Solution 5: Check BIOS SATA Mode

1. Enter BIOS/UEFI during boot.
2. Navigate to **SATA Configuration**.
3. Verify the mode is set correctly (AHCI or IDE) for your setup.
4. Save and exit.

### Solution 6: Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Related Errors

- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA storport.sys]({{< relref "/windows/bsod-page-fault-nonpaged-storport" >}})** — Storage port driver page fault
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Storage driver timeout
- **[BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/windows/bsod-kernel-data-inpage-error" >}})** — Failed disk page read
