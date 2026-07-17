---
title: "ERROR_LOGON_FAILURE (1326) - How to Fix"
description: "Fix Windows ERROR_LOGON_FAILURE (1326). Resolve authentication failures, fix incorrect credentials, and troubleshoot login problems on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-1326", "logon-failure", "authentication"]
weight: 5
---

# ERROR_LOGON_FAILURE (Win32 Error 1326)

This Win32 API error occurs when a logon attempt fails due to incorrect credentials. The error code is `ERROR_LOGON_FAILURE` (value 1326). The full message reads:

> "The user name or password is incorrect."

This is one of the most common authentication errors, appearing during domain logons, service account authentication, and remote connections.

## Common Causes

- **Wrong username or password** — Typo or outdated credentials.
- **Account locked out** — Too many failed attempts locked the account.
- **Password changed** — Password was changed but cached credentials are stale.
- **Wrong domain** — Attempting to log on to wrong domain.
- **Caps Lock enabled** — Password typed with wrong case.
- **Account disabled** — User account is administratively disabled.

## How to Fix

### Verify Credentials

```powershell
$cred = Get-Credential
$result = whoami /all
```

### Test Authentication

```powershell
# Test local authentication
$identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
Write-Host "Logged in as: $($identity.Name)"
```

### Check Account Lockout Status

```cmd
net accounts
```

Or for specific user:

```powershell
Search-ADAccount -LockedOut | Select-Object Name, LockedOut, LastLogonDate
```

### Unlock Account

```powershell
Unlock-ADAccount -Identity "username"
```

### Reset Password

```powershell
Set-ADAccountPassword -Identity "username" -Reset -NewPassword (ConvertTo-SecureString "NewPassword" -AsPlainText -Force)
```

### Test Network Authentication

```powershell
Test-NetConnection -ComputerName "ServerName" -Port 445
```

### Check Stored Credentials

```cmd
rundll32.exe keymgr.dll, KRKeymgr
```

### Clear Cached Credentials

```cmd
cmdkey /list
cmdkey /delete:target_name
```

### Verify Domain Connectivity

```cmd
nltest /dsgetdc:domainname
echo %LOGONSERVER%
```

## Related Errors

- [ERROR_ACCOUNT_DISABLED (1331)]({{< relref "/os/windows/win32-account-disabled" >}}) — Account is disabled
- [ERROR_PASSWORD_EXPIRED (1330)]({{< relref "/os/windows/win32-password-expired" >}}) — Password has expired
- [ERROR_ACCESS_DENIED (5)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Access denied after authentication
