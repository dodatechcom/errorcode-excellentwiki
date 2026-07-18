---
title: "[Solution] PowerShell Snap-in Registration Failed Error Fix"
description: "Fix PowerShell snap-in registration errors when Add-PSSnapIn fails. Learn why snap-in loading fails and how to use modern modules instead."
languages: ["powershell"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A PowerShell snap-in registration error occurs when `Add-PSSnapIn` fails to load a legacy snap-in. Snap-ins are the pre-module way to extend PowerShell and are increasingly deprecated in favor of modules. Errors occur when the snap-in DLL is missing, not registered, or incompatible with the current PowerShell version.

## Why It Happens

- The snap-in DLL is not installed or not in the GAC (Global Assembly Cache)
- The snap-in was designed for an older PowerShell version
- 32-bit snap-in is used in 64-bit PowerShell or vice versa
- Required .NET Framework version is not installed
- The snap-in has been superseded by a module
- Running on PowerShell Core which does not support snap-ins natively

## How to Fix It

### Check if snap-in is registered

```powershell
# WRONG: Adding snap-in without checking
Add-PSSnapIn "MyOldSnapIn"  # may not exist

# CORRECT: Verify registration first
$registered = Get-PSSnapIn -Registered | Where-Object { $_.Name -eq "MyOldSnapIn" }
if ($registered) {
    Add-PSSnapIn "MyOldSnapIn"
} else {
    Write-Warning "Snap-in 'MyOldSnapIn' not registered"
}
```

### Use modules instead of snap-ins

```powershell
# CORRECT: Prefer modern modules over snap-ins
# Instead of:
# Add-PSSnapIn "SqlServerCmdletSnapin"

# Use:
Install-Module -Name SqlServer -Force -Scope CurrentUser
Import-Module SqlServer
```

### Register the snap-in DLL if needed

```powershell
# CORRECT: Register the snap-in using InstallUtil
$snapinPath = "C:\Path\To\Snapin.dll"
# Run from elevated PowerShell
& "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe" /user $snapinPath
```

### Handle legacy snap-in migration

```powershell
# CORRECT: Map old snap-ins to new module equivalents
$snapinModuleMap = @{
    "SqlServerCmdletSnapin" = "SqlServer"
    "SharePoint.PowerShell.SNAP" = "SharePoint.PowerShell"
    "Microsoft.Exchange.Management.PowerShell.SnapIn" = "ExchangeOnlineManagement"
}

foreach ($snapin in $snapinModuleMap.Keys) {
    $loaded = Get-PSSnapIn -Registered | Where-Object { $_.Name -eq $snapin }
    if ($loaded) {
        Add-PSSnapIn $snapin -ErrorAction SilentlyContinue
    } else {
        $module = $snapinModuleMap[$snapin]
        if (Get-Module -ListAvailable $module) {
            Import-Module $module
            Write-Host "Loaded module $module instead of snap-in $snapin"
        }
    }
}
```

### Check PowerShell edition compatibility

```powershell
# CORRECT: Snap-ins are not supported in PowerShell Core
if ($PSVersionTable.PSEdition -eq "Core") {
    Write-Warning "Snap-ins are not supported in PowerShell Core. Use modules instead."
} else {
    Add-PSSnapIn "MyLegacySnapIn" -ErrorAction SilentlyContinue
}
```

## Common Mistakes

- Assuming snap-ins will continue to be supported in future PowerShell versions
- Not checking if a module replacement exists before trying to load a snap-in
- Forgetting that snap-ins require registration in the GAC
- Using 32-bit snap-ins in 64-bit PowerShell without SysWOW64 registration
- Not handling the case where both a snap-in and its module replacement are available

## Related Pages

- [PowerShell Module Not Found](ps-module-not-found-v2) - module not loaded
- [PowerShell Command Not Found](ps-command-not-found-v2) - cmdlet not found
- [PowerShell Profile Error](ps-profile-error) - profile load failure
- [PowerShell Module Not Found](ps-module-not-found-v2) - module loading
