---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E storport.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by storport.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "system-thread-exception", "storport", "storage", "stop-0x1000007e"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E storport.sys

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `storport.sys` indicates the Storage Port driver encountered an unhandled exception in a system thread. This is caused by storage driver bugs, RAID controller issues, or hardware storage failures.

## Common Causes

- **Storport driver bug** — The storport.sys driver has a defect in its I/O handling path.
- **RAID controller firmware issue** — Hardware RAID controllers cause storport exceptions.
- **Storage HBA driver conflict** — Host Bus Adapter drivers interact with storport and fail.
- **Failing storage hardware** — Defective drives cause the storport driver to encounter invalid states.

## How to Fix

### Update Storage Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Update RAID Controller Firmware

Download the latest firmware from the storage controller manufacturer.

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

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: storport
IMAGE_NAME:  storport.sys
```

## Related Errors

- [BSOD CRITICAL_PROCESS_DIED storport.sys]({{< relref "/os/windows/bsod-critical-process-died3" >}}) — Storage port critical failure
- [BSOD KERNEL_SECURITY_CHECK_FAILURE storport.sys]({{< relref "/os/windows/bsod-kernel-security-check2" >}}) — Storage port security failure
- [BSOD DPC_WATCHDOG_VIOLATION storport.sys]({{< relref "/os/windows/bsod-dpc-watchdog4" >}}) — Storage DPC timeout
