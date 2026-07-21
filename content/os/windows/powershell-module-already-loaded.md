---
title: "[Solution] PowerShell Module Already Loaded Error Fix"
description: "Fix PowerShell error when a module is already loaded or conflicts with an existing version. Resolve module loading and version conflicts on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] PowerShell Module Already Loaded Error Fix

The PowerShell module already loaded error occurs when you attempt to import a module that is already present in the current session, or when a different version is already loaded and conflicts with the requested version.

## Common Causes
- Module previously imported in the current session
- Different version of the module already loaded
- Circular module dependencies
- Module loaded in all-users scope conflicting with local scope
- PowerShell profile auto-loading the module before your script

## How to Fix

### Solution 1: Remove and Re-import

```powershell
Remove-Module -Name ModuleName -Force
Import-Module ModuleName -RequiredVersion 2.0
```

### Solution 2: Check Loaded Modules

```powershell
Get-Module -Name ModuleName -All | Select-Object Name, Version, ModuleBase
```

### Solution 3: Use -Force Parameter

```powershell
Import-Module ModuleName -Force
```

### Solution 4: Start a Fresh PowerShell Session

Close and reopen PowerShell to clear all loaded modules.

### Solution 5: Check Profile for Auto-loading

```powershell
Get-Content $PROFILE
```

## Examples
```powershell
Get-Module -ListAvailable | Where-Object { $_.Name -eq 'ModuleName' } | Select-Object Name, Version
```
