---
title: "[Solution] PowerShell PSCredentialError — Credential Failed"
description: "Fix PowerShell credential errors when authentication fails, credentials are rejected, or Get-Credential prompts fail."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell PSCredentialError — Credential Failed Fix

Credential errors occur when PowerShell cannot authenticate with provided credentials. Messages include `Logon failure: unknown user name or bad password` or `The server rejected the client credentials.`

## What This Error Means

PowerShell uses `PSCredential` objects to pass authentication to remote systems, APIs, and services. Failures indicate incorrect credentials, expired passwords, account lockout, or authentication protocol mismatch.

## Common Causes

- Incorrect username or password
- Account locked out or disabled
- Password recently changed
- Domain vs local account confusion
- NTLM vs Kerberos authentication mismatch
- Account requires MFA (not supported by basic auth)

## How to Fix

### 1. Create proper PSCredential object

```powershell
# Create credentials properly
$cred = Get-Credential
# Or explicitly:
$cred = [PSCredential]::new("DOMAIN\username",
    (ConvertTo-SecureString "password" -AsPlainText -Force))
```

### 2. Test credentials

```powershell
# Test authentication
$cred = Get-Credential
$session = New-PSSession -ComputerName server -Credential $cred
if ($session) { Write-Host "Authentication successful" }
```

### 3. Check account status

```powershell
# On the domain controller or local machine
Get-ADUser username -Properties LockedOut, Enabled, PasswordExpired
```

### 4. Use explicit domain

```powershell
# Include domain in username
$cred = [PSCredential]::new("DOMAIN\username", $password)

# Or UPN format
$cred = [PSCredential]::new("username@domain.com", $password)
```

## Related Errors

- [Remote Error](powershell-remote-error) — remote connection failures
- [Connection Error](connection-error) — network connectivity issues
- [Unauthorized Access](unauthorized-access) — permission errors
