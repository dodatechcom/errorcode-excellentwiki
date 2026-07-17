---
title: "[Solution] BSOD DPC_WATCHDOG_VIOLATION — 0x133 ndis.sys Windows 11/10"
description: "Fix Blue Screen DPC_WATCHDOG_VIOLATION stop code 0x133 caused by ndis.sys network driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "dpc-watchdog", "ndis", "network", "stop-0x133"]
weight: 5
---

# BSOD DPC_WATCHDOG_VIOLATION — 0x133 ndis.sys

The `DPC_WATCHDOG_VIOLATION` stop code `0x133` with `ndis.sys` indicates the Network Driver Interface Specification driver took too long to complete a Deferred Procedure Call. The DPC watchdog timer expired while the NDIS driver was processing network operations.

## Common Causes

- **NIC driver DPC timeout** — The network card driver hangs during a DPC callback.
- **Network stack congestion** — High network traffic causes NDIS to exceed DPC time limits.
- **VPN filter driver** — VPN NDIS filters cause DPC timeouts.
- **Wi-Fi driver bug** — Wireless adapter drivers encounter DPC timing issues.

## How to Fix

### Update Network Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Remove VPN and Network Filters

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

### Disable Wi-Fi Power Management

Device Manager > Network adapters > Wi-Fi adapter > Properties > Power Management:
- Uncheck "Allow the computer to turn off this device to save power"

### Disable Network Power Saving

```powershell
Get-NetAdapter | Set-NetAdapterAdvancedProperty -DisplayName "Energy Efficient Ethernet" -DisplayValue "Disabled"
```

### Reset Network Stack

```cmd
netsh int ip reset
netsh winsock reset
```

### Test with Wired Connection

If using Wi-Fi, test with an Ethernet cable to isolate the issue.

## Examples

```text
DPC_WATCHDOG_VIOLATION (133)
A DPC did not complete in a timely manner.

MODULE_NAME: ndis
IMAGE_NAME:  ndis.sys
```

## Related Errors

- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-driver-irql" >}}) — NDIS IRQL violation
- [BSOD IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-irql-not-less2" >}}) — NDIS IRQL error
- [BSOD DPC_WATCHDOG_VIOLATION stornvme.sys]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — NVMe DPC timeout
