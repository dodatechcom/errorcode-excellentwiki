---
title: "[Solution] Windows Firewall Connection Rejected Blocked Fix"
description: "Fix Windows Defender Firewall rejecting connections when the firewall is actively blocking network traffic on Windows. Resolve inbound connection blocks."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Firewall Connection Rejected Blocked Fix

Windows Firewall connection rejected errors occur when the firewall actively blocks inbound connections. The system drops packets silently or returns connection refused errors.

## Common Causes
- Default inbound policy set to Block
- No allow rule exists for the application or port
- Windows Firewall profile changed to Public with strict rules
- Third-party firewall software conflicting with Windows Firewall
- Rule order placing deny rules before allow rules

## How to Fix

### Solution 1: Check Default Inbound Policy

```powershell
Get-NetFirewallProfile | Select-Object Name, DefaultInboundAction, DefaultOutboundAction
```

### Solution 2: Set Default to Allow for Private Networks

```powershell
Set-NetFirewallProfile -Profile Private -DefaultInboundAction Allow
```

### Solution 3: Create Specific Allow Rules

```powershell
New-NetFirewallRule -DisplayName "Allow RDP" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Allow -Profile Domain,Private
```

### Solution 4: Check for Blocking Rules

```powershell
Get-NetFirewallRule -Direction Inbound -Action Block | Select-Object DisplayName, Enabled, Profile
```

### Solution 5: Reset Firewall to Defaults

```cmd
netsh advfirewall reset
```

## Examples
```powershell
Get-NetFirewallProfile | Select-Object Name, DefaultInboundAction, DefaultOutboundAction, Enabled
```
