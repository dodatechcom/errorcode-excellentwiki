---
title: "[Solution] Driver PnP Watchdog Timeout Error Fix"
description: "Fix driver PnP (Plug and Play) watchdog timeout error on Windows when a device driver does not respond to a PnP operation within the expected time."
platforms: ["windows"]
severities: ["error"]
error_types: ["bsod"]
weight: 10
---

# [Solution] Driver PnP Watchdog Timeout Error Fix

A driver PnP watchdog timeout means a device driver failed to complete a Plug and Play operation within the allotted time.

## Common Causes
- Driver taking too long to initialize during device enumeration
- USB device causing driver timeout during hot-plug
- Storage driver hanging during disk detection
- Network adapter driver blocking during configuration
- BIOS/firmware issue delaying device initialization

## How to Fix

### Solution 1: Increase PnP Timeout

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\PnP" /v PollingMillisecondsInternalDevice /t REG_DWORD /d 12000 /f
```

### Solution 2: Update Device Drivers

Open Device Manager and update drivers for recently connected devices.

### Solution 3: Remove Problematic USB Devices

Disconnect recently connected USB devices one at a time to identify the culprit.

### Solution 4: Check Device Manager for Errors

```powershell
Get-PnpDevice | Where-Object { $_.Status -eq 'Error' } | Select-Object FriendlyName, InstanceId, Status
```

### Solution 5: Update BIOS/UEFI

Download and install the latest BIOS update from your manufacturer.

## Examples
```powershell
Get-PnpDevice | Where-Object { $_.Status -ne 'OK' } | Select-Object FriendlyName, Class, Status
```
