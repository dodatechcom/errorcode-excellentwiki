---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED storport.sys Fix"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED caused by storport.sys on Windows 10 and 11. Resolve storage port driver critical process errors with driver updates and disk diagnostics."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "critical-process", "storport", "storage", "driver"]
weight: 5
---

# [Solution] BSOD CRITICAL_PROCESS_DIED storport.sys Fix

CRITICAL_PROCESS_DIED with `storport.sys` as the failing component is a Blue Screen error caused by the Windows storage port driver crashing as a critical system process. This indicates the storage subsystem encountered an unrecoverable error.

This error commonly occurs during disk-intensive operations, with RAID arrays, or when storage hardware is failing. It can lead to data loss if not addressed promptly.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: CRITICAL_PROCESS_DIED
> What failed: storport.sys

`storport.sys` is the Windows storage port driver that communicates with SATA, NVMe, and RAID storage controllers. When this driver crashes as a critical process, the storage subsystem has failed in a way that prevents Windows from continuing safely.

Common triggers include:

- **Failing SSD or HDD** — Degraded storage hardware causing driver crashes
- **Outdated storage driver** — Storport driver incompatible with current Windows version
- **RAID array issues** — Failed disks in a RAID array
- **SATA/NVMe controller issues** — Hardware failure on the storage controller

## Common Causes

1. **Failing storage device** — SSD or HDD with degraded sectors or firmware issues.
2. **Outdated storage driver** — Storport driver incompatible with Windows updates.
3. **RAID array degradation** — Failed or degraded disks in a RAID array.
4. **Corrupted Windows system files** — Damaged storage-related system files.
5. **SATA/NVMe cable issues** — Loose or faulty data cables.

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

### Solution 2: Run CHKDSK

```cmd
chkdsk C: /f /r
```

Schedule for next restart if prompted. This checks for bad sectors and file system errors.

### Solution 3: Update Storage Controller Driver

```powershell
Get-WmiObject Win32_SCSIController | Select-Object Name, DriverName, DriverVersion, Status | Format-Table -AutoSize
```

1. Open **Device Manager**.
2. Expand **Storage controllers**.
3. Right-click the controller and select **Update driver**.
4. Choose **Search automatically for drivers**.

### Solution 4: Check SATA/NVMe Cables

1. Shut down the computer.
2. Reseat SATA data cables on both the motherboard and drive.
3. Try different SATA ports.
4. For NVMe, reseat the M.2 drive.
5. Replace cables if damaged.

### Solution 5: Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 6: Update BIOS

Check your motherboard manufacturer's website for BIOS updates and install the latest version.

## Related Errors

- **[BSOD CRITICAL_PROCESS_DIED]({{< relref "/windows/bsod-critical-process-died" >}})** — Generic critical process death error
- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA storport.sys]({{< relref "/windows/bsod-page-fault-nonpaged-storport" >}})** — Storage port driver page fault
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Storage driver timeout errors
