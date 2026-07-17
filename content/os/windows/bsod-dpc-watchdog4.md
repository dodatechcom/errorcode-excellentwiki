---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION — 0x133 storport.sys Windows 11/10"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION stop code 0x133 caused by storport.sys storage port driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD DPC_WATCHDOG_VIOLATION — 0x133 storport.sys

The `DPC_WATCHDOG_VIOLATION` stop code `0x133` with `storport.sys` indicates the Storage Port driver took too long to complete a Deferred Procedure Call. The DPC watchdog timer expired waiting for the storport driver to finish its storage I/O operations.

## Common Causes

- **Storage controller driver hang** — The storport driver enters an infinite loop or deadlock during I/O.
- **Failing storage device** — A failing drive causes the storage port driver to wait indefinitely.
- **RAID array degradation** — A degraded RAID array causes slow or hung storage operations.
- **SATA/NVMe link issues** — Physical connection problems cause storage timeouts.

## How to Fix

### Update Storage Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

### Run Check Disk

```cmd
chkdsk C: /f /r
```

### Check SATA/NVMe Connections

Reseat SATA cables and try different ports. For NVMe drives, try a different M.2 slot.

### Update BIOS

Download the latest BIOS from the motherboard manufacturer.

### Disable StorPort Power Management

```powershell
powercfg /setacvalueindex SCHEME_CURRENT SUB_DISK NVMeNOP 0
powercfg /setactive SCHEME_CURRENT
```

### Check Event Viewer

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*storport*" -or $_.ProviderName -like "*disk*" } | Select-Object -First 10 TimeCreated, Id, Message | Format-Table -Wrap
```

## Examples

```text
DPC_WATCHDOG_VIOLATION (133)
A DPC did not complete in a timely manner.

MODULE_NAME: storport
IMAGE_NAME:  storport.sys
```

## Related Errors

- [BSOD DPC_WATCHDOG_VIOLATION stornvme.sys]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — NVMe DPC timeout
- [BSOD DPC_WATCHDOG_VIOLATION iaStorA.sys]({{< relref "/os/windows/bsod-dpc-watchdog3" >}}) — Intel RST DPC timeout
- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — Disk read failure
