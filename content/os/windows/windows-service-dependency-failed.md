---
title: "[Solution] Windows Service Dependency Failed Fix"
description: "Fix Windows service dependency failures with these step-by-step solutions. Includes dependency chain checks, service ordering fixes, and troubleshooting commands."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Windows Service Dependency Failed Fix

A Windows service cannot start because one or more of its dependent services have failed to start. This cascading failure prevents the target service from initializing properly.

## Description

The error typically appears as:

> "Windows could not start the [Service Name] service on Local Computer. Error 1068: The dependency service or group failed to start."

This error occurs when a service has a dependency chain and one or more services in that chain have failed. The service cannot start until all dependencies are running successfully.

## Common Causes

1. **Dependent service stopped** — A required service is not running.
2. **Circular dependencies** — Services configured with circular dependency chains.
3. **Delayed start conflicts** — Services with delayed start not ready in time.
4. **Corrupted dependency service** — A dependency service is damaged and cannot start.

## Solutions

### Solution 1: Check Dependent Services

```cmd
sc qc [ServiceName]
```

Look at the `DEPENDENCIES` section. Start each dependency manually:

```cmd
net start [DependencyName]
```

### Solution 2: Check All Service Dependencies Recursively

```powershell
$service = Get-Service -Name "[ServiceName]"
$deps = (Get-WmiObject Win32_Service -Filter "Name='[ServiceName]'").Dependencies
foreach ($dep in $deps) { Get-Service -Name $dep | Select-Object Name, Status, StartType }
```

### Solution 3: Start Dependencies in Correct Order

For Windows Update services, start in this order:

```cmd
net start cryptSvc
net start bits
net start trustedinstaller
net start wuauserv
```

For other services, identify the correct order:

```cmd
sc enumdepend [ServiceName]
```

### Solution 4: Change Service Startup Type

If a dependency service is disabled, enable it:

```powershell
Set-Service -Name "[DependencyName]" -StartupType Automatic
Start-Service -Name "[DependencyName]"
```

## Related Errors

- [Windows Service Failed to Start]({{< relref "/os/windows/windows-service-failed-to-start" >}}) — General service start failure
- [Windows Update Service Error]({{< relref "/os/windows/windows-update-service-error" >}}) — Update service specific
- [Error 0x8024001e]({{< relref "/os/windows/windows-update-0x8024001e" >}}) — Update service stopped
