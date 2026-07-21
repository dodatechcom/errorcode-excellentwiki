---
title: "[Solution] Event ID 41 Kernel Power Unexpected Shutdown Fix"
description: "Fix Windows Event ID 41 Kernel-Power unexpected system shutdown. Resolve unclean power events and random restart errors on Windows 10/11."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Event ID 41 Kernel Power Unexpected Shutdown Fix

Event ID 41 Kernel-Power records unexpected system shutdowns where Windows did not shut down cleanly. This event indicates the system lost power or crashed before completing a proper shutdown.

## Common Causes
- Faulty power supply unable to provide stable voltage
- Overheating CPU or GPU triggering thermal shutdown
- Unstable overclocking causing system instability
- Failing RAM causing random system crashes
- Outdated BIOS or chipset drivers causing power management issues

## How to Fix

### Solution 1: Review Event Details

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=41; ProviderName='Microsoft-Windows-Kernel-Power'} -MaxEvents 5 | ForEach-Object { [xml]$_.ToXml() } | Select-Object -ExpandProperty EventData
```

### Solution 2: Check Power Supply

If the Event 41 occurs frequently without a corresponding BSOD, the power supply may be failing. Test with a PSU tester.

### Solution 3: Disable Fast Startup and Hibernation

```cmd
powercfg /h off
powercfg /change standby-timeout-ac 0
```

### Solution 4: Check for Thermal Issues

```powershell
Get-WmiObject MSAcpi_ThermalZoneTemperature -Namespace root/wmi | Select-Object @{N='Temp(C)';E={$_.CurrentTemperature/100 - 273.15}}
```

### Solution 5: Run Memory Diagnostic

```cmd
mdsched.exe
```

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=41; ProviderName='Microsoft-Windows-Kernel-Power'} -MaxEvents 10 | Format-Table TimeCreated, Message -Wrap
```
