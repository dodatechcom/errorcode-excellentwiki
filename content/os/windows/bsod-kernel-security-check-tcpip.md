---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE tcpip.sys Fix"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE caused by tcpip.sys on Windows 10 and 11. Resolve TCP/IP driver security check errors with network stack resets."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "kernel-security", "tcpip", "network", "driver"]
weight: 5
---

# [Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE tcpip.sys Fix

KERNEL_SECURITY_CHECK_FAILURE with `tcpip.sys` as the failing driver is a critical Blue Screen caused by a kernel security integrity check violation in the TCP/IP networking stack. This error indicates that a kernel-mode driver has corrupted critical data structures.

This BSOD commonly occurs during heavy network activity, with VPN connections, or when third-party security software hooks into the network stack.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: KERNEL_SECURITY_CHECK_FAILURE
> What failed: tcpip.sys

The kernel security check verifies the integrity of critical kernel data structures. When tcpip.sys triggers this check, it means the network stack has corrupted a kernel structure, possibly due to a bug, memory corruption, or a security policy violation.

Common triggers include:

- **Third-party firewall with network inspection** — Modifying TCP/IP data structures
- **VPN client software** — VPN drivers altering kernel network structures
- **Malware** — Network-based malware corrupting kernel structures
- **Corrupted Windows updates** — Bad updates damaging TCP/IP driver files

## Common Causes

1. **Third-party security software** — Firewalls or antivirus that inspect network traffic at kernel level.
2. **VPN client drivers** — VPN software modifying TCP/IP stack behavior.
3. **Corrupted TCP/IP driver files** — Damaged tcpip.sys from Windows updates.
4. **Malware** — Kernel-mode malware corrupting network data structures.

## How to Fix

### Solution 1: Reset Network Stack

```cmd
netsh winsock reset
netsh int ip reset
ipconfig /flushdns
```

Restart your computer after running these commands.

### Solution 2: Remove Third-Party Security Software

1. Open **Settings > Apps > Installed apps**.
2. Uninstall third-party antivirus or firewall.
3. Restart your computer.

### Solution 3: Remove VPN Client Software

1. Uninstall all VPN clients from **Settings > Apps**.
2. Restart your computer.
3. Reinstall from the official source.

### Solution 4: Repair Windows System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 5: Scan for Malware

```powershell
Start-MpScan -ScanType FullScan
Start-MpScan -ScanType OfflineScan
```

### Solution 6: Update Network Adapter Driver

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion | Format-Table -AutoSize
```

Download the latest driver from the adapter manufacturer's website.

## Related Errors

- **[BSOD KERNEL_SECURITY_CHECK_FAILURE ndis.sys]({{< relref "/windows/bsod-kernel-security-check-ndis" >}})** — NDIS security check failure
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/windows/bsod-kmode-exception-not-handled-tcpip" >}})** — TCP/IP kernel exception
- **[BSOD KERNEL_SECURITY_CHECK_FAILURE]({{< relref "/windows/bsod-kernel-security-check-failure" >}})** — Generic kernel security check error
