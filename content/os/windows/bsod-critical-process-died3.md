---
title: "[Solution] BSOD CRITICAL_PROCESS_DIED — 0xEF storport.sys Windows 11/10"
description: "Fix Blue Screen CRITICAL_PROCESS_DIED stop code 0xEF caused by storport.sys storage port driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD CRITICAL_PROCESS_DIED — 0xEF storport.sys

The `CRITICAL_PROCESS_DIED` stop code `0xEF` with `storport.sys` indicates the Windows Storage Port driver caused a critical system process to terminate. The storport driver manages communication between the OS and storage controllers, and its failure prevents the system from accessing disk.

## Common Causes

- **Storport driver bug** — The storport.sys driver has a known issue with certain storage controllers.
- **RAID controller failure** — Hardware RAID controllers using storport encounter firmware bugs.
- **Storage HBA driver conflict** — Host Bus Adapter drivers interact with storport and cause failures.
- **Failing storage controller** — Physical storage hardware issues cause the port driver to hang.

## How to Fix

### Update Storage Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest storage driver from the motherboard or storage controller manufacturer.

### Check Disk Health

```powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Health, Wear
```

### Run Check Disk

```cmd
chkdsk C: /f /r
```

### Update BIOS

Download and install the latest BIOS from the motherboard manufacturer.

### Check Event Viewer for Storage Errors

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*storport*" -or $_.ProviderName -like "*disk*" } | Select-Object -First 10 TimeCreated, Id, Message | Format-Table -Wrap
```

### Disable StorPort Power Management

```powershell
# Disable aggressive link power management
powercfg /setacvalueindex SCHEME_CURRENT SUB_DISK NVMeNOP 0
powercfg /setactive SCHEME_CURRENT
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

## Examples

```text
CRITICAL_PROCESS_DIED (ef)
A critical system process terminated unexpectedly.

MODULE_NAME: storport
IMAGE_NAME:  storport.sys
```

## Related Errors

- [BSOD CRITICAL_PROCESS_DIED ci.dll]({{< relref "/os/windows/bsod-critical-process-died4" >}}) — Code Integrity failure
- [BSOD CRITICAL_PROCESS_DIED ntoskrnl.exe]({{< relref "/os/windows/bsod-critical-process-died6" >}}) — Kernel critical process
- [BSOD KERNEL_DATA_INPAGE_ERROR]({{< relref "/os/windows/bsod-kernel-data-inpage-error" >}}) — Disk read failure
