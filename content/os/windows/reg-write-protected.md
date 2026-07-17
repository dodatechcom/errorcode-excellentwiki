---
title: "Registry is Write Protected Error - How to Fix"
description: "Fix 'Registry is write protected' errors on Windows 10 and 11. Remove write protection, enable registry modifications, and restore write access."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["registry", "write-protected", "read-only", "readonly"]
weight: 5
---

# Registry is Write Protected Error

This error occurs when you try to modify a registry key or value but the registry (or a specific key) is write-protected. The error reads:

> "Error writing value's new contents."

or

> "Registry is write protected."

This commonly appears when installing software, applying Group Policy changes, or manually editing protected registry keys.

## Common Causes

- **Registry key has read-only ACL** — Permissions deny write access.
- **Group Policy lock** — Domain policy prevents registry modifications.
- **Registry key marked read-only** — Key was explicitly set to read-only.
- **System protection** — Windows protects critical registry keys from modification.
- **Malware lock** — Malicious software has restricted registry access.

## How to Fix

### Run as Administrator

Registry modifications require elevated privileges:

```powershell
Start-Process regedit -Verb RunAs
```

### Check Write Permissions

```powershell
Get-Acl "HKLM:\SOFTWARE\YourKey" | Format-List
```

Look for `Deny` entries or missing `WriteKey` permissions.

### Enable Write Access

Add write permissions using an elevated Command Prompt:

```cmd
reg add "HKLM\SOFTWARE\YourKey" /v "ValueName" /t REG_SZ /d "data" /f
```

### Remove Read-Only Attribute with PowerShell

```powershell
$key = "HKLM:\SOFTWARE\YourKey"
$acl = Get-Acl $key
$accessRule = New-Object System.Security.AccessControl.RegistryAccessRule("Administrators", "FullControl", "Allow")
$acl.AddAccessRule($accessRule)
Set-Acl -Path $key -AclObject $acl
```

### Check Group Policy Settings

```powershell
gpresult /h "$env:USERPROFILE\Desktop\gp_report.html"
```

Open the HTML report and check for registry-related policies under **Computer Configuration > Administrative Templates > System**.

## Related Errors

- [Registry Access Denied]({{< relref "/os/windows/reg-access-denied" >}}) — General permission denial for registry
- [Registry Transaction Error]({{< relref "/os/windows/reg-transaction-error" >}}) — Transaction-level failures
- [Access Denied (ERROR_ACCESS_DENIED)]({{< relref "/os/windows/win32-access-denied-win32" >}}) — General Windows access denied
