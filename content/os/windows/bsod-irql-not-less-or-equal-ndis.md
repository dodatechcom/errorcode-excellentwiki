---
title: "[Solution] BSOD IRQL_NOT_LESS_OR_EQUAL ndis.sys Fix"
description: "Fix Blue Screen IRQL_NOT_LESS_OR_EQUAL caused by ndis.sys on Windows 10 and 11. Resolve network driver interface errors with driver updates and network stack resets."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
tags: ["bsod", "blue-screen", "ndis", "network", "irql", "driver"]
weight: 5
---

# [Solution] BSOD IRQL_NOT_LESS_OR_EQUAL ndis.sys Fix

IRQL_NOT_LESS_OR_EQUAL with `ndis.sys` as the failing driver is a critical Blue Screen caused by the Network Driver Interface Specification driver accessing memory at an incorrect interrupt request level. This indicates a bug in a network driver or the NDIS framework itself.

This error commonly occurs during active network connections, especially with Wi-Fi adapters, VPN clients, or third-party network optimization software.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: IRQL_NOT_LESS_OR_EQUAL
> What failed: ndis.sys

`ndis.sys` is the core Windows networking framework that provides a standardized interface between network protocol drivers and hardware-specific NIC drivers. An IRQL violation in ndis.sys means a network driver attempted to access memory at a processor interrupt level that is too high for the operation.

Common triggers include:

- **Faulty network adapter driver** — NIC driver accessing paged memory at elevated IRQL
- **Third-party network software** — VPN clients or network optimizers hooking into NDIS
- **Wi-Fi adapter power management** — Power saving modes causing driver timing issues
- **Dual NIC conflicts** — Multiple network adapters with conflicting driver behaviors

## Common Causes

1. **Outdated or corrupted network adapter driver** — The NIC driver has a bug that causes IRQL violations.
2. **VPN client software** — VPN drivers modify network packet handling and can conflict with NDIS.
3. **Wi-Fi power management** — Aggressive power saving modes cause driver state corruption.
4. **Third-party firewall or network optimizer** — Software that hooks into the NDIS stack.

## How to Fix

### Solution 1: Reset the Network Stack

```cmd
netsh winsock reset
netsh int ip reset
ipconfig /flushdns
```

Restart your computer after running these commands.

### Solution 2: Update Network Adapter Driver

**Check current network adapters and drivers:**

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion, Status | Format-Table -AutoSize
```

Update the driver:

1. Open **Device Manager**.
2. Expand **Network adapters**.
3. Right-click each adapter and select **Update driver**.
4. Choose **Search automatically for drivers**.

For best results, download the driver from the adapter manufacturer's website (Intel, Realtek, Qualcomm, etc.).

### Solution 3: Disable Wi-Fi Power Management

Wi-Fi adapters with aggressive power saving frequently cause ndis.sys crashes:

1. Open **Device Manager**.
2. Expand **Network adapters**.
3. Right-click your Wi-Fi adapter and select **Properties**.
4. Go to the **Power Management** tab.
5. Uncheck **Allow the computer to turn off this device to save power**.
6. Go to the **Advanced** tab and disable these properties if present:
   - **Power Save Mode** → Disabled
   - **Throughput Booster** → Disabled
   - **Wake on Magic Packet** → Disabled

### Solution 4: Remove VPN Software

VPN clients frequently cause ndis.sys IRQL violations:

1. Open **Settings > Apps > Installed apps**.
2. Find and uninstall any VPN client.
3. Restart your computer.
4. Reinstall the VPN client from the official website.

**Check for network filter drivers:**

```powershell
Get-NetAdapterBinding -Name "*" | Where-Object { $_.Enabled -eq $true } | Format-Table Name, ComponentID, DisplayName -AutoSize
```

### Solution 5: Perform Network Adapter Reset

```powershell
Get-NetAdapter | Where-Object { $_.Status -eq "Up" } | Restart-NetAdapter
```

Or reset all network adapters completely:

```cmd
netcfg -d
```

Restart your computer. Windows will reinstall all network adapters.

### Solution 6: Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the most recent `.dmp` file in **WinDbg** and run `!analyze -v`. Look for `ndis` in MODULE_NAME and the specific NIC driver in the call stack.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL NETIO.SYS]({{< relref "/windows/bsod-irql-not-less-or-equal-netio" >}})** — Network I/O subsystem IRQL violation
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED ndis.sys]({{< relref "/windows/bsod-kmode-exception-not-handled-ndis" >}})** — NDIS driver kernel exception
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/windows/bsod-system-thread-exception-tcpip" >}})** — TCP/IP driver system thread crash
