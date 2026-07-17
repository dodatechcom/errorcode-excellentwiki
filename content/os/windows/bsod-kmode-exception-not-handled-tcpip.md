---
title: "[Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys Fix"
description: "Fix Blue Screen KMODE_EXCEPTION_NOT_HANDLED caused by tcpip.sys on Windows 10 and 11. Resolve TCP/IP kernel exceptions with network stack resets and driver fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "tcpip", "kmode", "network", "driver"]
weight: 5
---

# [Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys Fix

KMODE_EXCEPTION_NOT_HANDLED with `tcpip.sys` as the failing driver is a critical Blue Screen caused by an unhandled exception in the Windows TCP/IP networking stack. This occurs when the TCP/IP driver encounters a bug that the kernel cannot recover from.

This error frequently occurs during active network connections, VPN usage, or when network-inspecting security software interferes with TCP/IP processing.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: KMODE_EXCEPTION_NOT_HANDLED
> What failed: tcpip.sys

`tcpip.sys` implements the full TCP/IP protocol stack in Windows. A KMODE exception indicates the driver generated a fault that was not handled, such as accessing an invalid memory address. Common triggers include:

- **Third-party firewall with packet filtering** — Hooking into tcpip.sys causes exceptions
- **VPN client drivers** — Modifying TCP/IP behavior for tunneling
- **Network adapter driver bugs** — NIC drivers sending malformed packets to tcpip.sys
- **Corrupted Windows network components** — Damaged driver files from updates

## Common Causes

1. **Third-party security software** — Firewalls or antivirus performing deep packet inspection.
2. **VPN client software** — VPN drivers modifying the TCP/IP stack behavior.
3. **Corrupted network adapter driver** — NIC drivers incompatible with the current Windows version.
4. **Windows update corruption** — Recent updates damaging network stack components.

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
2. Uninstall third-party antivirus or firewall software.
3. Restart your computer.

### Solution 3: Update Network Adapter Driver

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion | Format-Table -AutoSize
```

Download the latest driver from the adapter manufacturer's website.

### Solution 4: Reinstall tcpip.sys

If the driver file is corrupted:

```cmd
sfc /scannow
```

If SFC cannot fix it:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Solution 5: Remove VPN Client Software

1. Uninstall all VPN clients from **Settings > Apps**.
2. Restart your computer.
3. Reinstall from the official source.

### Solution 6: Disable IPv6 (Temporary Workaround)

If the crash is related to IPv6 processing:

```powershell
Get-NetAdapterBinding -Name "*" -ComponentID ms_tcpip6 | Set-NetAdapterBinding -Enabled $false
```

Re-enable after identifying the root cause:

```powershell
Get-NetAdapterBinding -Name "*" -ComponentID ms_tcpip6 | Set-NetAdapterBinding -Enabled $true
```

## Related Errors

- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/windows/bsod-system-thread-exception-tcpip" >}})** — TCP/IP driver system thread crash
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED ndis.sys]({{< relref "/windows/bsod-kmode-exception-not-handled-ndis" >}})** — NDIS driver kernel exception
- **[BSOD IRQL_NOT_LESS_OR_EQUAL NETIO.SYS]({{< relref "/windows/bsod-irql-not-less-or-equal-netio" >}})** — Network I/O IRQL violation
