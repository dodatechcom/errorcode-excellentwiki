---
title: "ERROR_ACCESS_DENIED (5) - How to Fix"
description: "Fix Windows ERROR_ACCESS_DENIED (5). Resolve permission issues, UAC restrictions, and access control problems on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["win32", "error-5", "access-denied", "permissions"]
weight: 5
---

# ERROR_ACCESS_DENIED (Win32 Error 5)

This Win32 API error occurs when the system denies access to a resource. The error code is `ERROR_ACCESS_DENIED` (value 5). The full message reads:

> "Access is denied."

This is one of the most common Windows errors, appearing when trying to access files, folders, registry keys, services, or processes without sufficient permissions.

## Common Causes

- **Insufficient user permissions** — Account lacks required access rights.
- **UAC elevation needed** — Operation requires administrator privileges.
- **File/folder ownership** — Resource owned by SYSTEM or another user.
- **Antivirus blocking** — Security software prevents access.
- **Group Policy restrictions** — Domain policy denies the operation.

## How to Fix

### Run as Administrator

Right-click the application and select **Run as administrator**, or:

```powershell
Start-Process "app.exe" -Verb RunAs
```

### Take Ownership of File/Folder

```cmd
takeown /f "C:\Path\To\file" /a
icacls "C:\Path\To\file" /grant Administrators:F
```

### Check Current Permissions

```powershell
Get-Acl "C:\Path\To\file" | Format-List
```

### Grant Full Control

```cmd
icacls "C:\Path\To\file" /grant %USERNAME%:F /t
```

### Check Service Permissions

```powershell
sc.exe sdshow "ServiceName"
```

### Modify Service Permissions

```cmd
sc.exe sdset "ServiceName" "D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)"
```

### Check Effective Access

```powershell
Get-Acl "C:\Path\To\file" | Format-List Access
```

## Related Errors

- [Registry Access Denied]({{< relref "/os/windows/reg-access-denied" >}}) — Registry-specific access denial
- [COM Access Denied]({{< relref "/os/windows/com-access-denied" >}}) — COM object access denial
- [ERROR_ACCESS_DENIED Win32]({{< relref "/os/windows/win32-access-denied-win32" >}}) — General access denied
