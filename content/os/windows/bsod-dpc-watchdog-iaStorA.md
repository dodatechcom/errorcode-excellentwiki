---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION iaStorA.sys Intel RST Fix"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION caused by iaStorA.sys on Windows 10 and 11. Resolve Intel Rapid Storage Technology driver timeouts with driver updates and BIOS fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD DPC_WATCHDOG_VIOLATION iaStorA.sys Intel RST Fix

DPC_WATCHDOG_VIOLATION with `iaStorA.sys` is a Blue Screen error caused by the Intel Rapid Storage Technology (RST) driver taking too long to complete a deferred procedure call. The watchdog timer detects the hang and crashes the system to prevent data corruption.

This error is extremely common on laptops and desktops with Intel chipsets, especially after Windows updates or when the Intel RST driver is outdated.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: DPC_WATCHDOG_VIOLATION
> What failed: iaStorA.sys

`iaStorA.sys` is the Intel Rapid Storage Technology (RST) driver that manages SATA and NVMe storage controllers on Intel platforms. A DPC watchdog violation means this driver held a processor core for too long without yielding, causing the system watchdog to trigger a crash.

Common triggers include:

- **Outdated Intel RST driver** — Driver incompatibility with Windows updates
- **SATA/NVMe mode mismatch** — BIOS set to RAID mode without proper driver
- **Failing storage device** — SSD or HDD causing the storage driver to hang
- **BIOS settings** — Incorrect SATA operation mode in BIOS

## Common Causes

1. **Outdated Intel RST driver** — The most common cause; the driver is not updated for the current Windows version.
2. **BIOS SATA mode mismatch** — BIOS set to RAID mode but using AHCI driver, or vice versa.
3. **Failing SSD or HDD** — Degraded storage devices cause the driver to hang.
4. **BIOS needs update** — Outdated BIOS causes storage controller issues.

## How to Fix

### Solution 1: Update Intel RST Driver

**Check current version:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceName -like "*Intel*Storage*" -or $_.InfName -like "*iastor*" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest Intel RST driver from [intel.com/support](https://www.intel.com/content/www/us/en/support.html):

1. Enter your chipset model or let the Intel Driver Support Assistant detect it.
2. Download and install the recommended RST driver.
3. Restart your computer.

### Solution 2: Check BIOS SATA Mode

1. Restart and enter **BIOS/UEFI** (usually `Del` or `F2` during boot).
2. Navigate to **Advanced > SATA Configuration** or **Storage Configuration**.
3. Verify the SATA mode matches the driver:
   - If using **Intel RST (RAID)**, set mode to **RAID** or **Intel RST Premium**.
   - If not using RAID, set mode to **AHCI**.
4. Save and exit.

**Warning**: Changing SATA mode after Windows installation can prevent booting. Only change if you are prepared to reinstall Windows or modify the registry first.

### Solution 3: Switch from RST to AHCI (Without Reinstalling)

If you want to switch from RAID to AHCI without reinstalling Windows:

1. Open **Command Prompt as Administrator**.
2. Run:
   ```cmd
   bcdedit /set {current} safeboot minimal
   ```
3. Restart and enter BIOS.
4. Change SATA mode from **RAID** to **AHCI**.
5. Boot into Safe Mode (Windows will install the standard AHCI driver).
6. Open **Command Prompt as Administrator** and run:
   ```cmd
   bcdedit /deletevalue {current} safeboot
   ```
7. Restart normally.

### Solution 4: Update BIOS

1. Check your motherboard or laptop manufacturer's website for BIOS updates.
2. Download and install the latest BIOS version.
3. Restart your computer.

### Solution 5: Check Storage Health

```powershell
Get-PhysicalDisk | Select-Object DeviceId, FriendlyName, HealthStatus, OperationalStatus | Format-Table -AutoSize
```

If any drive shows **Warning** or **Failed**, back up data immediately and replace the drive.

### Solution 6: Run System File Checker

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Related Errors

- **[BSOD DPC_WATCHDOG_VIOLATION storahci.sys]({{< relref "/windows/bsod-dpc-watchdog-storahci" >}})** — Standard AHCI driver version of this error
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Generic DPC watchdog error
- **[BSOD PAGE_FAULT_IN_NONPAGED_AREA storport.sys]({{< relref "/windows/bsod-page-fault-nonpaged-storport" >}})** — Storage port driver page fault
