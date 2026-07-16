---
title: "[Solution] PowerShell Credential Error Fix"
description: "Fix 'Credential' errors when PowerShell cannot authenticate with provided credentials."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["credential", "authentication", "login"]
weight: 5
---

# PowerShell Credential Error Fix

This error occurs when PowerShell fails to authenticate using the provided credentials. The error message reads: `The supplied credential is invalid.` or `Logon failure: unknown user name or bad password.`

## Description

PowerShell uses credentials for accessing remote computers, network resources, databases, and APIs. A credential error indicates that the username/password combination was rejected, the account is locked, or the authentication mechanism doesn't match what the server expects.

## Common Causes

- **Incorrect username or password** — simple typo or expired password.
- **Account locked or disabled** — too many failed attempts or administrator disabled the account.
- **Domain/forest mismatch** — using a local account when a domain account is required, or vice versa.
- **Authentication protocol mismatch** — server requires NTLM but Kerberos is being used, or the credential type doesn't match.

## How to Fix

### Fix 1: Use Get-Credential properly

```powershell
# Interactive prompt — most secure
$cred = Get-Credential

# With explicit username
$cred = Get-Credential -UserName "DOMAIN\user"

# Use the credential with a cmdlet
Get-ChildItem "\\server\share" -Credential $cred
```

### Fix 2: Verify account status

```powershell
# Check if the account is locked (requires RSAT/AD module)
Get-ADUser -Identity "username" -Properties LockedOut, Enabled, PasswordExpired

# Reset password if needed (requires admin)
Set-ADAccountPassword -Identity "username" -Reset -NewPassword (ConvertTo-SecureString "NewP@ss" -AsPlainText -Force)
Unlock-ADAccount -Identity "username"
```

### Fix 3: Match authentication protocol

```powershell
# For domain authentication
$cred = Get-Credential
$session = New-PSSession -ComputerName "Server01" -Credential $cred -Authentication Kerberos

# For workgroup/local machine authentication
$cred = Get-Credential -UserName "localuser"
$session = New-PSSession -ComputerName "localhost" -Credential $cred -Authentication Basic

# Force NTLM if Kerberos fails
$session = New-PSSession -ComputerName "Server01" -Credential $cred -Authentication Negotiate
```

### Fix 4: Store and retrieve credentials securely

```powershell
# Save credential to file (encrypted)
$cred = Get-Credential
$cred | Export-Clixml -Path "$env:USERPROFILE\cred.xml"

# Retrieve later
$cred = Import-Clixml -Path "$env:USERPROFILE\cred.xml"

# Use with cmdlets
Invoke-Command -ComputerName "Server01" -Credential $cred -ScriptBlock { whoami }
```

## Examples

```powershell
PS> Invoke-Command -ComputerName "Server01" -Credential $cred -ScriptBlock { whoami }
Logon failure: unknown user name or bad password.

PS> Get-ChildItem "\\fileserver\share" -Credential $cred
Get-ChildItem: Access to the path '\\fileserver\share' is denied.

PS> Connect-AzAccount -Credential $cred
Connect-AzAccount: The supplied credential is invalid.
```

## Related Errors

- [PSRemotingError](remote-error.md) — remote session connection failure.
- [ConnectionError](connection-error.md) — WinRM connection failure.
- [UnauthorizedAccess](unauthorized-access.md) — permission denied after authentication.
