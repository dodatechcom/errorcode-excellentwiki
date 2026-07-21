---
title: "[Solution] Windows Firewall Blocking Unlisted Application Fix"
description: "Fix Windows Defender Firewall blocking an application that does not appear in the allowed apps list. Resolve firewall rules for unrecognized programs."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Firewall Blocking Unlisted Application Fix

Windows Firewall may block applications that are not present in the allowed apps list. This affects custom-built applications, portable tools, and recently installed software.

## Common Causes
- Application does not register itself with Windows Firewall API
- Windows Firewall profile changes resetting custom rules
- Application changed its executable path after an update
- Firewall running in block-all mode for the network profile
- Group Policy overriding local firewall rules

## How to Fix

### Solution 1: Add Application to Firewall Allow List

```powershell
New-NetFirewallRule -DisplayName "My App" -Direction Inbound -Program "C:\Path\To\app.exe" -Action Allow -Profile Domain,Private,Public
```

### Solution 2: Allow by Port

```powershell
New-NetFirewallRule -DisplayName "App Port" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow
```

### Solution 3: Allow Through GUI

1. Open Windows Defender Firewall > Allow an app through firewall
2. Click Change settings > Allow another app
3. Browse to the application executable

### Solution 4: Check Current Firewall Rules

```powershell
Get-NetFirewallRule -DisplayName "*MyApp*" | Select-Object DisplayName, Enabled, Direction, Action
```

### Solution 5: Verify Network Profile

```powershell
Get-NetConnectionProfile | Select-Object Name, NetworkCategory
```

## Examples
```powershell
Get-NetFirewallRule -Direction Inbound -Action Allow | Select-Object DisplayName, Enabled | Sort-Object DisplayName
```
