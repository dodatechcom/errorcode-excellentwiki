---
title: "[Solution] BSOD SYSTEM_THREAD_EXCEPTION ndis.sys Wi-Fi Fix"
description: "Fix SYSTEM_THREAD_EXCEPTION caused by ndis.sys Wi-Fi adapter crashes on Windows. Resolve wireless driver BSOD and NDIS Wi-Fi failures on Windows 10/11."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] BSOD SYSTEM_THREAD_EXCEPTION ndis.sys Wi-Fi Fix

This BSOD variant specifically involves the Wi-Fi adapter NDIS driver. The wireless network interface card driver encounters an unhandled exception during system thread execution, often related to power management or roaming events.

## Common Causes
- Wi-Fi driver incompatibility with NDIS framework
- Wi-Fi adapter power management causing driver crashes
- Roaming between access points triggering a driver bug
- Bluetooth coexistence interference with Wi-Fi driver
- Corrupted Wi-Fi driver profile

## How to Fix

### Solution 1: Update Wi-Fi Driver

```powershell
Get-NetAdapter | Where-Object { $_.InterfaceDescription -like '*Wireless*' -or $_.InterfaceDescription -like '*Wi-Fi*' } | Select-Object Name, InterfaceDescription, DriverVersion
```

Download the latest driver from your adapter manufacturer website.

### Solution 2: Disable Wi-Fi Power Management

1. Open Device Manager
2. Expand Network adapters
3. Right-click your Wi-Fi adapter and select Properties > Power Management
4. Uncheck Allow the computer to turn off this device to save power

### Solution 3: Change Wi-Fi Band

Switch between 2.4 GHz and 5 GHz bands in your Wi-Fi adapter properties Advanced tab to avoid band-specific driver bugs.

### Solution 4: Reset Wi-Fi Profile

```cmd
netsh wlan delete profile name="NetworkName"
netsh wlan connect name="NetworkName"
```

### Solution 5: Disable Bluetooth Coexistence

In Wi-Fi adapter properties > Advanced tab, find Bluetooth Coexistence and set it to Disabled. Restart after the change.

## Examples
```powershell
Get-NetAdapter | Where-Object { $_.InterfaceDescription -like '*Wireless*' }
netsh wlan show interfaces
```
