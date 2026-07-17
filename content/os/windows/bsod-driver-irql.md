---
title: "[Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xD1 ndis.sys Windows 11/10"
description: "Fix Blue Screen DRIVER_IRQL_NOT_LESS_OR_EQUAL stop code 0xD1 caused by ndis.sys network driver failure on Windows 10 and 11."
platforms: ["windows"]
error-types: ["bsod"]
severities: ["critical"]
tags: ["bsod", "blue-screen", "driver-irql", "ndis", "network", "stop-0xd1"]
weight: 5
---

# BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL — 0xD1 ndis.sys

The `DRIVER_IRQL_NOT_LESS_OR_EQUAL` stop code with `0xD1` and the faulty module `ndis.sys` indicates the Windows Network Driver Interface Specification driver attempted to access pageable memory at an elevated IRQL. This is a common network-related Blue Screen of Death on Windows 10 and 11.

## Common Causes

- **Corrupted or outdated network adapter driver** — The NDIS miniport driver has a bug causing invalid memory access during packet processing.
- **Wi-Fi adapter driver conflict** — Third-party wireless drivers interfere with the NDIS framework.
- **VPN software with network filter drivers** — VPN clients install NDIS filter drivers that cause IRQL violations.
- **Faulty RAM in network buffer regions** — Memory corruption causes the NIC driver to read invalid addresses.

## How to Fix

### Identify the Faulting Module

Check the minidump to confirm `ndis.sys` is the culprit:

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime
```

Open the `.dmp` file in WinDbg and run `!analyze -v`:

```text
0: kd> !analyze -v
MODULE_NAME: ndis
IMAGE_NAME:  ndis.sys
```

### Update Network Adapter Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest driver from the adapter manufacturer's website.

### Remove VPN and Network Filters

```powershell
Get-NetAdapterFilter | Select-Object Name, ComponentId, Enabled
```

Disable or remove third-party VPN clients and network filter drivers.

### Disable Wi-Fi Power Management

Open Device Manager, expand Network adapters, right-click the adapter, select Properties > Power Management, and uncheck "Allow the computer to turn off this device to save power."

### Test RAM

```cmd
mdsched.exe
```

Select **Restart now and check for problems**.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples

```text
DRIVER_IRQL_NOT_LESS_OR_EQUAL (d1)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.

STACK_TEXT:
ndis!ndisMIndicateStatusEx+0x...
```

## Related Errors

- [BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-driver-irql-not-less-or-equal" >}}) — General DRIVER_IRQL error
- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — General IRQL violation
- [BSOD DPC Watchdog Violation]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — DPC timeout from driver issues
- [BSOD NETWORK_DRIVER_IRQL_FAULT]({{< relref "/os/windows/bsod-irql-not-less2" >}}) — ndis.sys IRQL fault variant
