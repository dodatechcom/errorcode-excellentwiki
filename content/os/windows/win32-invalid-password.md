---
title: "[Solution] Error 86 — INVALID_PASSWORD Fix"
description: "Fix Windows Error Code (INVALID_PASSWORD) with these step-by-step solutions. Includes copy-paste commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 86
---

# [Solution] Error 86 — INVALID_PASSWORD Fix

Win32 error 86 (`ERROR_INVALID_PASSWORD`) occurs when the specified network password is not correct. This error typically appears when connecting to network shares, remote servers, or authenticated services.

## Description

The INVALID_PASSWORD error is returned when authentication fails because the password provided does not match the expected credentials. This commonly occurs during network drive mapping, remote desktop connections, and API calls to authenticated services. The error code is `ERROR_INVALID_PASSWORD` (value 86). The full message reads:

> "The specified network password is not correct."

## Common Causes

1. The password was typed incorrectly.
2. The account password was changed but the cached credential is stale.
3. Caps Lock or Num Lock is enabled, causing incorrect input.
4. The stored Windows credential is outdated or corrupted.
5. The account is locked out after too many failed attempts.
6. The password has expired and needs to be reset.

## Solutions

### Solution 1: Verify the Password

Retype the password carefully, ensuring correct case and special characters:

```powershell
# Test credentials by connecting to the resource
$cred = Get-Credential
Test-Path "\\Server\Share" -Credential $cred
```

### Solution 2: Reset Stored Credentials

Remove and re-add the saved credential in Windows Credential Manager:

```cmd
:: Delete stored credential
cmdkey /delete:TargetName

:: Add new credential
cmdkey /generic:TargetName /user:DOMAIN\Username /pass:NewPassword
```

Or via PowerShell:

```powershell
# Remove stored network credentials
cmdkey /delete:Domain:target=Server
```

### Solution 3: Check Caps Lock

Verify Caps Lock and Num Lock are in the correct state before entering the password. Also check for keyboard layout differences:

```powershell
# Check current keyboard layout
Get-WinUserLanguageList
```

### Solution 4: Reset Network Drive Credentials

Remove and re-map the network drive with correct credentials:

```cmd
:: Remove existing mapped drive
net use Z: /delete

:: Re-map with new credentials
net use Z: \\Server\Share /user:DOMAIN\Username password
```

### Solution 5: Reset Account Password

If the account is locked or the password needs resetting:

```powershell
# Reset password via Active Directory (requires admin)
Set-ADAccountPassword -Identity "Username" -Reset -NewPassword (ConvertTo-SecureString "NewP@ssw0rd" -AsPlainText -Force)
Unlock-ADAccount -Identity "Username"
```

## Related Errors

- [Error 1326 — LOGON_FAILURE]({{< relref "/os/windows/win32-logon-failure" >}}) — User name or password is incorrect
- [Error 1325 — ACCOUNT_DISABLED]({{< relref "/os/windows/win32-account-disabled" >}}) — Account is disabled
- [Error 1398 — PASSWORD_EXPIRED]({{< relref "/os/windows/win32-password-expired" >}}) — Password has expired
