---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION Windows 11/10 — Fixed"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION error on Windows 10 and 11. Update storage drivers, check SSD firmware, and disable AHCI power management to resolve this stop code."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD DPC_WATCHDOG_VIOLATION Windows 11/10 — Fixed

DPC_WATCHDOG_VIOLATION is a critical Blue Screen of Death error with stop code `0x00000133`. It occurs when the Windows DPC (Deferred Procedure Call) watchdog detects that a deferred procedure call has exceeded its timeout — typically 10 seconds. The system crashes to prevent data corruption when a driver takes too long to complete its work.

This BSOD affects both Windows 10 and 11 and is most commonly caused by storage driver issues, SSD firmware problems, or incompatible hardware. It often strikes during normal use — browsing, watching videos, or performing file operations.

## Common Causes

- **Outdated or corrupted storage drivers** — AHCI, NVMe, or SATA controller drivers are outdated or incompatible.
- **SSD firmware issues** — The solid-state drive's firmware has bugs that trigger timeouts during I/O operations.
- **AHCI power management** — Link State Power Management puts the drive into a low-power state it cannot recover from quickly enough.
- **Faulty storage hardware** — A failing drive causes intermittent timeouts.

## How to Fix

### Update Storage Drivers

The most common fix is updating the storage controller driver.

**Check current storage driver version:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC"} | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

**Update via Device Manager:**

1. Right-click the **Start** button and select **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers** or **Storage controllers**.
3. Right-click your storage controller and select **Update driver**.
4. Choose **Search automatically for drivers**.

For Intel systems, install the Intel Rapid Storage Technology (IRST) driver from [Intel's download center](https://www.intel.com/content/www/us/en/download-center/home.html). For AMD systems, install the AMD StoreMI or SATA driver from your motherboard manufacturer.

### Check and Update SSD Firmware

**Identify your SSD model:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size | Format-Table -AutoSize
```

**Check current firmware version:**

```powershell
Get-WmiObject -Namespace root\wmi -Class MSStorageDriver_FirmwareVersionModel | Select-Object InstanceName, FirmwareVersion | Format-Table -AutoSize
```

Visit your SSD manufacturer's website for firmware updates:
- **Samsung**: Samsung Magician software
- **Western Digital**: WD Dashboard
- **Crucial**: Crucial Storage Executive
- **Intel**: Intel Memory and Storage Tool
- **Kingston**: Kingston SSD Manager

**Do not turn off your computer during a firmware update.**

### Disable AHCI Power Management

SATA power management can cause DPC timeouts by putting drives into deep sleep states.

**Disable via PowerShell:**

```powershell
powercfg /setacvalueindex SCHEME_CURRENT SUB_DISK AHCIHIPM 0
powercfg /setactive SCHEME_CURRENT
```

**Disable Hibernate to prevent deep sleep states:**

```cmd
powercfg -h off
```

**Set high performance power plan:**

```cmd
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```

### Check for Disk Errors

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule the check for the next restart, then reboot.

**Check SMART status:**

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal | Format-Table -AutoSize
```

A high Wear value (above 90%) or any errors greater than 0 indicates a failing drive.

### Update BIOS/UEFI

```cmd
wmic baseboard get product,Manufacturer,version
```

Visit your motherboard manufacturer's website and download the latest BIOS update. Ensure uninterrupted power during the update process.

### Test RAM

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 from a bootable USB for at least 4 passes. Memory issues can indirectly trigger DPC timeouts through timing conflicts in the storage subsystem.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples

This error commonly occurs in these scenarios:

- **After installing a new SSD** — The drive's firmware or driver is incompatible with the system.
- **During heavy disk I/O** — Large file transfers, backups, or database operations expose driver timeouts.
- **Following a Windows update** — A new driver conflicts with existing storage hardware.
- **With older SATA SSDs** — Certain SSD models have firmware bugs that trigger DPC violations.

## Related Errors

- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — Another common BSOD caused by driver conflicts
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault" >}}) — Related to memory and storage problems
- [BSOD CRITICAL_PROCESS_DIED]({{< relref "/os/windows/bsod-critical-process-died" >}}) — Another watchdog-related BSOD
- [BSOD SYSTEM_SERVICE_EXCEPTION]({{< relref "/os/windows/bsod-system-service-exception" >}}) — System service failure from driver issues
