---
title: "[Solution] Event ID 131 Registry Key Notification Fix"
description: "Fix Windows Event ID 131 registry key notification error when a registry key notification operation fails on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Event ID 131 Registry Key Notification Fix

Event ID 131 in the System log records failures in registry key notification operations. These notifications are used by applications and services to monitor changes to specific registry keys.

## Common Causes
- Too many registry notifications queued for processing
- Registry key being monitored was deleted while notification was pending
- Third-party software creating excessive registry notifications
- System resource exhaustion preventing notification delivery
- Corrupted registry key causing notification loop

## How to Fix

### Solution 1: Review the Event Details

```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=131} -MaxEvents 5 | ForEach-Object { [xml]$_.ToXml() } | Select-Object -ExpandProperty EventData
```

### Solution 2: Check for Registry Monitoring Tools

Disable or uninstall third-party registry monitoring utilities that may be creating excessive notifications.

### Solution 3: Restart Affected Services

```powershell
Get-Service | Where-Object { $_.Status -eq 'Running' } | Restart-Service -Force -ErrorAction SilentlyContinue
```

### Solution 4: Run System File Checker

```cmd
sfc /scannow
```

### Solution 5: Monitor Registry Activity

Use Process Monitor from Sysinternals to identify which processes are creating the most registry notifications.

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='System'; Id=131} -MaxEvents 10 | Format-Table TimeCreated, Message -Wrap
```
