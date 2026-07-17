---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 tcpip.sys Windows 11/10"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE stop code 0x139 caused by tcpip.sys TCP/IP driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
weight: 5
---

# BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 tcpip.sys

The `KERNEL_SECURITY_CHECK_FAILURE` stop code `0x139` with `tcpip.sys` indicates the Windows TCP/IP network stack corrupted a critical kernel data structure. The kernel's security integrity check detected that a linked list or structure managed by the TCP/IP driver has been damaged.

## Common Causes

- **Corrupted TCP/IP driver** — The tcpip.sys file is damaged by disk errors or failed updates.
- **Third-party network filter driver** — VPN or firewall software corrupts TCP/IP data structures.
- **Winsock catalog corruption** — Damaged Winsock entries cause TCP/IP kernel structures to fail.
- **Network adapter driver conflict** — NIC drivers interact with tcpip.sys and cause corruption.

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

### Uninstall VPN and Firewall Software

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*VPN*" -or $_.Name -like "*firewall*" } | Select-Object Name, Version
```

### Update Network Adapter Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Reset Windows Firewall

```cmd
netsh advfirewall reset
```

### Disable Network Filter Drivers

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

## Examples

```text
KERNEL_SECURITY_CHECK_FAILURE (139)
A kernel security check failure has occurred.

MODULE_NAME: tcpip
IMAGE_NAME:  tcpip.sys
```

## Related Errors

- [BSOD KERNEL_SECURITY_CHECK_FAILURE storport.sys]({{< relref "/os/windows/bsod-kernel-security-check2" >}}) — Storage port kernel security
- [BSOD KERNEL_SECURITY_CHECK_FAILURE win32kfull.sys]({{< relref "/os/windows/bsod-kernel-security-check3" >}}) — Win32k kernel security
- [BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/os/windows/bsod-kmode-exception3" >}}) — TCP/IP kernel exception
