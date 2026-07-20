---
title: "[Solution] PowerShell REMOTING — WSMan Configuration Error"
description: "Fix PowerShell Remoting error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 1004
---

# [Solution] PowerShell REMOTING — WSMan Configuration Error

The PowerShell Remoting error prevents remote command execution when the WSMan (Web Services for Management) configuration is incorrect or the remoting service is not properly configured. This breaks `Invoke-Command`, `Enter-PSSession`, and other remoting operations.

## Description

PowerShell Remoting relies on Windows Remote Management (WinRM) and the WSMan provider to establish remote connections. When remoting fails, you typically see one of these error messages:

> "The WinRM client cannot process the request because the server name cannot be resolved."

> "Connecting to remote server failed with the following error message: The WinRM client cannot process the request."

> "WSManFault Message: The client cannot connect to the destination specified in the request."

## Common Causes

1. WinRM service is not running on the target machine.
2. PowerShell Remoting is not enabled.
3. Windows Firewall blocks the WinRM ports (5985/5986).
4. The target machine is not reachable over the network.
5. Kerberos authentication or double-hop delegation issues.
6. WinRM configuration is corrupted or misconfigured.
7. SSL certificate issues for HTTPS-based remoting (port 5986).

## Solutions

### Solution 1: Enable PowerShell Remoting

Enable remoting on the local machine:

```powershell
Enable-PSRemoting -Force -SkipNetworkProfileCheck
```

### Solution 2: Check and Start WinRM Service

Verify the WinRM service is running:

```powershell
Get-Service WinRM
Start-Service WinRM
Set-Service WinRM -StartupType Automatic
```

### Solution 3: Configure WinRM for HTTP Access

Allow unencrypted HTTP connections for trusted networks:

```powershell
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'
```

### Solution 4: Add Trusted Hosts

Add target machines to the trusted hosts list:

```powershell
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "ServerName" -Force

# Add multiple hosts
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "Server1,Server2,192.168.1.*" -Force
```

### Solution 5: Configure Firewall Rules

Open the required WinRM ports:

```powershell
Enable-NetFirewallRule -DisplayGroup "Windows Remote Management"
New-NetFirewallRule -DisplayName "WinRM HTTP" -Direction Inbound -Protocol TCP -LocalPort 5985 -Action Allow
New-NetFirewallRule -DisplayName "WinRM HTTPS" -Direction Inbound -Protocol TCP -LocalPort 5986 -Action Allow
```

### Solution 6: Test the Connection

Verify remoting is working:

```powershell
Test-WSMan -ComputerName "ServerName"
Test-WSMan -ComputerName "localhost"
```

### Solution 7: Reset WinRM Configuration

If the configuration is corrupted, reset it:

```powershell
Disable-PSRemoting -Force
Remove-Item WSMan:\localhost\Client\TrustedHosts -Force -ErrorAction SilentlyContinue
Enable-PSRemoting -Force
```

## Related Errors

- [PowerShell Execution Policy Error]({{< relref "/os/windows/powershell-execution-policy-error" >}}) — Scripts cannot be loaded
- [PowerShell Invoke-Command Error]({{< relref "/os/windows/powershell-invoke-command-error" >}}) — Remote execution failed
- [PowerShell DSC Error]({{< relref "/os/windows/powershell-desired-state-configuration-error" >}}) — Configuration failed
