---
title: "[Solution] PowerShell Set-Location Provider Not Found Fix"
description: "Fix PowerShell Set-Location error about provider not found on Windows. Resolve PSDrive and provider errors when changing directories."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] PowerShell Set-Location Provider Not Found Fix

The Set-Location provider not found error occurs when PowerShell cannot find the requested navigation provider.

## Common Causes
- Attempting to navigate to a non-existent PSDrive
- Custom provider module not loaded in the session
- Registry provider path does not exist
- HKLM or HKCU hive not mounted
- Module providing the provider was uninstalled

## How to Fix

### Solution 1: Check Available Providers

```powershell
Get-PSProvider | Select-Object Name, Capabilities, Drives
```

### Solution 2: List Available PSDrives

```powershell
Get-PSDrive | Select-Object Name, Provider, Root
```

### Solution 3: Create a New PSDrive

```powershell
New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT
Set-Location HKCR:\
```

### Solution 4: Verify the Path Exists

```powershell
Test-Path "C:\NonExistentFolder"
```

### Solution 5: Load Required Module

```powershell
Import-Module ModuleName -Force
Set-Location ProviderDrive:\
```

## Examples
```powershell
Get-PSProvider | Format-Table Name, Capabilities -AutoSize
Get-PSDrive | Format-Table Name, Provider, Root -AutoSize
```
