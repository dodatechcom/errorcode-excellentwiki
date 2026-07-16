---
title: "[Solution] PowerShell PSRemoting Error Fix"
description: "Fix 'PSRemoting' errors when PowerShell cannot establish or maintain remote sessions."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["PSRemoting", "remote", "winrm"]
weight: 5
---

# PowerShell PSRemoting Error Fix

This error occurs when PowerShell fails to create or manage a remote session using WS-Man/WinRM. The error message reads: `PSRemotingTransportException: The connection to remote server was closed with the following error message` or `PSRemotingTransportException: An error occurred while establishing a connection to the server.`

## Description

PowerShell remoting uses Windows Remote Management (WinRM) to execute commands on remote computers. A `PSRemotingTransportException` indicates a transport-level failure — the connection couldn't be established, was rejected, or was interrupted during communication.

## Common Causes

- **WinRM not configured** — the remote machine doesn't have WinRM enabled or properly configured.
- **Network connectivity issues** — firewall blocks port 5985 (HTTP) or 5986 (HTTPS).
- **Authentication failure** — credentials don't have permission to access the remote machine.
- **WSMan configuration mismatch** — trusted hosts list or certificate issues prevent connection.

## How to Fix

### Fix 1: Enable WinRM on the remote machine

```powershell
# Enable WinRM with default settings (requires admin)
Enable-PSRemoting -Force

# Or configure manually
winrm quickconfig

# Verify WinRM is running
Get-Service WinRM
```

### Fix 2: Configure trusted hosts

```powershell
# View current trusted hosts
Get-Item WSMan:\localhost\Client\TrustedHosts

# Add a specific machine
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "Server01" -Force

# Add multiple machines
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "Server01,Server02,192.168.1.*" -Force

# Or use * to trust all (less secure)
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*" -Force
```

### Fix 3: Test the connection before running commands

```powershell
# Test WSMan connectivity
Test-WSMan -ComputerName "Server01"

# Test with credentials
Test-WSMan -ComputerName "Server01" -Credential (Get-Credential)

# Quick remoting test
Test-Connection -ComputerName "Server01" -Count 1
```

### Fix 4: Use alternative remoting options

```powershell
# Use SSH transport instead of WinRM (PowerShell 7+)
New-PSSession -HostName "user@server" -SSHTransport

# Use -Authentication with appropriate method
New-PSSession -ComputerName "Server01" -Authentication Kerberos

# Bypass SSL certificate check (temporary troubleshooting)
$sessionOption = New-PSSessionOption -SkipCACheck -SkipCNCheck
New-PSSession -ComputerName "Server01" -SessionOption $sessionOption -UseSSL
```

## Examples

```powershell
PS> Invoke-Command -ComputerName "Server01" -ScriptBlock { Get-Process }
PSRemotingTransportException: The connection to remote server was closed...

PS> New-PSSession -ComputerName "Server01"
New-PSSession: An error occurred while establishing a connection to the server.

PS> Test-WSMan -ComputerName "Server01"
Test-WSMan: The client cannot connect to the destination specified in the request.
```

## Related Errors

- [CredentialError](credential-error.md) — authentication failure for remote session.
- [ConnectionError](connection-error.md) — WinRM connection failure.
- [UnauthorizedAccess](unauthorized-access.md) — permission denied for remote operations.
