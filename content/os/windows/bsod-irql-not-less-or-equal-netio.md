---
title: "[Solution] BSOD IRQL_NOT_LESS_OR_EQUAL NETIO.SYS Fix"
description: "Fix Blue Screen IRQL_NOT_LESS_OR_EQUAL caused by NETIO.SYS on Windows 10 and 11. Resolve network I/O driver errors with stack resets and driver updates."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "netio", "network", "irql", "driver"]
weight: 5
---

# [Solution] BSOD IRQL_NOT_LESS_OR_EQUAL NETIO.SYS Fix

IRQL_NOT_LESS_OR_EQUAL with `NETIO.SYS` as the failing driver is a critical Blue Screen caused by the Windows Network I/O subsystem accessing memory at an incorrect interrupt request level. This driver sits between the TCP/IP stack and the NDIS framework.

This error commonly occurs during active network connections, large file transfers, or when third-party security software performs deep packet inspection.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: IRQL_NOT_LESS_OR_EQUAL
> What failed: NETIO.SYS

`NETIO.SYS` is the Windows Network I/O subsystem driver that handles network packet processing between the TCP/IP stack and the NDIS miniport drivers. An IRQL violation here indicates a network-related driver accessing memory improperly.

Common triggers include:

- **Third-party firewall or antivirus with network inspection** — Deep packet inspection hooks into NETIO
- **VPN client software** — VPN drivers modify network packet routing
- **Corrupted Windows network components** — Damaged network stack from bad updates
- **Network adapter driver bugs** — NIC drivers that do not properly handle IRQL requirements

## Common Causes

1. **Third-party security software** — Antivirus or firewall performing network traffic inspection.
2. **VPN client conflicts** — VPN software that modifies packet routing or filtering.
3. **Corrupted network drivers** — Outdated or buggy NIC drivers.
4. **Windows network stack corruption** — Damaged network configuration files.

## How to Fix

### Solution 1: Reset the Network Stack

```cmd
netsh winsock reset
netsh int ip reset
ipconfig /flushdns
ipconfig /release
ipconfig /renew
```

Restart your computer after running these commands.

### Solution 2: Uninstall Third-Party Security Software

Network-inspecting security software is the most common cause of NETIO.SYS crashes:

1. Open **Settings > Apps > Installed apps**.
2. Find your third-party antivirus or firewall.
3. Uninstall it and restart your computer.

**Check for network filter drivers:**

```powershell
Get-NetAdapterBinding -Name "*" | Where-Object { $_.Enabled -eq $true } | Select-Object Name, ComponentID, DisplayName | Format-Table -AutoSize
```

### Solution 3: Update Network Adapter Driver

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion, Status | Format-Table -AutoSize
```

Download the latest driver from your adapter manufacturer's website and install it.

### Solution 4: Remove VPN Client Software

1. Uninstall all VPN clients from **Settings > Apps**.
2. Restart your computer.
3. Reinstall the VPN from the official source.

### Solution 5: Disable Large Send Offload

```powershell
Get-NetAdapterAdvancedProperty -Name "*" -DisplayName "Large Send Offload IPv4" | Set-NetAdapterAdvancedProperty -DisplayValue "Disabled"
Get-NetAdapterAdvancedProperty -Name "*" -DisplayName "Large Send Offload V2 IPv4" | Set-NetAdapterAdvancedProperty -DisplayValue "Disabled"
```

### Solution 6: Reinstall Network Stack

If the above steps fail, reset the entire network stack:

```cmd
netcfg -d
```

Restart your computer. Windows will reinstall all network components.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/windows/bsod-irql-not-less-or-equal-ndis" >}})** — NDIS framework IRQL violation
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/windows/bsod-kmode-exception-not-handled-tcpip" >}})** — TCP/IP driver kernel exception
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — Generic system thread exception error
