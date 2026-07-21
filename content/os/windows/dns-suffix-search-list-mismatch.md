---
title: "[Solution] DNS Suffix Search List Mismatch Error Fix"
description: "Fix DNS suffix search list mismatch errors on Windows when domain suffixes are not configured correctly for name resolution."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] DNS Suffix Search List Mismatch Error Fix

DNS suffix search list mismatches cause name resolution failures when the system appends incorrect or missing suffixes to unqualified hostnames. This prevents access to internal resources using short names.

## Common Causes
- DHCP not providing the correct DNS suffix
- Group Policy DNS suffix configuration conflicting with DHCP
- Manual DNS configuration missing the search suffix
- Multiple network adapters with different DNS suffixes
- VPN connection overriding the local DNS suffix

## How to Fix

### Solution 1: Check Current DNS Suffix

```powershell
Get-DnsClientGlobalSetting | Select-Object SuffixSearchList
```

### Solution 2: Set DNS Suffix via PowerShell

```powershell
Set-DnsClientGlobalSetting -SuffixSearchList @("domain.com","sub.domain.com")
```

### Solution 3: Configure via Network Adapter Properties

1. Open Network Connections
2. Right-click adapter > Properties
3. Select IPv4 > Properties > Advanced > DNS
4. Add the correct DNS suffix

### Solution 4: Check DHCP DNS Registration

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, ServerAddresses
ipconfig /all
```

### Solution 5: Configure via Group Policy

Open gpedit.msc and navigate to Computer Configuration > Administrative Templates > Network > DNS Client and configure the DNS suffix search list.

## Examples
```powershell
Get-DnsClientGlobalSetting
ipconfig /all | Select-String "DNS Suffix"
```
