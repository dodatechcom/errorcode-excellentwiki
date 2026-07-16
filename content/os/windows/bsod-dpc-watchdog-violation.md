---
title: "[Solution] BSOD DPC Watchdog Violation Windows 11/10 — Fixed"
description: "Fix Blue Screen DPC Watchdog Violation error on Windows 10 and 11. Update your storage drivers and fix SSD firmware issues with these proven solutions."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
tags: ["bsod", "blue-screen", "dpc-watchdog", "drivers", "ssd"]
weight: 50
---

# [Solution] BSOD DPC Watchdog Violation Windows 11/10 — Fixed

The DPC Watchdog Violation is one of the most common Blue Screen of Death errors on Windows 10 and 11. It appears as a stop code `DPC_WATCHDOG_VIOLATION` and causes an immediate system crash with a blue screen.

This error typically strikes during normal use — browsing the web, watching videos, or working in applications. It can occur randomly or repeatedly, and is often linked to storage driver issues, SSD firmware problems, or incompatible hardware.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: DPC_WATCHDOG_VIOLATION

The DPC (Deferred Procedure Call) Watchdog monitors the execution of deferred procedure calls and detects when a call takes too long to complete. When a DPC exceeds the watchdog timeout (typically 10 seconds), Windows triggers a bug check and crashes to prevent data corruption.

The error commonly appears in these scenarios:

- **After installing a new SSD or NVMe drive** — The drive's firmware or driver is incompatible
- **Following a Windows update** — A new driver conflicts with existing hardware
- **During heavy disk I/O** — Large file transfers, backups, or database operations
- **With specific SSD models** — Particularly older SATA SSDs and certain NVMe drives
- **After connecting external storage** — USB drives or external hard drives triggering the violation

## Common Causes

1. **Outdated or corrupted storage drivers** — The AHCI, NVMe, or SATA controller drivers are outdated or incompatible with your hardware.
2. **SSD firmware issues** — The solid-state drive's firmware has bugs that trigger timeouts.
3. **AHCI power management** — Link State Power Management puts the drive in a low-power state that it can't recover from quickly enough.
4. **Outdated BIOS/UEFI** — The motherboard firmware doesn't properly communicate with modern storage devices.
5. **Faulty storage hardware** — A failing drive causes intermittent timeouts.
6. **Incompatible RAM** — Memory timing conflicts can cause DPC timeouts indirectly.
7. **Third-party disk management tools** — Software like disk encryption or RAID managers interfering with storage access.

## Solutions

### Solution 1: Update Storage Drivers

The most common fix is updating the storage controller driver. Outdated AHCI or NVMe drivers are the leading cause of this BSOD.

**Using Device Manager:**

1. Right-click the **Start** button and select **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers** or **Storage controllers**.
3. Right-click your storage controller (usually "Standard SATA AHCI Controller" or "Intel(R) Chipset SATA/PCIe RST Premium Controller").
4. Select **Update driver**.
5. Choose **Search automatically for drivers**.
6. If Windows doesn't find a newer driver, visit your motherboard manufacturer's website.

**Using PowerShell to check current driver version:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC"} | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

For Intel systems, install the Intel Rapid Storage Technology (IRST) driver:

1. Go to [Intel's download center](https://www.intel.com/content/www/us/en/download-center/home.html).
2. Search for **Intel Rapid Storage Technology**.
3. Download and install the latest version for your system.
4. Restart your computer.

For AMD systems, install the AMD StoreMI or SATA driver from your motherboard manufacturer's support page.

### Solution 2: Check and Update SSD Firmware

SSD firmware bugs are a frequent cause of DPC Watchdog Violation. Check and update your SSD's firmware:

**Identify your SSD model:**

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, Size | Format-Table -AutoSize
```

**Check current firmware version:**

```powershell
Get-WmiObject -Namespace root\wmi -Class MSStorageDriver_FirmwareVersionModel | Select-Object InstanceName, FirmwareVersion | Format-Table -AutoSize
```

Visit your SSD manufacturer's website to check for firmware updates:

- **Samsung**: Samsung Magician software
- **Western Digital**: WD Dashboard
- **Crucial**: Crucial Storage Executive
- **Intel**: Intel Memory and Storage Tool
- **Kingston**: Kingston SSD Manager

Download the manufacturer's tool, check your current firmware version against the latest available, and apply any updates. **Do not turn off your computer during a firmware update** — this can permanently brick the drive.

### Solution 3: Disable AHCI Power Management

The SATA power management feature can cause DPC timeouts by putting drives into deep sleep states. Disabling it often resolves the error:

**Using Device Manager:**

1. Open **Device Manager**.
2. Expand **IDE ATA/ATAPI controllers**.
3. Right-click your AHCI controller and select **Properties**.
4. Go to the **Policies** or **Power Management** tab.
5. Uncheck **Allow the computer to turn off this device to save power**.
6. Click **OK**.

**Using PowerShell to disable aggressive power management:**

```powershell
powercfg /setacvalueindex SCHEME_CURRENT SUB_DISK AHCIHIPM 0
powercfg /setactive SCHEME_CURRENT
```

**Disable Hibernate to prevent deep sleep states:**

```cmd
powercfg -h off
```

**Set the balanced power plan to high performance:**

```cmd
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```

### Solution 4: Run Hardware Diagnostics

If driver and firmware updates don't fix the issue, run hardware diagnostics to check for failing components.

**Run Windows Memory Diagnostic:**

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Windows will test your RAM during the reboot process. Results appear in the Event Viewer under **Windows Logs > System** with source `MemoryDiagnostics-Results`.

**Run CHKDSK to check for disk errors:**

```cmd
chkdsk C: /f /r
```

Press `Y` to schedule the check for the next restart, then reboot your computer.

**Check SMART status of your drives:**

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal | Format-Table -AutoSize
```

A high Wear value (above 90%) or any ReadErrorsTotal/WriteErrorsTotal greater than 0 indicates a failing drive.

### Solution 5: Update BIOS/UEFI

An outdated BIOS can cause communication issues between the operating system and storage hardware.

1. Identify your motherboard model:

```cmd
wmic baseboard get product,Manufacturer,version
```

2. Visit your motherboard manufacturer's website (ASUS, MSI, Gigabyte, ASRock, Dell, HP, etc.).
3. Find the support page for your exact model.
4. Download the latest BIOS update.
5. Follow the manufacturer's instructions for flashing the BIOS carefully.

**Warning**: Do not interrupt a BIOS update. Ensure your computer is plugged into a reliable power source throughout the process.

### Solution 6: Check for Faulty RAM

Memory issues can indirectly trigger DPC Watchdog Violation by causing timing conflicts in the storage subsystem.

**Run MemTest86:**

1. Download MemTest86 from [memtest86.com](https://www.memtest86.com/).
2. Create a bootable USB drive using the provided tool.
3. Boot from the USB drive.
4. Let the test run for at least 4 passes.
5. Look for any errors in the results.

If errors are found, try reseating the RAM modules. If errors persist, the RAM module is likely faulty and should be replaced.

### Solution 7: Disable Overclocking

Overclocking CPU, RAM, or storage controllers can cause timing violations:

1. Enter BIOS/UEFI setup (press `Del`, `F2`, or `F12` during boot).
2. Load **Optimized Defaults** or **Fail-Safe Defaults**.
3. Save and exit.

In Windows, if you're using software-based overclocking:

1. Open the overclocking software (MSI Afterburner, Intel XTU, Ryzen Master, etc.).
2. Click **Reset to defaults** or **Return to stock settings**.
3. Apply changes and restart your computer.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL](/os/windows/bsod-irql-not-less-or-equal.md)** — Another common BSOD caused by driver conflicts and memory issues
- **Error 0x0000007E** — System thread exception not handled, often caused by the same driver issues
- **Error 0x00000050** — Page fault in nonpaged area, related to memory and storage problems
- **Error 0x000000F4** — Critical object termination, can be triggered by failing storage drives
- **Error 0x000000EF** — Critical process died, another watchdog-related BSOD
