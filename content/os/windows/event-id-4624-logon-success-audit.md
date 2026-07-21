---
title: "[Solution] Event ID 4624 Logon Audit Analysis Fix"
description: "Fix and analyze Windows Event ID 4624 successful logon audit events. Understand logon types and troubleshoot unexpected logon activity on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Event ID 4624 Logon Audit Analysis Fix

Event ID 4624 records successful logon events on Windows. Analyzing these helps identify unauthorized access and troubleshoot logon type issues.

## Common Causes
- Scheduled tasks running under user credentials
- Service accounts logging on interactively
- RDP sessions creating new logon events
- Batch jobs or scripts using stored credentials
- Network logon attempts from remote systems

## How to Fix

### Solution 1: Filter Logon Events by Type

```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -MaxEvents 100 | ForEach-Object {
    [xml]$_.ToXml()
} | Select-Object -ExpandProperty EventData
```

### Solution 2: Identify Logon Types

- Type 2: Interactive (console)
- Type 3: Network (SMB, IIS)
- Type 5: Service
- Type 7: Unlock
- Type 10: RemoteDesktop
- Type 11: Cached credentials

### Solution 3: Detect Anomalous Logons

Look for logon Type 10 from unexpected IP addresses or Type 2 at unusual hours.

### Solution 4: Enable Advanced Audit Policy

```cmd
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
```

### Solution 5: Forward to SIEM

Configure Windows Event Forwarding to send Event ID 4624 to your SIEM for centralized analysis.

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -MaxEvents 20 | ForEach-Object { [xml]$_.ToXml() } | Select-Object -ExpandProperty EventData
```
