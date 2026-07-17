---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION — 0x133 iaStorA.sys Windows 11/10"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION stop code 0x133 caused by iaStorA.sys Intel Rapid Storage Technology on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD DPC_WATCHDOG_VIOLATION — 0x133 iaStorA.sys

The `DPC_WATCHDOG_VIOLATION` stop code `0x133` with `iaStorA.sys` indicates the Intel Rapid Storage Technology (IRST) driver took too long to complete a Deferred Procedure Call, triggering the DPC watchdog timer. This is a common storage-related BSOD on Intel-based systems.

## Common Causes

- **Outdated Intel RST driver** — The iaStorA.sys driver has known bugs causing DPC timeouts.
- **AHCI/NVMe mode mismatch** — BIOS is set to AHCI but the IRST driver expects RAID mode, or vice versa.
- **Failing SSD or HDD** — Storage device errors cause the driver to hang during I/O operations.
- **SATA cable or port issues** — Physical connection problems cause intermittent storage timeouts.

## How to Fix

### Update Intel RST Driver

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceName -like "*Intel*Rapid*" -or $_.DeviceName -like "*IRST*" } | Select-Object DeviceName, DriverVersion, DriverDate
```

Download the latest Intel RST driver from [intel.com/content/www/us/en/download](https://www.intel.com/content/www/us/en/download-center/home.html).

### Check BIOS SATA Mode

Enter BIOS and ensure the SATA mode matches the driver:
- If using **IRST/RAID**: Set SATA mode to **RAID** or **Intel RST Premium**
- If not using RAID: Set SATA mode to **AHCI** and install the standard AHCI driver

### Replace iaStorA with StorNVMe or Standard AHCI

```powershell
# Check which storage drivers are loaded
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC" } | Select-Object DeviceName, DriverVersion | Format-Table -AutoSize
```

If not using Intel RAID, uninstall IRST and let Windows use the standard AHCI driver.

### Check Storage Device Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

Replace failing drives.

### Update BIOS

Download and install the latest BIOS from your motherboard or laptop manufacturer.

### Check SATA Cables

Reseat SATA cables and try different SATA ports on the motherboard.

## Examples

```text
DPC_WATCHDOG_VIOLATION (133)
A DPC did not complete in a timely manner.

MODULE_NAME: iaStorA
IMAGE_NAME:  iaStorA.sys
```

## Related Errors

- [BSOD DPC_WATCHDOG_VIOLATION stornvme.sys]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — NVMe DPC watchdog
- [BSOD DPC_WATCHDOG_VIOLATION storport.sys]({{< relref "/os/windows/bsod-dpc-watchdog4" >}}) — Storage port DPC timeout
- [BSOD CRITICAL_PROCESS_DIED]({{< relref "/os/windows/bsod-critical-process-died" >}}) — Critical process terminated
