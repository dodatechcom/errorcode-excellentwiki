---
title: "[Solution] Windows Defender Unauthorized Changes Blocked Fix"
description: "Fix Windows Defender notification that unauthorized changes are being blocked on Windows. Resolve Defender tamper protection and configuration issues."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Defender Unauthorized Changes Blocked Fix

Windows Defender shows unauthorized changes blocked when Tamper Protection or Controlled Folder Access prevents modifications to Defender settings or protected files.

## Common Causes
- Tamper Protection preventing registry changes to Defender
- Controlled Folder Access blocking application writes
- Third-party software attempting to disable Defender
- Group Policy changes conflicting with local settings
- Malware attempting to modify Defender configuration

## How to Fix

### Solution 1: Temporarily Disable Tamper Protection

Open Windows Security > Virus & threat protection > Manage settings. Toggle Tamper Protection off temporarily.

### Solution 2: Add Applications to Controlled Folder Access Allow List

```powershell
Add-MpPreference -ControlledFolderAccessAllowedApplications "C:\Path\To\app.exe"
```

### Solution 3: Check Controlled Folder Access

```powershell
Get-MpPreference | Select-Object EnableControlledFolderAccess, ControlledFolderAccessAllowedApplications
```

### Solution 4: Review Defender Event Log

```powershell
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Windows Defender/Operational'; Id=1123} -MaxEvents 10 | Format-Table TimeCreated, Message -Wrap
```

### Solution 5: Reset Defender Settings

```powershell
Set-MpPreference -DisableRealtimeMonitoring $false
```

## Examples
```powershell
Get-MpPreference | Select-Object EnableControlledFolderAccess, EnableNetworkProtection
```
