---
title: "[Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED ndis.sys Fix"
description: "Fix Blue Screen KMODE_EXCEPTION_NOT_HANDLED caused by ndis.sys on Windows 10 and 11. Resolve NDIS network driver exceptions with driver updates and stack resets."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD KMODE_EXCEPTION_NOT_HANDLED ndis.sys Fix

KMODE_EXCEPTION_NOT_HANDLED with `ndis.sys` as the failing driver is a critical Blue Screen caused by an unhandled exception in the Network Driver Interface Specification framework. This core networking component provides the interface between network protocol drivers and hardware-specific NIC drivers.

This error commonly occurs with Wi-Fi adapters, Ethernet adapters, and when third-party network software modifies the NDIS framework.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: KMODE_EXCEPTION_NOT_HANDLED
> What failed: ndis.sys

`ndis.sys` is the Windows NDIS framework driver that standardizes network communication between protocol drivers and NIC miniport drivers. A KMODE exception means a network driver generated a fault that was not handled by the kernel.

Common triggers include:

- **Buggy NIC driver** — Network adapter driver accessing invalid memory
- **Third-party network filter drivers** — Software hooking into the NDIS stack
- **Wi-Fi driver power management** — Power saving modes causing driver state corruption
- **Dual NIC conflicts** — Multiple network adapters with conflicting driver behaviors

## Common Causes

1. **Outdated or buggy network adapter driver** — The NIC driver has a code defect.
2. **Third-party network filter drivers** — VPN clients or network optimization software.
3. **Wi-Fi driver power management** — Aggressive power saving modes.
4. **Corrupted NDIS framework** — Damaged ndis.sys from Windows updates.

## How to Fix

### Solution 1: Update Network Adapter Driver

**Check current adapters:**

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, DriverVersion, Status | Format-Table -AutoSize
```

Download the latest driver from the adapter manufacturer's website and install it.

### Solution 2: Disable Wi-Fi Power Management

1. Open **Device Manager**.
2. Expand **Network adapters**.
3. Right-click your Wi-Fi adapter and select **Properties**.
4. Go to the **Power Management** tab.
5. Uncheck **Allow the computer to turn off this device to save power**.
6. Go to the **Advanced** tab and disable power saving properties.

### Solution 3: Remove Third-Party Network Software

```powershell
Get-NetAdapterBinding -Name "*" | Where-Object { $_.Enabled -eq $true } | Format-Table Name, ComponentID, DisplayName -AutoSize
```

Uninstall VPN clients or network optimization software from **Settings > Apps**.

### Solution 4: Reset Network Stack

```cmd
netsh winsock reset
netsh int ip reset
```

Restart after running these commands.

### Solution 5: Reinstall NDIS Framework

```cmd
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

Restart after repairs complete.

### Solution 6: Disable Network Adapters for Testing

Disable adapters one at a time to isolate the culprit:

```powershell
Disable-NetAdapter -Name "Wi-Fi" -Confirm:$false
```

Re-enable after identifying which adapter causes the crash:

```powershell
Enable-NetAdapter -Name "Wi-Fi" -Confirm:$false
```

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL ndis.sys]({{< relref "/windows/bsod-irql-not-less-or-equal-ndis" >}})** — NDIS IRQL violation
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED tcpip.sys]({{< relref "/windows/bsod-kmode-exception-not-handled-tcpip" >}})** — TCP/IP driver kernel exception
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — Generic system thread exception error
