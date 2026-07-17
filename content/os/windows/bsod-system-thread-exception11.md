---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E tcpip.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED stop code 0x1000007E caused by tcpip.sys on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED — 0x1000007E tcpip.sys

The `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` stop code `0x1000007E` with `tcpip.sys` indicates the TCP/IP network stack driver encountered an unhandled exception in a system thread. This is caused by network driver corruption, VPN filter conflicts, or TCP/IP stack bugs.

## Common Causes

- **Corrupted TCP/IP driver** — The tcpip.sys file is damaged by disk errors or failed updates.
- **VPN filter driver conflict** — VPN software NDIS filters cause TCP/IP exceptions.
- **Network adapter driver bug** — NIC drivers interact with TCP/IP and cause system thread exceptions.
- **Winsock catalog corruption** — Damaged Winsock entries cause TCP/IP to fail.

## How to Fix

### Reset TCP/IP and Winsock

```cmd
netsh int ip reset
netsh winsock reset
ipconfig /flushdns
```

Restart after these commands.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Update Network Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Uninstall VPN Software

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*VPN*" } | Select-Object Name, Version
```

### Check for Network Filter Drivers

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

### Boot into Safe Mode

```cmd
bcdedit /set {current} safeboot minimal
shutdown /r /t 0
```

## Examples

```text
SYSTEM_THREAD_EXCEPTION_NOT_HANDLED (7e)
An exception that was not handled in a system thread.

MODULE_NAME: tcpip
IMAGE_NAME:  tcpip.sys
```

## Related Errors

- [BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/os/windows/bsod-kmode-exception3" >}}) — TCP/IP kernel exception
- [BSOD SYSTEM_SERVICE_EXCEPTION tcpip.sys]({{< relref "/os/windows/bsod-system-service-exception4" >}}) — TCP/IP service exception
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL netio.sys]({{< relref "/os/windows/bsod-irql-driver2" >}}) — Network I/O IRQL
