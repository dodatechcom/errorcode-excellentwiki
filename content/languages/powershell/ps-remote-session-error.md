---
title: "[Solution] PowerShell PSSession Creation Failed Error Fix"
description: "Fix PowerShell remote session creation failures. Learn why PSSession errors occur and how to configure remoting correctly."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A PowerShell PSSession error occurs when `New-PSSession`, `Enter-PSSession`, or `Invoke-Command` fails to create a remote session. This involves the WinRM (Windows Remote Management) service, which PowerShell uses for remoting. Common errors include connection refused, authentication failure, and configuration issues.

## Why It Happens

- WinRM service is not running on the remote machine
- The remote machine is not configured for PowerShell remoting
- Firewall blocks WinRM ports (5985 HTTP, 5986 HTTPS)
- Authentication fails due to wrong credentials or Kerberos/NTLM issues
- TrustedHosts does not include the target machine
- The remote machine is in a different domain without trust
- SSL certificate issues for HTTPS remoting

## How to Fix It

### Enable PowerShell remoting on the target

```powershell
# WRONG: Assuming remoting is enabled
Enter-PSSession -ComputerName Server01  # connection refused

# CORRECT: Enable remoting on the target (run as admin)
Enable-PSRemoting -Force

# Verify WinRM is running
Get-Service WinRM
```

### Configure trusted hosts for workgroup environments

```powershell
# WRONG: Not setting trusted hosts for non-domain machines
Enter-PSSession -ComputerName "192.168.1.10"  # fails

# CORRECT: Add to trusted hosts
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "192.168.1.10" -Force

# Or allow all trusted hosts (less secure)
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*" -Force
```

### Test connectivity before creating sessions

```powershell
# CORRECT: Test WinRM connectivity
Test-WSMan -ComputerName Server01

# If it fails, check firewall
Test-NetConnection -ComputerName Server01 -Port 5985

# For HTTPS
Test-NetConnection -ComputerName Server01 -Port 5986
```

### Use correct authentication method

```powershell
# WRONG: Using wrong authentication for the environment
Enter-PSSession -ComputerName Server01 -Credential (Get-Credential)

# CORRECT: Specify authentication explicitly
# For domain environments
Enter-PSSession -ComputerName Server01 -Credential (Get-Credential) -Authentication Kerberos

# For workgroup
Enter-PSSession -ComputerName Server01 -Credential (Get-Credential) -Authentication Negotiate

# For local machine
Enter-PSSession -ComputerName localhost -Authentication CredSSP
```

### Use SSH as an alternative transport

```powershell
# CORRECT: Use SSH transport for cross-platform remoting
# Requires OpenSSH on both machines
New-PSSession -HostName user@remotehost -SSHTransport

# For Windows with OpenSSH installed
New-PSSession -HostName remotehost -SSHTransport -Credential (Get-Credential)
```

### Handle session reliability

```powershell
# CORRECT: Create sessions with reliability options
$sessionOptions = New-PSSessionOption -OperationTimeout 30000 -IdleTimeout 60000
$session = New-PSSession -ComputerName Server01 -SessionOption $sessionOptions

# Reconnect on failure
try {
    Invoke-Command -Session $session -ScriptBlock { Get-Date }
} catch {
    Write-Warning "Session failed, reconnecting..."
    $session = New-PSSession -ComputerName Server01
    Invoke-Command -Session $session -ScriptBlock { Get-Date }
}
```

## Common Mistakes

- Not enabling WinRM before attempting remote connections
- Forgetting that workgroup environments require TrustedHosts configuration
- Using `-ComputerName localhost` without enabling local remoting
- Not checking that the WinRM firewall exception is enabled
- Assuming that domain credentials automatically work for remoting

## Related Pages

- [PowerShell Remote Error](ps-remote-session-error) - remote session issues
- [PowerShell Unauthorized Access](ps-unauthorized-access-v2) - access denied
- [PowerShell Job Error](ps-job-error) - background job failed
- [PowerShell DSC Error](ps-dsc-error) - DSC configuration failed
