---
title: "[Solution] Active Directory Domain Controller Not Found Fix"
description: "Fix Active Directory domain controller not found error on Windows. Resolve DC location failures and domain trust issues on Windows client machines."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Active Directory Domain Controller Not Found Fix

The Active Directory domain controller not found error means the client computer cannot locate a domain controller for authentication.

## Common Causes
- DNS misconfigured preventing DC location
- Network connectivity issues to DC
- DNS SRV records missing or incorrect
- Domain Controller is offline or overloaded
- Client computer clock skew exceeding Kerberos tolerance

## How to Fix

### Solution 1: Verify DNS Configuration

```cmd
nslookup -type=SRV _ldap._tcp.dc._msdcs.domain.com
```

### Solution 2: Check Domain Controller Status

```cmd
nltest /dsgetdc:domain.com
```

### Solution 3: Flush DNS and Re-register

```cmd
ipconfig /flushdns
ipconfig /registerdns
```

### Solution 4: Test Network Connectivity to DC

```cmd
Test-NetConnection -ComputerName dc01.domain.com -Port 389
Test-NetConnection -ComputerName dc01.domain.com -Port 88
```

### Solution 5: Verify Time Synchronization

```cmd
w32tm /query /status
w32tm /resync
```

## Examples
```powershell
nltest /dsgetdc:domain.com
Get-DnsClientServerAddress | Select-Object InterfaceAlias, ServerAddresses
```
