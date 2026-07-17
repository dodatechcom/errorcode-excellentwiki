---
title: "[Solution] HRESULT E_ACCESSDENIED (0x80070005) — Access Denied"
description: "Fix Windows HRESULT E_ACCESSDENIED (0x80070005) access denied error. Causes and solutions for permission failures in COM operations."
platforms: ["windows"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HRESULT E_ACCESSDENIED (0x80070005) — Access Denied

**Error Code:** `0x80070005`

E_ACCESSDENIED indicates that the requested operation requires elevated privileges or the caller lacks necessary permissions to access the resource.

## What This Error Means

This HRESULT code maps to the Win32 error `ERROR_ACCESS_DENIED`. The calling process does not have the required security context to perform the requested operation.

## Common Causes

- Insufficient user account privileges for the operation
- UAC (User Account Control) blocking elevated operations
- File or registry key ACL restrictions preventing access
- Services or COM objects requiring administrator privileges

## How to Fix

### Run as Administrator

Right-click the application and select **Run as administrator** to provide elevated privileges.

### Take Ownership of Files/Folders

```cmd
takeown /f "C:\path\to\file" /a
icacls "C:\path\to\file" /grant administrators:F
```

### Enable Built-in Administrator Account

```cmd
net user Administrator /active:yes
```

### Modify Registry Permissions

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```

## Related Errors

- [E_FAIL (0x80004005)]({{< relref "/os/windows/hresult-e-fail" >}}) — General failure, often a broader form of this error
- [E_INVALIDARG (0x80070057)]({{< relref "/os/windows/hresult-e-invalid-arg" >}}) — Invalid argument when parameters are malformed
- [E_OUTOFMEMORY (0x8007000E)]({{< relref "/os/windows/hresult-e-outofmemory" >}}) — Out of memory during allocation
