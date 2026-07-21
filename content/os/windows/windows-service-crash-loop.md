---
title: "[Solution] Windows Service Crash Loop Fix"
description: "Fix Windows service that keeps crashing and restarting in a loop. Resolve service failure events and service recovery configuration on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Service Crash Loop Fix

A service crash loop occurs when a Windows service repeatedly starts, encounters a fatal error, and restarts. This consumes system resources and may affect dependent services.

## Common Causes
- Bug in the service application code
- Service depending on another service that is not running
- Corrupted service binary or configuration
- Invalid startup parameters causing immediate failure
- Service account credentials expired or invalid

## How to Fix

### Solution 1: Identify the Crashing Service

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7031,7034} -MaxEvents 20 | Format-Table TimeCreated, Message -Wrap
```

### Solution 2: Change Recovery Options

```cmd
sc.exe failure "ServiceName" reset= 86400 actions= restart/60000/restart/120000/restart/300000
```

### Solution 3: Check Service Dependencies

```powershell
Get-Service -Name "ServiceName" | Select-Object -ExpandProperty ServicesDependedOn | Select-Object Name, Status
```

### Solution 4: Run Service Under LocalSystem

Temporarily change the service account to LocalSystem in services.msc.

### Solution 5: Check Service Binary Path

```powershell
Get-WmiObject Win32_Service | Where-Object { $_.Name -eq 'ServiceName' } | Select-Object Name, PathName, State
```

## Examples
```powershell
Get-Service | Where-Object { $_.Status -eq 'Stopped' -and $_.StartType -eq 'Automatic' } | Select-Object Name, Status, StartType
```
