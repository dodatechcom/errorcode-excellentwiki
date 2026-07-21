---
title: "[Solution] .NET Framework Not Installed Error Fix"
description: "Fix .NET Framework not installed or enabled error on Windows. Resolve .NET Framework installation and activation failures on Windows 10 and 11."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] .NET Framework Not Installed Error Fix

The .NET Framework not installed error appears when an application requires a specific .NET Framework version that is not present on the system.

## Common Causes
- Application requires an older .NET Framework version not included by default
- .NET Framework feature disabled in Windows Features
- Corrupted .NET Framework installation
- Application not compatible with .NET Framework 4.x
- Windows Feature on Demand package missing

## How to Fix

### Solution 1: Enable .NET Framework in Windows Features

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName NetFx3 -All
Enable-WindowsOptionalFeature -Online -FeatureName NetFx4 -All
```

### Solution 2: Download and Install from Microsoft

Download the offline installer from the official Microsoft .NET Framework download page.

### Solution 3: Repair .NET Framework

```cmd
DISM /Online /Enable-Feature /FeatureName:NetFx3 /All
```

### Solution 4: Check Installed Versions

```powershell
Get-ChildItem "HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP" -Recurse | Get-ItemProperty -Name Version -ErrorAction SilentlyContinue | Select-Object PSChildName, Version
```

### Solution 5: Use .NET Repair Tool

Download the official Microsoft .NET Framework Repair Tool from the Microsoft support site.

## Examples
```powershell
Get-WindowsOptionalFeature -Online | Where-Object { $_.FeatureName -like 'NetFx*' }
```
