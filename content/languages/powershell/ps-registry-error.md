---
title: "[Solution] Registry Access Error"
description: "Registry read/write errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Registry Access Error

Registry read/write errors.

### Common Causes
Path not found; permissions; wrong hive

### How to Fix
```powershell
Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion" -Name "ProgramFilesDir"
```

### Examples
```powershell
New-ItemProperty -Path "HKCU:\Software\MyApp" -Name "Version" -Value "1.0"
```
