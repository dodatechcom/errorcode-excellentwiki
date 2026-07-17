---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E ndis.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by ndis.sys network driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E ndis.sys

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `ndis.sys` indicates the Network Driver Interface Specification driver encountered an unhandled exception in a system thread. This is caused by network driver bugs, corrupted NDIS structures, or VPN filter driver conflicts.

## Common Causes

- **Corrupted NDIS driver** — The ndis.sys file is damaged by disk errors or failed updates.
- **Network adapter driver conflict** — NIC drivers interact with NDIS and cause exceptions.
- **VPN filter driver bug** — VPN software installs NDIS filters that cause exceptions.
- **Third-party firewall interfering with NDIS** — Firewall software hooks into the network stack.

## How to Fix

### Update Network Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest driver from the NIC manufacturer's website.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Remove VPN and Network Filters

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

Disable or uninstall VPN clients and third-party network filter drivers.

### Reset Network Stack

```cmd
netsh int ip reset
netsh winsock reset
ipconfig /flushdns
```

### Check NDIS Driver Version

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceName -like "*NDIS*" } | Select-Object DeviceName, DriverVersion, DriverDate
```

### Boot into Safe Mode to Test

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: ndis
IMAGE_NAME:  ndis.sys
```

## Related Errors

- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-driver-irql" >}}) — NDIS IRQL violation
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL netio.sys]({{< relref "/os/windows/bsod-irql-driver2" >}}) — Network I/O IRQL error
- [BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED ndis.sys]({{< relref "/os/windows/bsod-system-thread-exception9" >}}) — Another NDIS variant
