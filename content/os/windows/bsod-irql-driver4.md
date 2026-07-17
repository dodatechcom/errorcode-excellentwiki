---
title: "[Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xD1 ataport.SYS Windows 11/10"
description: "Fix Blue Screen DRIVER_IRQL_NOT_LESS_OR_EQUAL stop code 0xD1 caused by ataport.SYS ATA port driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xD1 ataport.SYS

The `DRIVER_IRQL_NOT_LESS_OR_EQUAL` stop code `0xD1` with `ataport.SYS` indicates the ATA port driver attempted to access paged memory at an elevated IRQL. This is a storage-related BSOD caused by SATA/IDE controller driver issues.

## Common Causes

- **SATA controller driver bug** — The ataport.SYS driver has a defect in its interrupt handler.
- **Failing SATA drive** — Drive errors cause the ATA port driver to access invalid memory.
- **SATA cable issues** — Loose or damaged SATA cables cause intermittent communication errors.
- **BIOS SATA mode mismatch** — AHCI/IDE mode in BIOS doesn't match the installed driver.

## How to Fix

### Check BIOS SATA Mode

Enter BIOS and verify SATA mode is correct:
- **AHCI** for modern systems
- **IDE** for legacy compatibility
- **RAID** for Intel RST configurations

### Update SATA/AHCI Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Check SATA Cables

Reseat SATA cables and try different ports on the motherboard.

### Check Drive Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Run Check Disk

```cmd
chkdsk C: /f /r
```

### Update BIOS

Download the latest BIOS from the motherboard manufacturer.

## Examples

```text
DRIVER_IRQL_NOT_LESS_OR_EQUAL (d1)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.

MODULE_NAME: ataport
IMAGE_NAME:  ataport.SYS
```

## Related Errors

- [BSOD KERNEL_DATA_INPAGE_ERROR ataport.SYS]({{< relref "/os/windows/bsod-kernel-data-inpage-error2" >}}) — ATA port data error
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-driver-irql" >}}) — NDIS IRQL violation
- [BSOD DPC_WATCHDOG_VIOLATION iaStorA.sys]({{< relref "/os/windows/bsod-dpc-watchdog3" >}}) — Intel RST DPC timeout
