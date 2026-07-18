---
title: "[Solution] PowerShell Module Cannot Be Loaded Error Fix"
description: "Fix PowerShell 'module cannot be loaded' errors. Learn why module loading fails and how to import modules correctly in PowerShell."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The PowerShell Module Load Failure occurs when `Import-Module` or auto-loading cannot load a PowerShell module. The error includes details about why loading failed, such as missing dependencies, version conflicts, or script execution errors within the module itself.

## Why It Happens

- The module is not installed on the system
- The module requires a specific PowerShell version not currently running
- A dependent module or DLL is missing
- The module script contains errors that prevent loading
- PowerShell Core module is incompatible with Windows PowerShell
- The module requires a specific .NET Framework version
- Module manifest has incorrect root module references

## How to Fix It

### Check if the module is installed

```powershell
# WRONG: Assuming module is available
Import-Module MyCustomModule  # fails

# CORRECT: Check installation first
Get-Module -ListAvailable -Name MyCustomModule

# Install if missing
Install-Module -Name MyCustomModule -Scope CurrentUser -Force
Import-Module MyCustomModule
```

### Verify module compatibility

```powershell
# WRONG: Importing module without checking version
Import-Module ActiveDirectory  # may need RSAT

# CORRECT: Check module manifest for requirements
(Get-Module -ListAvailable ActiveDirectory).Version
$PSVersionTable.PSVersion

# Check module required PS version
$manifest = Import-PowerShellDataFile (Get-Module -ListAvailable ActiveDirectory).Path -ErrorAction SilentlyContinue
if ($manifest) {
    $manifest.PowerShellVersion
}
```

### Fix missing dependent modules

```powershell
# WRONG: Module requires dependency that is not installed
Import-Module Az  # fails if Az.Accounts not installed

# CORRECT: Import with all required dependencies
# Az modules auto-import dependencies from the same folder
Import-Module Az -ErrorAction Stop

# Or install all Az modules
Install-Module -Name Az -Repository PSGallery -Force -Scope CurrentUser
```

### Handle module loading errors with detail

```powershell
# WRONG: Generic error handling
Import-Module ProblemModule  # error message is vague

# CORRECT: Capture detailed error information
try {
    Import-Module ProblemModule -ErrorAction Stop
} catch {
    Write-Error "Module load failed: $($_.Exception.Message)"
    Write-Error "FullyQualifiedErrorId: $($_.FullyQualifiedErrorId)"
    
    # Check module's error records
    $error | Where-Object { $_.TargetObject -eq "ProblemModule" }
}
```

### Use fully qualified module paths

```powershell
# WRONG: Ambiguous module name
Import-Module Utils  # may import wrong module

# CORRECT: Use full path
$modulePath = Get-Module -ListAvailable -Name Utils |
    Where-Object { $_.Path -like "*MyOrganization*" } |
    Select-Object -ExpandProperty Path

Import-Module $modulePath
```

### Check module signing requirements

```powershell
# CORRECT: Module may require signing in restricted environments
Get-AuthenticodeSignature (Get-Module -ListAvailable MyModule).Path

# If unsigned and policy requires signed modules:
# Option 1: Sign the module
# Option 2: Adjust policy for module path
```

## Common Mistakes

- Not installing the module before attempting to import it
- Forgetting that `Install-Module` requires NuGet provider
- Assuming `Import-Module` will install missing dependencies automatically
- Not checking if the module is blocked by execution policy or AppLocker
- Confusing module version with cmdlet version in different releases

## Related Pages

- [PowerShell Module Not Found](ps-module-not-found-v2) - module not found
- [PowerShell Command Not Found](ps-command-not-found-v2) - cmdlet not recognized
- [PowerShell Snapin Error](ps-snapin-error) - snap-in registration failed
- [PowerShell Profile Error](ps-profile-error) - profile load failure
