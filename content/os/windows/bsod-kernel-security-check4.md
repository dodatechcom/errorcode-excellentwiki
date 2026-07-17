---
title: "[Solution] BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 ndis.sys Windows 11/10"
description: "Fix Blue Screen KERNEL_SECURITY_CHECK_FAILURE stop code 0x139 caused by ndis.sys network driver on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "kernel-security", "ndis", "network", "stop-0x139"]
weight: 5
---

# BSOD KERNEL_SECURITY_CHECK_FAILURE — 0x139 ndis.sys

The `KERNEL_SECURITY_CHECK_FAILURE` stop code `0x139` with `ndis.sys` indicates the Network Driver Interface Specification driver corrupted a critical kernel data structure. The kernel security integrity check detected that a linked list or structure managed by NDIS has been damaged.

## Common Causes

- **Corrupted NDIS driver** — The ndis.sys file is damaged by disk errors or failed updates.
- **NIC driver conflict** — Network adapter drivers corrupt NDIS internal data structures.
- **VPN filter driver bug** — VPN software NDIS filters cause corruption.
- **Third-party firewall** — Firewall products hooking into NDIS corrupt kernel structures.

## How to Fix

### Update Network Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

### Remove VPN and Network Filters

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

Uninstall VPN clients and remove third-party network filter drivers.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

### Reset Network Stack

```cmd
netsh int ip reset
netsh winsock reset
ipconfig /flushdns
```

### Disable Third-Party Firewalls

Temporarily uninstall third-party firewall software.

### Test RAM

```cmd
mdsched.exe
```

## Examples

```text
KERNEL_SECURITY_CHECK_FAILURE (139)
A kernel security check failure has occurred.

MODULE_NAME: ndis
IMAGE_NAME:  ndis.sys
```

## Related Errors

- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-driver-irql" >}}) — NDIS IRQL violation
- [BSOD KERNEL_SECURITY_CHECK_FAILURE]({{< relref "/os/windows/bsod-kernel-security-check-failure" >}}) — General kernel security failure
- [BSOD IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/os/windows/bsod-irql-not-less2" >}}) — NDIS IRQL error
