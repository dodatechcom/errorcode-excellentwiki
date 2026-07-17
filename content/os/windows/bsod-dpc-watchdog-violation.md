---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION — 0x133 stornvme.sys Windows 11/10"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION stop code 0x133 caused by stornvme.sys NVMe driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD DPC_WATCHDOG_VIOLATION — 0x133 stornvme.sys

The `DPC_WATCHDOG_VIOLATION` stop code `0x133` with `stornvme.sys` indicates the Standard NVM Express driver took too long to complete a Deferred Procedure Call. This is a storage-related BSOD common on systems with NVMe SSDs.

## Common Causes

- **NVMe SSD firmware bug** — The SSD controller has firmware that causes DPC timeouts.
- **Outdated stornvme driver** — The standard NVMe driver has compatibility issues with certain SSDs.
- **Failing NVMe SSD** — Hardware failure causes the drive to become unresponsive.
- **Power management conflicts** — NVMe power states cause the drive to not wake in time.
- **M.2 slot thermal throttling** — NVMe drives overheat and throttle, causing DPC timeouts.

## How to Fix

### Update NVMe Firmware

Check the SSD manufacturer's website for firmware updates:
- Samsung: Samsung Magician
- Western Digital: WD Dashboard
- Crucial: Crucial Storage Executive

### Disable NVMe Power Management

```powershell
# Disable NVMe autonomous power state transitions
powercfg /setacvalueindex SCHEME_CURRENT SUB_DISK NVMeNOP 0
powercfg /setactive SCHEME_CURRENT
```

### Update stornvme Driver

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceName -like "*NVMe*" -or $_.DeviceName -like "*stornvme*" } | Select-Object DeviceName, DriverVersion, DriverDate
```

Download the latest driver from the SSD manufacturer or motherboard manufacturer.

### Monitor SSD Temperature

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health
```

Add heatsinks to M.2 NVMe drives if they exceed 70°C.

### Check for Bad Sectors

```cmd
chkdsk C: /f /r
```

### Check M.2 Slot Compatibility

Ensure the M.2 slot supports the NVMe generation of your SSD. Some M.2 slots only support SATA.

## Examples

```text
DPC_WATCHDOG_VIOLATION (133)
A DPC did not complete in a timely manner.

MODULE_NAME: stornvme
IMAGE_NAME:  stornvme.sys
```

## Related Errors

- [BSOD DPC_WATCHDOG_VIOLATION iaStorA.sys]({{< relref "/os/windows/bsod-dpc-watchdog3" >}}) — Intel RST DPC timeout
- [BSOD DPC_WATCHDOG_VIOLATION storport.sys]({{< relref "/os/windows/bsod-dpc-watchdog4" >}}) — Storage port DPC timeout
- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — Disk read failure
