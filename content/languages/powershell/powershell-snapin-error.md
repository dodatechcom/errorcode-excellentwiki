---
title: "[Solution] PowerShell Add-PSSnapIn Load Error Fix"
description: "Fix PowerShell snap-in loading errors when Add-PSSnapIn fails."
languages: ["powershell"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PowerShell Add-PSSnapIn Load Error Fix

A PowerShell snap-in load error occurs when `Add-PSSnapIn` fails to register a legacy snap-in with the PowerShell session.

## What This Error Means

PSSnapIn is the legacy (pre-module) way to extend PowerShell. `Add-PSSnapIn` registers snap-ins that provide cmdlets. Errors occur when the snap-in DLL is missing, not registered with the GAC, or incompatible with the current PowerShell version.

## Common Causes

- Snap-in DLL not found or not installed
- Snap-in not in GAC (Global Assembly Cache)
- Incompatible snap-in version for PowerShell edition
- Wrong PowerShell edition (Core vs Desktop)
- Snap-in requires specific .NET Framework version

## How to Fix

### 1. Check if snap-in exists

```powershell
# CORRECT: Verify snap-in is registered
Get-PSSnapIn -Registered | Where-Object { $_.Name -like "*SQL*" }

# Try to add it
Add-PSSnapIn "SqlServerCmdletSnapin" -ErrorAction Stop
```

### 2. Use modules instead of snap-ins

```powershell
# CORRECT: Prefer modules over snap-ins
# Instead of:
# Add-PSSnapIn "SqlCmdletsSnapin"

# Use:
Install-Module -Name SqlServer -Force
Import-Module SqlServer
```

### 3. Register the snap-in DLL

```powershell
# CORRECT: Register if not in GAC
# Run from elevated PowerShell
$snapinPath = "C:\Program Files\Microsoft SQL Server\110\Tools\SnapIn\Microsoft.SqlServer.SqlManagementObjects.dll"
InstallUtil /user $snapinPath  # Register in GAC
```

### 4. Handle missing snap-ins gracefully

```powershell
# CORRECT: Check before adding
$snapinName = "SqlServerCmdletSnapin"
if (Get-PSSnapIn -Registered | Where-Object { $_.Name -eq $snapinName }) {
    Add-PSSnapIn $snapinName -ErrorAction Stop
    Write-Host "Snap-in loaded: $snapinName"
} else {
    Write-Warning "Snap-in '$snapinName' not registered. Using module alternative."
    Import-Module SqlServer -ErrorAction SilentlyContinue
}
```

## Related Errors

- [PowerShell Module Load Error](powershell-module-load-error) — module loading
- [PowerShell Command Not Found](powershell-command-not-found) — missing commands
- [PowerShell Profile Error](powershell-profile-error-v2) — profile errors
