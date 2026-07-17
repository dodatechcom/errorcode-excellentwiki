---
title: "[Solution] PowerShell ExecutionPolicy Error Fix"
description: "Fix 'ExecutionPolicy' when PowerShell blocks script execution due to policy restrictions."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell ExecutionPolicy Error Fix

This error occurs when PowerShell refuses to run a script because the current execution policy prohibits it. The error message reads: `File cannot be loaded because running scripts is disabled on this system.` or `SecurityError: File cannot be loaded. The file is not digitally signed.`

## Description

PowerShell's execution policy is a safety feature that controls which scripts are allowed to run. The default policy on Windows is `Restricted`, which blocks all `.ps1` scripts. Policies can be set at Machine, User, or Process scope, and they validate script origin and digital signatures.

## Common Causes

- **Default Restricted policy** — Windows ships with `Restricted` policy that blocks all scripts.
- **Script downloaded from the internet** — the file has a `Zone.Identifier` alternate data stream marking it as unsafe.
- **No digital signature** — `AllSigned` or `RemoteSigned` policy requires scripts to be signed.
- **Policy scope conflict** — a higher-scope policy (Machine) overrides a lower one (User).

## How to Fix

### Fix 1: Check current execution policy

```powershell
# View all policies
Get-ExecutionPolicy -List

# Check current effective policy
Get-ExecutionPolicy
```

### Fix 2: Set a permissive policy for current user

```powershell
# Allow locally created scripts to run (recommended)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Allow all scripts (less secure)
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

### Fix 3: Unblock downloaded scripts

```powershell
# Unblock a specific script
Unblock-File -Path "C:\Scripts\myscript.ps1"

# Unblock all scripts in a directory
Get-ChildItem "C:\Scripts\*.ps1" | Unblock-File

# Check if a file is blocked
Get-Item "C:\Scripts\myscript.ps1" -Stream Zone.Identifier
```

### Fix 4: Bypass policy for a single session

```powershell
# Bypass policy for current session only
powershell -ExecutionPolicy Bypass -File "C:\Scripts\myscript.ps1"

# Or from within PowerShell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

## Examples

```powershell
PS> .\myscript.ps1
myscript.ps1 cannot be loaded because running scripts is disabled on this system.

PS> Set-ExecutionPolicy Restricted
PS> .\myscript.ps1
myscript.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies.

PS> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
PS> .\myscript.ps1
# Now works for locally created scripts
```

## Related Errors

- [UnauthorizedAccess](unauthorized-access.md) — permission denied for file operations.
- [CredentialError](credential-error.md) — authentication failure.
- [ModuleNotFound](module-not-loaded.md) — module loading failure.
