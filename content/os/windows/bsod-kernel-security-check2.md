---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 storport.sys Windows 11/10"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE stop code 0x139 caused by storport.sys storage driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "kernel-security", "storport", "storage", "stop-0x139"]
weight: 5
---

# BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 storport.sys

The `KERNEL_SECURITY_CHECK_FAILURE` stop code `0x139` with `storport.sys` indicates the Storage Port driver corrupted a critical kernel data structure. The kernel's security integrity check detected damage in a structure managed by the storage subsystem.

## Common Causes

- **Storport driver bug** — The storport.sys driver has a defect that corrupts kernel data.
- **Storage controller firmware issue** — RAID or HBA firmware causes the storport driver to corrupt memory.
- **SCSI/SAS driver conflict** — Enterprise storage drivers interact with storport and cause corruption.
- **Failing storage hardware** — Defective storage controllers cause the driver to enter invalid states.

## How to Fix

### Update Storage Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Update Storage Controller Firmware

Download the latest firmware from the storage controller manufacturer (LSI/Broadcom, Adaptec, etc.).

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Update BIOS

Download the latest BIOS from the motherboard manufacturer.

### Check Event Viewer for Storage Errors

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*storport*" } | Select-Object -First 10 TimeCreated, Id, Message | Format-Table -Wrap
```

## Examples

```text
KERNEL_SECURITY_CHECK_FAILURE (139)
A kernel security check failure has occurred.

MODULE_NAME: storport
IMAGE_NAME:  storport.sys
```

## Related Errors

- [BSOD KERNEL_SECURITY_CHECK_FAILURE tcpip.sys]({{< relref "/os/windows/bsod-kernel-security-check-failure" >}}) — TCP/IP kernel security
- [BSOD KERNEL_SECURITY_CHECK_FAILURE CI.dll]({{< relref "/os/windows/bsod-kernel-security-check5" >}}) — Code Integrity failure
- [BSOD CRITICAL_PROCESS_DIED storport.sys]({{< relref "/os/windows/bsod-critical-process-died3" >}}) — Storage port critical failure
