---
title: "[Solution] Windows Service Start Timeout 30000ms Fix"
description: "Fix Windows service start timeout after 30000 milliseconds. Resolve service that takes too long to start on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Service Start Timeout 30000ms Fix

A Windows service start timeout of 30000 milliseconds means the service did not report a running state within 30 seconds. Windows considers the start attempt failed.

## Common Causes
- Service performing heavy initialization during startup
- Service waiting for a network resource that is slow to respond
- Service dependent on a slow database connection
- Disk I/O bottleneck delaying service startup
- Antivirus scanning the service binary on each start

## How to Fix

### Solution 1: Increase Service Timeout

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control" /v ServicesPipeTimeout /t REG_DWORD /d 120000 /f
```

Restart after applying.

### Solution 2: Set Service to Delayed Start

```powershell
Set-Service -Name "ServiceName" -StartupType AutomaticDelayedStart
```

### Solution 3: Optimize Service Startup

Check the service logs for initialization bottlenecks. Consider lazy-loading dependencies.

### Solution 4: Set Dependent Services to Automatic

```powershell
Get-Service -Name "ServiceName" | Select-Object -ExpandProperty ServicesDependedOn | ForEach-Object { Set-Service -Name $_.Name -StartupType Automatic }
```

### Solution 5: Add Dependency Between Services

```cmd
sc.exe config "ServiceName" depend= "DepService1/DepService2"
```

## Examples
```powershell
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control" -Name ServicesPipeTimeout -ErrorAction SilentlyContinue
```
