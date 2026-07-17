---
title: "[Solution] BSOD IRQL_NOT_LESS_OR_EQUAL — 0xA ndis.sys Windows 11/10"
description: "Fix Blue Screen IRQL_NOT_LESS_OR_EQUAL stop code 0xA caused by ndis.sys network driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "irql", "ndis", "network", "stop-0xa"]
weight: 5
---

# BSOD IRQL_NOT_LESS_OR_EQUAL — 0xA ndis.sys

The `IRQL_NOT_LESS_OR_EQUAL` stop code `0xA` with `ndis.sys` indicates the NDIS (Network Driver Interface Specification) driver accessed paged memory at an elevated IRQL. This is a network-related BSOD commonly caused by NIC driver bugs or VPN filter driver conflicts.

## Common Causes

- **NIC driver accessing paged memory at high IRQL** — The network card driver has a bug in its interrupt handler.
- **VPN NDIS filter driver** — VPN clients install NDIS Lightweight Filter drivers that cause IRQL violations.
- **Wi-Fi adapter driver issue** — Wireless drivers encounter invalid memory access during packet processing.
- **Faulty RAM** — Memory corruption causes the NDIS driver to read invalid addresses.

## How to Fix

### Update Network Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Remove VPN Filter Drivers

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

Uninstall VPN clients and remove their NDIS filter drivers.

### Disable Wi-Fi Power Management

Open Device Manager > Network Adapters > adapter properties > Power Management > uncheck "Allow the computer to turn off this device to save power."

### Test RAM

```cmd
mdsched.exe
```

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
```

### Reset Network Stack

```cmd
netsh int ip reset
netsh winsock reset
```

## Examples

```text
IRQL_NOT_LESS_OR_EQUAL (a)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.

MODULE_NAME: ndis
IMAGE_NAME:  ndis.sys
```

## Related Errors

- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-driver-irql" >}}) — NDIS IRQL violation
- [BSOD IRQL_NOT_LESS_OR_EQUAL ntoskrnl.exe]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — Kernel IRQL error
- [BSOD IRQL_NOT_LESS_OR_EQUAL dxgkrnl.sys]({{< relref "/os/windows/bsod-irql-not-less3" >}}) — DirectX IRQL error
