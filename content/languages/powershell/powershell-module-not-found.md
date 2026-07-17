---
title: "[Solution] PowerShell ModuleNotFound Error"
description: "Fix 'ModuleNotFound' errors in PowerShell when modules fail to import, are not installed, or cannot be found on the module path."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# PowerShell ModuleNotFound Error Fix

ModuleNotFound errors occur when `Import-Module` cannot find the specified module. The error reads: `The specified module 'X' was not loaded because no valid module file was found in any module directory.`

## What This Error Means

PowerShell searches for modules in paths listed in `$env:PSModulePath`. If the module isn't installed or isn't in a recognized path, the import fails.

## Common Causes

- Module not installed on the system
- Module path not included in `$env:PSModulePath`
- Module name typo
- Module requires a specific PowerShell version
- NuGet provider not installed (for PSGallery modules)

## How to Fix

### 1. Install the missing module

```powershell
# Install from PowerShell Gallery
Install-Module -Name ModuleName -Force

# With scope
Install-Module -Name ModuleName -Scope CurrentUser -Force
```

### 2. Check module availability

```powershell
# List available modules
Get-Module -ListAvailable

# Check specific module
Get-Module -Name ModuleName -ListAvailable

# Check module path
$env:PSModulePath -split ';'
```

### 3. Add module path

```powershell
# Add custom module path
$env:PSModulePath += ";C:\CustomModules"

# Make it permanent
[Environment]::SetEnvironmentVariable("PSModulePath",
    $env:PSModulePath + ";C:\CustomModules", "User")
```

### 4. Install NuGet provider

```powershell
# Required for PSGallery modules
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
```

## Related Errors

- [CommandNotFoundException](powershell-command-not-found) — command not found
- [ParameterBindingException](powershell-parameter-binding) — parameter issues
- [UnauthorizedAccess](unauthorized-access) — module signing errors
