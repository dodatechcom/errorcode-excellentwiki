---
title: "[Solution] PowerShell Remoting Trusted Host Error Fix"
description: "Fix PowerShell remoting error about trusted host configuration on Windows. Resolve WinRM trusted host restrictions for remote PowerShell sessions."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] PowerShell Remoting Trusted Host Error Fix

PowerShell remoting fails when the target computer is not configured as a trusted host. WinRM refuses to connect to machines not in the trusted host list for security reasons.

## Common Causes
- Target computer not in the TrustedHosts list
- Workgroup environment without domain trust
- WinRM not configured for remote management
- Firewall blocking WinRM ports 5985 and 5986
- Authentication method mismatch between client and server

## How to Fix

### Solution 1: Add to TrustedHosts

```powershell
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "ServerName" -Force
```

### Solution 2: Add Multiple Trusted Hosts

```powershell
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "Server1,Server2,192.168.1.*" -Force
```

### Solution 3: Use -Credential with Remoting

```powershell
Enter-PSSession -ComputerName ServerName -Credential (Get-Credential)
```

### Solution 4: Enable WinRM

```cmd
winrm quickconfig
```

### Solution 5: Configure HTTPS for WinRM

```powershell
New-Item -Path WSMan:\localhost\Listener -Transport HTTPS -Address * -CertificateThumbprint (Get-ChildItem Cert:\LocalMachine\My | Select-Object -First 1).Thumbprint
```

## Examples
```powershell
Get-Item WSMan:\localhost\Client\TrustedHosts
Test-WSMan -ComputerName ServerName
```
