---
title: "[Solution] Windows Service Failed to Start Fix"
description: "Fix Windows services that fail to start with these step-by-step solutions. Includes dependency checks, Event Viewer diagnostics, and permission repairs."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] Windows Service Failed to Start Fix

A Windows service has failed to start, preventing dependent applications or system functions from working correctly. This error can affect any Windows service and requires diagnosing the specific failure cause.

## Description

The error typically appears as:

> "Windows could not start the [Service Name] service on Local Computer. Error 1053: The service did not respond to the start or control request in a timely fashion."

Or:

> "Error 0x80070005: Access is denied."

Service start failures are common and can be caused by dependency failures, corrupted files, incorrect permissions, or configuration issues.

## Common Causes

1. **Service dependencies stopped** — Required dependent services not running.
2. **Corrupted service files** — DLLs or executables used by the service are damaged.
3. **Incorrect service permissions** — The service account lacks required permissions.
4. **Event Viewer logs** — Errors logged in Windows Event Log.

## Solutions

### Solution 1: Check Service Dependencies

```cmd
sc qc [ServiceName]
```

This shows the service's dependencies. Start them first:

```cmd
net start [DependencyServiceName]
```

### Solution 2: Check Event Viewer for Errors

```powershell
Get-WinEvent -LogName System -MaxEvents 50 | Where-Object {$_.LevelDisplayName -eq 'Error'} | Select-Object TimeCreated, Message | Format-List
```

Look for entries related to the failing service.

### Solution 3: Run System File Checker

```cmd
sfc /scannow
```

Corrupted system files are a common cause of service start failures. Restart after the scan completes.

### Solution 4: Reset Service Permissions

```cmd
sc sdset [ServiceName] D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)
```

Replace `[ServiceName]` with the actual service name. Then restart the service:

```cmd
net stop [ServiceName]
net start [ServiceName]
```

## Related Errors

- [Windows Service Dependency Failed]({{< relref "/os/windows/windows-service-dependency-failed" >}}) — Service dependency chain failure
- [Windows Update Service Error]({{< relref "/os/windows/windows-update-service-error" >}}) — Update service specific failure
- [Error 0x80070424]({{< relref "/os/windows/0x80070424" >}}) — Service does not exist
