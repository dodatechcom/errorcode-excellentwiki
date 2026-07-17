---
title: "ERROR_ACCOUNT_DISABLED (1331) - How to Fix"
description: "Fix Windows ERROR_ACCOUNT_DISABLED (1331). Enable disabled user accounts, resolve account status issues, and restore access on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-1331", "account-disabled", "account"]
weight: 5
---

# ERROR_ACCOUNT_DISABLED (Win32 Error 1331)

This Win32 API error occurs when a logon attempt is made with an account that has been disabled. The error code is `ERROR_ACCOUNT_DISABLED` (value 1331). The full message reads:

> "This user can't sign in because this account is currently disabled."

Accounts can be disabled by administrators, by Group Policy, or automatically after inactivity.

## Common Causes

- **Administratively disabled** — Admin explicitly disabled the account.
- **Inactivity auto-disable** — Account unused for extended period.
- **Group Policy disable** — Domain policy disables the account.
- **Security lockout** — Account disabled due to security incident.
- **Test/dev account cleanup** — Temporary account was cleaned up.

## How to Fix

### Check Account Status

```powershell
Get-ADUser -Identity "username" -Properties Enabled, LastLogonDate, Description | Select-Object Name, Enabled, LastLogonDate
```

### Enable Account via Active Directory

```powershell
Enable-ADAccount -Identity "username"
```

### Enable Local Account

```powershell
Enable-LocalUser -Name "username"
```

### Check Using net User

```cmd
net user username
```

### Enable via Local Users and Groups GUI

1. Press **Win+R**, type `lusrmgr.msc`.
2. Navigate to **Users**.
3. Right-click the disabled account.
4. Select **Properties**.
5. Uncheck **Account is disabled**.
6. Click **OK**.

### Check Group Policy for Auto-Disable

```powershell
gpresult /h "$env:USERPROFILE\Desktop\gp_report.html"
```

Look for account policy settings under **Computer Configuration > Windows Settings > Security Settings > Account Policies**.

### Re-enable via PowerShell Script

```powershell
$disabledUsers = Search-ADAccount -Disabled | Where-Object { $_.Enabled -eq $false }
foreach ($user in $disabledUsers) {
    Enable-ADAccount -Identity $user.SamAccountName
    Write-Host "Enabled: $($user.SamAccountName)"
}
```

### Check Account Expiration

```powershell
Get-ADUser -Identity "username" -Properties AccountExpirationDate, AccountNotDelegated
```

## Related Errors

- [ERROR_LOGON_FAILURE (1326)]({{< relref "/os/windows/win32-logon-failure" >}}) — Incorrect credentials
- [ERROR_PASSWORD_EXPIRED (1330)]({{< relref "/os/windows/win32-password-expired" >}}) — Password expired
- [Access Denied (ERROR_ACCESS_DENIED)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — Permission denied
