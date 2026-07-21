---
title: "[Solution] Event ID 7011 Service Transaction Timeout Fix"
description: "Fix Windows Event ID 7011 when a service transaction times out while waiting for another service to respond on Windows 10/11."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Event ID 7011 Service Transaction Timeout Fix

Event ID 7011 occurs when a Windows service transaction times out. The service sent a transaction request to another service and it did not respond within the expected time frame.

## Common Causes
- Dependent service is overloaded or hung
- Deadlock between two service transactions
- Network latency between distributed services
- Resource contention from heavy system load
- Service configuration with too short a timeout

## How to Fix

### Solution 1: Identify the Timeout Event

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7011} -MaxEvents 5 | ForEach-Object { [xml]$_.ToXml() } | Select-Object -ExpandProperty EventData
```

### Solution 2: Increase Service Timeout

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v ServicesPipeTimeout /t REG_DWORD /d 180000 /f
```

Set the timeout to 180 seconds. Restart after applying.

### Solution 3: Restart the Dependent Service

```powershell
Restart-Service -Name "DependentServiceName" -Force
```

### Solution 4: Check System Resources

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, CPU, @{N='WS(MB)';E={[math]::Round($_.WorkingSet64/1MB)}}
```

### Solution 5: Review Service Dependencies

```powershell
Get-Service -Name "ServiceName" | Select-Object -ExpandProperty ServicesDependedOn | ForEach-Object { Get-Service $_.Name | Select-Object Name, Status }
```

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7011} -MaxEvents 10 | Format-Table TimeCreated, Message -Wrap
```
