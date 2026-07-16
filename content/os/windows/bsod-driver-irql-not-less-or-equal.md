---
title: "[Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL Windows 11/10 — Fixed"
description: "Fix Blue Screen DRIVER_IRQL_NOT_LESS_OR_EQUAL error on Windows 10 and 11. Update network and storage drivers, check RAM, and disable VPN software to resolve."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "driver-irql", "network-driver", "stop-code"]
weight: 5
---

# [Solution] BSOD DRIVER_IRQL_NOT_LESS_OR_EQUAL Windows 11/10 — Fixed

DRIVER_IRQL_NOT_LESS_OR_EQUAL is a critical Blue Screen of Death error with stop code `0x000000D1`. It occurs when a kernel-mode driver attempts to access a memory address at an Interrupt Request Level (IRQL) that is too high for the type of memory access being performed. This is a variant of IRQL_NOT_LESS_OR_EQUAL specifically tied to a driver making an invalid memory request.

This BSOD affects both Windows 10 and 11 and frequently points to network drivers, VPN software, or antivirus products.

## Common Causes

- **Network driver issues** — NIC drivers, Wi-Fi adapters, or VPN tunnel drivers attempting invalid memory access.
- **Third-party antivirus or firewall** — Kernel-mode security products that intercept network traffic at too high an IRQL.
- **Outdated storage drivers** — AHCI or NVMe drivers with bugs in their interrupt handling routines.
- **Faulty RAM** — Memory corruption causes drivers to read invalid addresses during interrupt handling.

## How to Fix

### Identify the Faulting Driver

The blue screen message typically names the driver:

> What failed: `ndis.sys`, `tcpip.sys`, `rtwlanu.sys`, etc.

**Analyze the minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the most recent `.dmp` file in WinDbg and run `!analyze -v`. The **MODULE_NAME** and **IMAGE_NAME** lines identify the problematic driver.

### Update Network Drivers

Network drivers are the most common cause of this specific BSOD.

1. Open **Device Manager** (`Win + X` > Device Manager).
2. Expand **Network adapters**.
3. Right-click each adapter and select **Update driver** > **Search automatically for drivers**.

**Check current network driver versions:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "NET" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

Download the latest drivers directly from the hardware manufacturer's website rather than relying on Windows Update.

### Uninstall or Reinstall VPN and Security Software

VPN clients and third-party firewalls frequently cause this error:

1. Open **Settings > Apps > Installed apps**.
2. Sort by **Install date** to find recently installed VPN or security software.
3. Uninstall the software and restart your computer.
4. Reinstall the latest version from the vendor's website if needed.

### Update Storage Drivers

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.DeviceClass -eq "SCSIAdapter" -or $_.DeviceClass -eq "HDC" } | Select-Object DeviceName, DriverVersion, DriverDate | Format-Table -AutoSize
```

For Intel systems, install the latest Intel Rapid Storage Technology (IRST) driver. For AMD systems, install the AMD SATA/NVMe driver from your motherboard manufacturer.

### Test RAM

```cmd
mdsched.exe
```

Select **Restart now and check for problems**. Use MemTest86 for extended testing if initial diagnostics pass.

### Repair System Files

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

## Examples

This error commonly occurs in these scenarios:

- **After installing VPN software** — A VPN client's network filter driver accesses memory at an elevated IRQL.
- **Following a Windows Update** — An updated network driver contains a bug in its interrupt handler.
- **When connecting to Wi-Fi** — The wireless adapter driver attempts to access freed memory during connection.
- **With antivirus network filters** — Security software intercepts packets at too high an IRQL level.

## Related Errors

- [BSOD IRQL_NOT_LESS_OR_EQUAL]({{< relref "/os/windows/bsod-irql-not-less-or-equal" >}}) — The general IRQL violation BSOD
- [BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/os/windows/bsod-kmode-exception" >}}) — Kernel-mode program generates an unhandled exception
- [BSOD DPC Watchdog Violation]({{< relref "/os/windows/bsod-dpc-watchdog-violation" >}}) — Deferred procedure call timeout from driver issues
- [BSOD PAGE_FAULT_IN_NONPAGED_AREA]({{< relref "/os/windows/bsod-page-fault-in-nonpaged-area" >}}) — Memory page reference error
