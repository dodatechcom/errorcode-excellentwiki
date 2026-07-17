---
title: "[Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xA netio.sys Windows 11/10"
description: "Fix Blue Screen DRIVER_IRQL_NOT_LESS_OR_EQUAL stop code 0xA caused by netio.sys network I/O driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "driver-irql", "netio", "network", "stop-0xa"]
weight: 5
---

# BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xA netio.sys

The `DRIVER_IRQL_NOT_LESS_OR_EQUAL` stop code `0xA` with `netio.sys` indicates the Network I/O subsystem driver attempted to access memory at an elevated Interrupt Request Level. The `netio.sys` driver manages Windows network stack operations.

## Common Causes

- **Network filter driver conflict** — Third-party firewalls or antivirus install network filter drivers that cause IRQL violations.
- **Corrupted TCP/IP stack** — Damaged network stack components cause invalid memory access.
- **Faulty NIC driver** — Network interface card driver accesses paged memory at high IRQL.
- **VPN client filter drivers** — VPN software installs NDIS LWF (Lightweight Filter) drivers that cause issues.

## How to Fix

### Reset TCP/IP Stack

```cmd
netsh int ip reset
netsh winsock reset
ipconfig /flushdns
```

Restart the computer after running these commands.

### Identify Faulty Network Filter Drivers

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled | Format-Table -AutoSize
```

Disable or remove unnecessary network filter drivers.

### Update Network Adapter Driver

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest driver from the NIC manufacturer.

### Uninstall Problematic VPN Software

```powershell
Get-WmiObject Win32_Product | Where-Object { $_.Name -like "*VPN*" -or $_.Name -like "*Tunnel*" } | Select-Object Name, Version
```

Uninstall VPN clients and reinstall the latest version.

### Disable Network Power Management

```powershell
# Disable power saving on network adapter
Get-NetAdapter | Set-NetAdapterAdvancedProperty -DisplayName "Energy Efficient Ethernet" -DisplayValue "Disabled"
```

### Check for Faulty RAM

```cmd
mdsched.exe
```

## Examples

```text
DRIVER_IRQL_NOT_LESS_OR_EQUAL (a)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.

MODULE_NAME: netio
IMAGE_NAME:  netio.sys
```

## Related Errors

- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-driver-irql" >}}) — NDIS driver IRQL violation
- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — General IRQL violation
- [BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — DPC timeout
