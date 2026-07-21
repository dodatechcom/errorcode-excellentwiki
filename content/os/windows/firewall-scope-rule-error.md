---
title: "[Solution] Windows Firewall Scope Rule Error Fix"
description: "Fix Windows Defender Firewall scope rule errors when remote IP address restrictions block legitimate network traffic on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Windows Firewall Scope Rule Error Fix

Firewall scope rule errors occur when remote IP address restrictions on firewall rules incorrectly block legitimate traffic. The rule scope does not match the actual source addresses of allowed connections.

## Common Causes
- Rule scope configured for wrong IP range
- Dynamic IP addresses outside the configured scope
- VPN traffic originating from unexpected IP ranges
- NAT translation changing source IP addresses
- Group Policy scope settings conflicting with local rules

## How to Fix

### Solution 1: Check Rule Scope

```powershell
Get-NetFirewallRule -DisplayName "RuleName" | Get-NetFirewallAddressFilter | Select-Object RemoteAddress
```

### Solution 2: Update Rule Scope

```powershell
Set-NetFirewallRule -DisplayName "RuleName" -RemoteAddress 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
```

### Solution 3: Allow Any Remote Address

```powershell
Set-NetFirewallRule -DisplayName "RuleName" -RemoteAddress Any
```

### Solution 4: Add Specific VPN IP Ranges

```powershell
$rule = Get-NetFirewallRule -DisplayName "RuleName"
$scope = $rule | Get-NetFirewallAddressFilter
$newAddresses = $scope.RemoteAddress + "100.64.0.0/10"
$scope | Set-NetFirewallAddressFilter -RemoteAddress $newAddresses
```

### Solution 5: Review Group Policy Scope

```powershell
gpresult /h C:\gpreport.html
```

## Examples
```powershell
Get-NetFirewallRule -Direction Inbound | Get-NetFirewallAddressFilter | Select-Object @{N='Rule';E={$_.PSObject.Properties.Value | Select-Object -First 1}}, RemoteAddress
```
