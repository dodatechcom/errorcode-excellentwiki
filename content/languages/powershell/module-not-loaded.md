---
title: "[Solution] PowerShell ModuleNotFound Fix"
description: "Fix 'ModuleNotFound' when PowerShell cannot find or load a module."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell ModuleNotFound Fix

This error occurs when PowerShell cannot locate or import a required module. The error message reads: `The specified module 'X' was not loaded because no valid module file was found in any module directory.`

## Description

PowerShell modules extend functionality by providing cmdlets, functions, and variables. When `Import-Module` is called, PowerShell searches registered module paths for a matching `.psd1` or `.psm1` file. If no valid module manifest is found, the import fails with a `ModuleNotFound` error.

## Common Causes

- **Module not installed** — the module was never installed on the system.
- **Module installed for different PowerShell edition** — module installed in Windows PowerShell but used in PowerShell 7, or vice versa.
- **Corrupted module files** — the module manifest (`.psd1`) or script module (`.psm1`) is damaged.
- **Module path not configured** — `$env:PSModulePath` doesn't include the module's location.

## How to Fix

### Fix 1: Install the missing module

```powershell
# Find the module in the gallery
Find-Module -Name "ModuleName"

# Install for current user
Install-Module -Name ModuleName -Scope CurrentUser

# Install for all users (requires admin)
Install-Module -Name ModuleName -Scope AllUsers
```

### Fix 2: Check module availability and path

```powershell
# Check if module is available
Get-Module -Name ModuleName -ListAvailable

# Check PSModulePath
$env:PSModulePath -split ";"

# Add custom module path
$env:PSModulePath += ";C:\CustomModules"
```

### Fix 3: Verify module manifest integrity

```powershell
# Test the module manifest
Test-ModuleManifest -Path "C:\Modules\ModuleName\ModuleName.psd1"

# Check if the manifest loads correctly
$manifest = Test-ModuleManifest -Path "C:\Modules\ModuleName\ModuleName.psd1" -ErrorAction Stop
Write-Host "Module: $($manifest.Name) v$($manifest.Version)"
```

### Fix 4: Import with full path as a workaround

```powershell
# Import directly from file path
Import-Module "C:\CustomModules\MyModule\MyModule.psd1"

# Or import a .psm1 file directly
Import-Module "C:\Scripts\MyScriptModule.psm1"
```

## Examples

```powershell
PS> Import-Module Az.Accounts
ImportModule: The specified module 'Az.Accounts' was not loaded because no valid module file was found.

PS> Get-Module Az.Accounts -ListAvailable
# Returns nothing — module not installed

PS> Install-Module Az.Accounts -Scope CurrentUser
PS> Import-Module Az.Accounts
# Works after installation
```

## Related Errors

- [CommandNotFoundException](command-not-found.md) — command not recognized.
- [CommandNotRecognized2](command-not-found2.md) — similar command lookup failure.
- [UnauthorizedAccess](unauthorized-access.md) — permission denied loading module.
