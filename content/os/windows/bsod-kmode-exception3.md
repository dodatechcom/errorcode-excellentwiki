---
title: "[Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED — 0x1E tcpip.sys Windows 11/10"
description: "Fix Blue Screen KMODE_EXCEPTION_NOT_HANDLED stop code 0x1E caused by tcpip.sys TCP/IP driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "kmode-exception", "tcpip", "network", "stop-0x1e"]
weight: 5
---

# BSOD KMODE_EXCEPTION_NOT_HANDLED — 0x1E tcpip.sys

The `KMODE_EXCEPTION_NOT_HANDLED` stop code `0x1E` with `tcpip.sys` indicates the TCP/IP network stack driver encountered an unhandled exception in kernel mode. This typically points to network driver corruption or conflict.

## Common Causes

- **Corrupted TCP/IP driver** — The tcpip.sys file is damaged by malware, disk errors, or failed updates.
- **Third-party network software conflict** — Firewalls, VPNs, or network monitoring tools hook into the TCP/IP stack.
- **Winsock catalog corruption** — Damaged Winsock entries cause the TCP/IP stack to crash.
- **Windows network stack bugs** — Known bugs in certain Windows versions affect tcpip.sys.

## How to Fix

### Reset TCP/IP and Winsock

```cmd
netsh int ip reset
netsh winsock reset
ipconfig /flushdns
netsh int ipv4 reset
netsh int ipv6 reset
```

Restart the computer after these commands.

### Restore tcpip.sys from System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Reset Windows Firewall

```cmd
netsh advfirewall reset
```

### Check for Third-Party Network Software

```powershell
Get-Service | Where-Object { $_.DisplayName -like "*firewall*" -or $_.DisplayName -like "*VPN*" -or $_.DisplayName -like "*network monitor*" } | Select-Object Name, DisplayName, Status
```

Stop or uninstall conflicting services.

### Update Network Adapter Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion | Format-Table -AutoSize
```

### Check Network Performance Settings

```cmd
netsh interface tcp show global
```

Ensure chimney offload and other advanced features are compatible with your NIC.

## Examples

```text
KMODE_EXCEPTION_NOT_HANDLED (1e)
An unhandled kernel exception has occurred.

MODULE_NAME: tcpip
IMAGE_NAME:  tcpip.sys
```

## Related Errors

- [BSOD SYSTEM_SERVICE_EXCEPTION tcpip.sys]({{< relref "/os/windows/bsod-system-service-exception4" >}}) — TCP/IP system service exception
- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL netio.sys]({{< relref "/os/windows/bsod-irql-driver2" >}}) — Network I/O IRQL error
- [BSOD KMODE_EXCEPTION_NOT_HANDLED win32kfull.sys]({{< relref "/os/windows/bsod-kmode-exception4" >}}) — Win32k kernel exception
