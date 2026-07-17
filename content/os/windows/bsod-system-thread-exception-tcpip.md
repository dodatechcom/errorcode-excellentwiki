---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED tcpip.sys Fix"
description: "Fix Blue Screen SYSTEM_THREAD_EXCEPTION_NOT_HANDLED caused by tcpip.sys on Windows 10 and 11. Resolve TCP/IP driver crashes with network stack resets and driver updates."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED tcpip.sys Fix

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED with `tcpip.sys` as the failing driver is a critical Blue Screen caused by a crash in the Windows TCP/IP networking stack. This driver handles all TCP and IP network communications, and a failure here indicates a problem with network processing.

This BSOD often occurs during heavy network activity, VPN connections, or when third-party firewall or antivirus software interferes with network traffic inspection.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED
> What failed: tcpip.sys

`tcpip.sys` is the core Windows networking driver that implements the TCP/IP protocol stack. When this driver crashes, it means the network subsystem encountered an unrecoverable error. Common triggers include:

- **Third-party firewall or antivirus with network inspection** — Software that hooks into the network stack
- **VPN client conflicts** — VPN software modifying network routing or packet filtering
- **Corrupted network adapter drivers** — NIC drivers conflicting with the TCP/IP stack
- **Malware using the network stack** — Network-based malware causing protocol violations

## Common Causes

1. **Third-party security software** — Antivirus or firewall programs that perform deep packet inspection.
2. **VPN client software** — VPN drivers that modify the TCP/IP stack for tunneling.
3. **Corrupted network adapter driver** — Outdated or buggy NIC drivers.
4. **Windows network stack corruption** — Damaged network configuration from bad updates.

## How to Fix

### Solution 1: Reset the Network Stack

Reset all network configurations to defaults:

```cmd
netsh winsock reset
netsh int ip reset
ipconfig /flushdns
ipconfig /release
ipconfig /renew
```

Restart your computer after running these commands.

### Solution 2: Remove Third-Party Security Software

Third-party firewalls and antivirus programs that inspect network traffic frequently crash tcpip.sys:

1. Open **Settings > Apps > Installed apps**.
2. Find your third-party antivirus or firewall.
3. Uninstall it and restart your computer.

**Check for network filter drivers:**

```powershell
Get-NetAdapterBinding | Where-Object { $_.ComponentID -like "*ms_firewall*" -or $_.ComponentID -like "*ms_lbfep*" } | Format-Table -AutoSize
```

### Solution 3: Update Network Adapter Driver

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion, Status | Format-Table -AutoSize
```

Update the driver:

1. Open **Device Manager**.
2. Expand **Network adapters**.
3. Right-click your network adapter and select **Update driver**.
4. Choose **Search automatically for drivers**.

Or download the latest driver from your adapter manufacturer's website (Intel, Realtek, Killer, etc.).

### Solution 4: Reinstall the TCP/IP Stack

If the network stack is corrupted:

```cmd
netsh int ip reset resetlog.txt
```

This rebuilds the TCP/IP stack from scratch. Restart after running.

### Solution 5: Disable Large Send Offload (LSO)

LSO can cause tcpip.sys crashes on some network configurations:

```powershell
Get-NetAdapterAdvancedProperty -Name "*" -DisplayName "Large Send Offload*" | Format-Table Name, DisplayName, DisplayValue -AutoSize
```

Disable it for all adapters:

```powershell
Get-NetAdapterAdvancedProperty -Name "*" -DisplayName "Large Send Offload IPv4" | Set-NetAdapterAdvancedProperty -DisplayValue "Disabled"
Get-NetAdapterAdvancedProperty -Name "*" -DisplayName "Large Send Offload V2 IPv4" | Set-NetAdapterAdvancedProperty -DisplayValue "Disabled"
```

### Solution 6: Analyze the Minidump

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

Open the most recent `.dmp` file in **WinDbg** and run `!analyze -v`. Look for `tcpip` in the MODULE_NAME and the specific function that caused the exception.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL tcpip.sys]({{< relref "/windows/bsod-irql-not-less-or-equal-ndis" >}})** — Another tcpip.sys related network BSOD
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/windows/bsod-kmode-exception-not-handled-tcpip" >}})** — TCP/IP driver kernel-mode exception
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — Generic version of this BSOD
