---
title: "[Solution] Event ID 4101 Display Driver Stopped Responding Fix"
description: "Fix Windows Event ID 4101 display driver stopped responding and has recovered. Resolve GPU driver TDR failures in the System event log."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] Event ID 4101 Display Driver Stopped Responding Fix

Event ID 4101 records when the display driver stops responding and recovers through the Timeout Detection and Recovery (TDR) mechanism. This means your GPU driver stopped responding to Windows requests.

## Common Causes
- GPU overheating due to dust or failing cooling
- Outdated or corrupted graphics driver
- Overclocked GPU exceeding stability limits
- Insufficient power supply to the GPU
- Faulty graphics card hardware

## How to Fix

### Solution 1: Increase TDR Timeout

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v TdrDelay /t REG_DWORD /d 10 /f
```

### Solution 2: Update Graphics Driver

Download the latest driver from the GPU manufacturer. Perform a clean installation.

### Solution 3: Check GPU Temperature

Use GPU-Z or HWMonitor to check temperatures. Clean dust from the GPU cooler if temperatures exceed 85 degrees Celsius under load.

### Solution 4: Remove GPU Overclocking

Reset GPU clock speeds to factory defaults using MSI Afterburner or your GPU vendor utility.

### Solution 5: Disable TDR

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v TdrLevel /t REG_DWORD /d 0 /f
```

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=4101} -MaxEvents 5 | Format-Table TimeCreated, Message -Wrap
```
