---
title: "ERROR_PASSWORD_EXPIRED (1330) - How to Fix"
description: "Fix Windows ERROR_PASSWORD_EXPIRED (1330). Resolve expired password errors, reset passwords, and configure password policies on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-1330", "password-expired", "password"]
weight: 5
---

# ERROR_PASSWORD_EXPIRED (Win32 Error 1330)

This Win32 API error occurs when a logon attempt fails because the user's password has expired. The error code is `ERROR_PASSWORD_EXPIRED` (value 1330). The full message reads:

> "The password of this user has expired."

This commonly occurs in domain environments with password expiration policies, or when local account passwords have exceeded their maximum age.

## Common Causes

- **Password expiration policy** — Domain or local policy requires periodic password changes.
- **Password age exceeded** — Password has been in use longer than allowed.
- **Forced password change** — Admin flagged account for password reset.
- **Group Policy expiration** — GPO-enforced password aging.

## How to Fix

### Change Expired Password

```powershell
# For current user (prompts for new password)
net user $env:USERNAME *
```

### Reset Password via Active Directory

```powershell
Set-ADAccountPassword -Identity "username" -Reset -NewPassword (ConvertTo-SecureString "NewSecurePassword123!" -AsPlainText -Force)
```

### Change Password via GUI

1. Press **Ctrl+Alt+Delete**.
2. Select **Change a password**.
3. Enter old and new passwords.

### Check Password Expiration Date

```powershell
Get-ADUser -Identity "username" -Properties PasswordLastSet, PasswordExpired, PasswordNeverExpires | Select-Object Name, PasswordLastSet, PasswordExpired, PasswordNeverExpires
```

### Set Password to Never Expire

```powershell
Set-ADUser -Identity "username" -PasswordNeverExpires $true
```

### Check Password Policy

```powershell
Get-ADDefaultDomainPasswordPolicy | Select-Object MaxPasswordAge, MinPasswordAge, PasswordHistoryCount
```

### Extend Password Expiry

```powershell
$user = Get-ADUser -Identity "username" -Properties PasswordLastSet
$newDate = (Get-Date).AddDays(30)
Set-ADUser -Identity "username" -Replace @{PasswordLastSet = $newDate.ToFileTime()}
```

### Unlock Account After Password Change

```powershell
Unlock-ADAccount -Identity "username"
```

### Reset Local Account Password

```cmd
net user username NewPassword123!
```

## Related Errors

- [ERROR_LOGON_FAILURE (1326)]({{< relref "/os/windows/win32-logon-failure" >}}) — Incorrect credentials
- [ERROR_ACCOUNT_DISABLED (1331)]({{< relref "/os/windows/win32-account-disabled" >}}) — Account is disabled
- [Access Denied (ERROR_ACCESS_DENIED)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Permission denied
