---
title: "[Solution] PowerShell PSSecurityException — Execution Policy Error"
description: "Fix PowerShell execution policy errors when scripts cannot run due to security restrictions. Change or bypass execution policy."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell PSSecurityException — Execution Policy Error Fix

Execution policy errors prevent PowerShell scripts from running. The error reads: `File cannot be loaded because running scripts is disabled on this system.`

## What This Error Means

PowerShell execution policies control which scripts are allowed to run. The default policy on Windows is `Restricted` (no scripts allowed) or `AllSigned` (scripts must be signed).

## Common Causes

- Execution policy set to `Restricted` (default)
- Script not digitally signed
- Policy set by Group Policy (cannot be overridden)
- Downloaded script blocked by Windows
- Running scripts from network share with restricted policy

## How to Fix

### 1. Check current execution policy

```powershell
Get-ExecutionPolicy
Get-ExecutionPolicy -List
```

### 2. Set execution policy

```powershell
# Allow local scripts, require signing for remote
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Allow all scripts (less secure)
Set-ExecutionPolicy Bypass -Scope CurrentUser

# Unrestricted (prompts for remote scripts)
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
```

### 3. Bypass policy for a single script

```powershell
# Run with bypass
powershell -ExecutionPolicy Bypass -File script.ps1

# Or from within PowerShell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\script.ps1
```

### 4. Unblock downloaded scripts

```powershell
# Remove the "downloaded from internet" block
Unblock-File -Path .\script.ps1

# Or for all scripts in a folder
Get-ChildItem *.ps1 | Unblock-File
```

## Related Errors

- [CommandNotFoundException](powershell-command-not-found) — command not found
- [UnauthorizedAccess](unauthorized-access) — access denied errors
- [Script Syntax Error](script-syntax) — script syntax issues
