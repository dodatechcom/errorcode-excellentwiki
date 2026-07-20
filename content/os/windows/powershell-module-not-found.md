---
title: "[Solution] PowerShell MODULE_NOT_FOUND — Module Cannot Be Loaded"
description: "Fix PowerShell Module not found error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 1002
---

# [Solution] PowerShell MODULE_NOT_FOUND — Module Cannot Be Loaded

The PowerShell Module Not Found error occurs when PowerShell cannot locate or load a required module. This prevents cmdlets from being available and breaks scripts that depend on specific modules.

## Description

When you attempt to import or use a module that is not installed or not accessible, PowerShell returns an error indicating the module could not be found. The full error message reads:

> "The specified module 'ModuleName' was not loaded because no valid module file was found in any module directory."

This error can occur with both built-in and third-party modules from the PowerShell Gallery or local installations.

## Common Causes

1. The module is not installed on the system.
2. The module is installed for a different PowerShell version or architecture.
3. The module path is not included in `$env:PSModulePath`.
4. NuGet provider is not installed (required for PSGallery modules).
5. The module name is misspelled in the `Import-Module` command.
6. PowerShell Gallery repository is not registered or accessible.
7. Corporate proxy or firewall blocks access to PSGallery.

## Solutions

### Solution 1: Install the Module from PSGallery

Install the missing module directly from the PowerShell Gallery:

```powershell
Install-Module -Name "ModuleName" -Force -AllowClobber
```

For the current user only:

```powershell
Install-Module -Name "ModuleName" -Scope CurrentUser -Force
```

### Solution 2: Check Available Modules

Verify if the module is already installed but under a different name:

```powershell
Get-Module -ListAvailable | Where-Object { $_.Name -like "*Keyword*" }
```

Search for the module by command it provides:

```powershell
Get-Command -Module "ModuleName"
```

### Solution 3: Import with Full Path

If the module is installed but not in a standard path, import it directly:

```powershell
Import-Module -Name "C:\Path\To\Module\ModuleName.psd1"
```

### Solution 4: Install NuGet Provider

PSGallery requires the NuGet package provider:

```powershell
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
```

### Solution 5: Register PSGallery Repository

Ensure the PSGallery repository is registered:

```powershell
Register-PSRepository -Default -ErrorAction SilentlyContinue
Get-PSRepository
```

### Solution 6: Update PowerShellGet

An outdated PowerShellGet module can cause installation failures:

```powershell
Install-Module -Name PowerShellGet -Force -AllowClobber
```

### Solution 7: Check Module Path

Verify the module search paths:

```powershell
$env:PSModulePath -split ";"
```

Add a custom module path:

```powershell
$env:PSModulePath += ";C:\Custom\ModulePath"
```

## Related Errors

- [PowerShell Execution Policy Error]({{< relref "/os/windows/powershell-execution-policy-error" >}}) — Scripts cannot be loaded
- [PowerShell Get-Command Error]({{< relref "/os/windows/powershell-get-command-error" >}}) — Command not found
- [PowerShell Invoke-Command Error]({{< relref "/os/windows/powershell-invoke-command-error" >}}) — Remote execution failed
