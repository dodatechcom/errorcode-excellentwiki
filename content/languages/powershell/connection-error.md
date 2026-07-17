---
title: "[Solution] PowerShell WinRM Connection Error Fix"
description: "Fix 'WinRM connection error' when PowerShell cannot connect to a remote WinRM service."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell WinRM Connection Error Fix

This error occurs when PowerShell cannot establish a network connection to the WinRM service on a remote machine. The error message reads: `WSMan fault: The client cannot connect to the destination specified in the request.` or `WinRM cannot process the request.`

## Description

WinRM (Windows Remote Management) is the underlying transport for PowerShell remoting. A connection error indicates that the network-level connection to the WinRM service (port 5985/5986) failed. This is a different issue from authentication — the server simply can't be reached or isn't responding.

## Common Causes

- **WinRM service not running** — the remote machine's WinRM service is stopped or disabled.
- **Firewall blocking ports** — port 5985 (HTTP) or 5986 (HTTPS) is blocked by a firewall.
- **DNS resolution failure** — the hostname cannot be resolved to an IP address.
- **Network unreachable** — the remote machine is offline or on a different network segment.

## How to Fix

### Fix 1: Verify WinRM service status on remote machine

```powershell
# Check WinRM service locally
Get-Service WinRM

# Start WinRM if stopped
Start-Service WinRM

# Set WinRM to start automatically
Set-Service WinRM -StartupType Automatic
```

### Fix 2: Test network connectivity

```powershell
# Test basic connectivity
Test-Connection -ComputerName "Server01" -Count 3

# Test WinRM port specifically
Test-NetConnection -ComputerName "Server01" -Port 5985

# Test HTTPS port
Test-NetConnection -ComputerName "Server01" -Port 5986
```

### Fix 3: Configure Windows Firewall

```powershell
# Enable WinRM firewall rules (requires admin)
Enable-NetFirewallRule -DisplayGroup "Windows Remote Management"

# Or create a custom rule
New-NetFirewallRule -DisplayName "WinRM HTTP" `
    -Direction Inbound -Protocol TCP -LocalPort 5985 `
    -Action Allow -Profile Domain,Private

New-NetFirewallRule -DisplayName "WinRM HTTPS" `
    -Direction Inbound -Protocol TCP -LocalPort 5986 `
    -Action Allow -Profile Domain,Private
```

### Fix 4: Configure WinRM listener

```powershell
# Create a WinRM listener for HTTP
winrm create winrm/config/Listener?Address=*+Transport=HTTP

# Create a WinRM listener for HTTPS (requires certificate)
winrm create winrm/config/Listener?Address=*+Transport=HTTPS `
    @{Hostname="Server01"; CertificateThumbprint="THUMBPRINT"}

# List current listeners
winrm enumerate winrm/config/Listener
```

## Examples

```powershell
PS> Enter-PSSession -ComputerName "Server01"
Enter-PSSession: Connecting to remote server Server01 failed with the following error message: The client cannot connect to the destination specified in the request.

PS> Invoke-Command -ComputerName "Server01" -ScriptBlock { Get-Date }
Invoke-Command: Connecting to remote server Server01 failed with the following error message: WinRM cannot process the request.

PS> Test-NetConnection -ComputerName "Server01" -Port 5985
ComputerName     : Server01
RemotePort       : 5985
TcpTestSucceeded : False
```

## Related Errors

- [PSRemotingError](remote-error.md) — PSRemoting transport failure.
- [CredentialError](credential-error.md) — authentication failure after connection.
- [UnauthorizedAccess](unauthorized-access.md) — permission denied for operations.
