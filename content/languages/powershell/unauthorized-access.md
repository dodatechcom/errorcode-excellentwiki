---
title: "[Solution] PowerShell UnauthorizedAccess Fix"
description: "Fix 'UnauthorizedAccess' when PowerShell lacks permission to perform an operation."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell UnauthorizedAccess Fix

This error occurs when PowerShell attempts an operation that requires higher privileges than the current session has. The error message reads: `Access to the path 'X' is denied.` or `The requested operation requires elevation.`

## Description

PowerShell inherits the security context of the user running it. Operations that modify system files, registry keys, services, or other protected resources require administrative privileges. When the current user lacks the necessary permissions, an `UnauthorizedAccess` or `SecurityException` is thrown.

## Common Causes

- **Insufficient user privileges** — the operation requires admin rights but the session is running as a standard user.
- **File or directory permissions** — the target resource has restrictive ACLs that deny the current user access.
- **UAC elevation required** — User Account Control blocks privileged operations in non-elevated sessions.
- **Ownership issues** — the current user doesn't own the resource and lacks explicit permissions.

## How to Fix

### Fix 1: Run PowerShell as Administrator

```powershell
# Right-click PowerShell and select "Run as administrator"
# Or from an existing elevated prompt
Start-Process powershell -Verb RunAs

# Check current privileges
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal(
    [Security.Principal.WindowsIdentity]::GetCurrent()
)
$currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```

### Fix 2: Adjust file/folder permissions

```powershell
# View current permissions
Get-Acl "C:\Path\To\Item" | Format-List

# Grant full control to current user (requires admin)
$acl = Get-Acl "C:\Path\To\Item"
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
    [System.Security.Principal.WindowsIdentity]::GetCurrent().Name,
    "FullControl",
    "Allow"
)
$acl.AddAccessRule($rule)
Set-Acl "C:\Path\To\Item" $acl
```

### Fix 3: Take ownership of files

```powershell
# Take ownership (requires admin)
takeown /F "C:\Path\To\Item" /R /A

# Then grant permissions
icacls "C:\Path\To\Item" /grant "${env:USERNAME}:(OI)(CI)F"
```

### Fix 4: Use -ErrorAction to handle gracefully

```powershell
# Suppress errors for non-critical operations
Get-ChildItem "C:\ProtectedFolder" -ErrorAction SilentlyContinue

# Or catch and handle the error
try {
    Set-Content "C:\SystemFile.txt" "data"
} catch [System.UnauthorizedAccessException] {
    Write-Warning "Insufficient permissions — run as Administrator"
}
```

## Examples

```powershell
PS> Set-Content "C:\Windows\System32\test.txt" "hello"
Set-Content: Access to the path 'C:\Windows\System32\test.txt' is denied.

PS> Remove-Item "C:\Program Files\App\file.dll"
Remove-Item: Access to the path 'C:\Program Files\App\file.dll' is denied.

PS> New-Item "C:\Windows\test.txt" -ItemType File
New-Item: Access to the path 'C:\Windows\test.txt' is denied.
```

## Related Errors

- [InvalidOperation](invalid-operation.md) — operation not valid on current state.
- [PSRemotingError](remote-error.md) — remote session permission issues.
- [CredentialError](credential-error.md) — authentication failure.
