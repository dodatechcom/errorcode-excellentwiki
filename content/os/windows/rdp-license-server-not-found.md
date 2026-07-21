---
title: "[Solution] RDP License Server Not Found Error Fix"
description: "Fix Remote Desktop license server not found error on Windows. Resolve RDS licensing failures and terminal server client connection issues."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] RDP License Server Not Found Error Fix

The Remote Desktop license server not found error means the RD Session Host cannot locate a valid license server to issue client access licenses (CALs).

## Common Causes
- RD Licensing service not installed or not running
- License server not configured on the RD Session Host
- License server not activated with Microsoft
- Firewall blocking port 135 to the license server
- Group Policy not pointing to the correct license server

## How to Fix

### Solution 1: Install RD Licensing Role

```powershell
Install-WindowsFeature RDS-Licensing -IncludeManagementTools
```

### Solution 2: Configure License Server

Open RD Licensing Manager and add your license server to the RD Session Host configuration.

### Solution 3: Activate the License Server

Open RD Licensing Manager, right-click the server, and select Activate Server. Follow the activation wizard.

### Solution 4: Configure Licensing Mode

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\RCM\LicensingMode" /t REG_DWORD /d 4 /f
```

### Solution 5: Check Firewall Rules

```powershell
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```

## Examples
```powershell
Get-WindowsFeature RDS-Licensing | Select-Object Name, Installed
```
