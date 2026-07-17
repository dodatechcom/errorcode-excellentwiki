---
title: "[Solution] BSOD SYSTEM_SERVICE_EXCEPTION — 0x3B tcpip.sys Windows 11/10"
description: "Fix Blue Screen SYSTEM_SERVICE_EXCEPTION stop code 0x3B caused by tcpip.sys TCP/IP driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD SYSTEM_SERVICE_EXCEPTION — 0x3B tcpip.sys

The `SYSTEM_SERVICE_EXCEPTION` stop code `0x3B` with `tcpip.sys` indicates the TCP/IP network stack driver threw an unhandled exception during a system service call. This is commonly caused by network driver bugs, VPN filter conflicts, or corrupted network stack components.

## Common Causes

- **TCP/IP driver corruption** — The tcpip.sys file is damaged by disk errors or failed updates.
- **VPN filter driver conflict** — VPN software installs network filters that cause TCP/IP exceptions.
- **Network adapter driver bug** — NIC drivers interact with tcpip.sys and cause service exceptions.
- **Winsock catalog corruption** — Damaged Winsock entries cause TCP/IP to fail during system calls.

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

### Disable Third-Party Firewalls

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

### Reset Windows Firewall

```cmd
netsh advfirewall reset
```

## Examples

```text
SYSTEM_SERVICE_EXCEPTION (3b)
An exception happened while executing a system service routine.

MODULE_NAME: tcpip
IMAGE_NAME:  tcpip.sys
```

## Related Errors

- [BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/os/windows/bsod-kmode-exception3" >}}) — TCP/IP kernel exception
- [BSOD SYSTEM_SERVICE_EXCEPTION win32kfull.sys]({{< relref "/os/windows/bsod-system-service-exception3" >}}) — Win32k service exception
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL netio.sys]({{< relref "/os/windows/bsod-irql-driver2" >}}) — Network I/O IRQL
