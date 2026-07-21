---
title: "[Solution] Event ID 7034 Service Crash Unexpectedly Fix"
description: "Fix Windows Event ID 7034 when a Windows service terminates unexpectedly. Resolve service crash errors in the System event log on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Event ID 7034 Service Crash Unexpectedly Fix

Event ID 7034 in the System log indicates a Windows service has crashed unexpectedly. The service terminated without a proper shutdown request, and Windows records the crash for diagnostic purposes.

## Common Causes
- Bug in the service application code
- Service depending on another failed service
- Memory corruption in the service process
- Corrupted service binary or configuration
- Service account password expired or changed

## How to Fix

### Solution 1: Check Service Dependencies

```powershell
Get-Service -Name "servicename" | Select-Object Name, Status, DependentServices, ServicesDependedOn
```

### Solution 2: Review Service Account

Verify the service account password has not expired.

### Solution 3: Check Event Viewer for Details

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=7034} -MaxEvents 10 | Format-Table TimeCreated, Message -Wrap
```

### Solution 4: Increase Service Recovery Options

In the service properties, set the Recovery tab to Restart the Service after failure with a delay of 60 seconds.

### Solution 5: Update Service Configuration

Open Services console (services.msc), check the service properties for the correct binary path and startup account.

## Examples
```powershell
Get-Service | Where-Object { $_.Status -ne 'Running' } | Select-Object Name, Status, StartType
```
