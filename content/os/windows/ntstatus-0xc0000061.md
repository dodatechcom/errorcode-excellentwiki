---
title: "[Solution] NTSTATUS STATUS_PRIVILEGE_NOT_HELD Fix"
description: "Fix NTSTATUS STATUS_PRIVILEGE_NOT_HELD error on Windows when the caller does not have the required privilege for an operation."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] NTSTATUS STATUS_PRIVILEGE_NOT_HELD Fix

The NTSTATUS STATUS_PRIVILEGE_NOT_HELD (0xC0000061) error means the calling process does not possess the privilege required to perform the requested operation. Windows enforces strict privilege checks for administrative operations.

## Common Causes
- User account is not a member of the required administrative group
- User Account Control (UAC) blocking elevation
- Group Policy restricting privilege assignments
- The required privilege has not been granted in Local Security Policy
- Service running under a low-privilege account attempting administrative tasks

## How to Fix

### Solution 1: Run as Administrator

Right-click the application and select Run as administrator.

### Solution 2: Add User to Administrators Group

```powershell
Add-LocalGroupMember -Group "Administrators" -Member "DOMAIN\username"
```

### Solution 3: Grant Required Privilege via Group Policy

1. Open secpol.msc
2. Navigate to Local Policies > User Rights Assignment
3. Find the required privilege and add your user account

### Solution 4: Disable UAC for Testing

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f
```

Restart after making this change. Re-enable UAC after testing.

### Solution 5: Configure Service Account

If a service encounters this error, change its logon account to one with the necessary privileges in Services console.

## Examples
```powershell
whoami /priv
Get-LocalGroupMember -Group "Administrators"
```
