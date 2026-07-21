---
title: "[Solution] Windows Service Failed Due to Dependent Service Fix"
description: "Fix Windows service that fails to start because a dependent service is not running or has failed. Resolve service dependency chain failures on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Service Failed Due to Dependent Service Fix

A service that depends on another service will fail to start if its required dependency is stopped or in a failed state.

## Common Causes
- Dependent service crashed or was manually stopped
- Dependent service set to Manual startup and not yet started
- Circular dependency between two services
- Dependent service account credentials are invalid
- Group Policy disabling the dependent service

## How to Fix

### Solution 1: Identify Dependent Services

```powershell
Get-Service -Name "ServiceName" | Select-Object Name, Status, ServicesDependedOn, DependentServices
```

### Solution 2: Start Dependencies in Order

```powershell
$service = Get-Service -Name "ServiceName"
$service.ServicesDependedOn | ForEach-Object { Start-Service -Name $_.Name }
Start-Service -Name "ServiceName"
```

### Solution 3: Set Dependent Services to Automatic

```powershell
Set-Service -Name "DependentService" -StartupType Automatic
```

### Solution 4: Check Dependency Chain

```powershell
Get-Service -Name "ServiceName" -RequiredServices | ForEach-Object { Get-Service -Name $_.Name }
```

### Solution 5: Check Service Account

```powershell
Get-WmiObject Win32_Service | Where-Object { $_.Name -eq 'DependentService' } | Select-Object Name, StartName, State
```

## Examples
```powershell
Get-Service -Name "Spooler" -RequiredServices
Get-Service -Name "Spooler" | Select-Object -ExpandProperty DependentServices
```
