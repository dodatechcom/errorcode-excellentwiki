---
title: "[Solution] Windows Defender Real-Time Protection Disabled Fix"
description: "Fix Windows Defender real-time protection that is turned off and cannot be re-enabled on Windows. Resolve Defender protection errors on Windows 10/11."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Defender Real-Time Protection Disabled Fix

Windows Defender real-time protection may be disabled by Group Policy, third-party software, or system corruption. When disabled the system is vulnerable to malware.

## Common Causes
- Group Policy disabling Defender real-time protection
- Third-party antivirus disabling Defender automatically
- Registry key forcing Defender off
- Windows Security Center reporting stale status
- Tamper Protection blocking configuration changes

## How to Fix

### Solution 1: Check Registry Settings

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" -ErrorAction SilentlyContinue
```

### Solution 2: Enable via Group Policy

Open gpedit.msc and navigate to Computer Configuration > Administrative Templates > Windows Defender Antivirus. Ensure Turn off Windows Defender Antivirus is set to Disabled.

### Solution 3: Restart Defender Service

```powershell
Restart-Service -Name WinDefend -Force
```

### Solution 4: Run Windows Security Troubleshooter

Go to Settings > System > Troubleshoot and run the Windows Security troubleshooter.

### Solution 5: Check Tamper Protection

Open Windows Security > Virus & threat protection > Manage settings. Verify Tamper Protection is on.

## Examples
```powershell
Get-MpPreference | Select-Object DisableRealtimeMonitoring, DisableBehaviorMonitoring, DisableIOAVProtection
```
