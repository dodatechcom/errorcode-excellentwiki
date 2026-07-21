---
title: "[Solution] Provider Error"
description: "PowerShell provider operation fails."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Provider Error

PowerShell provider operation fails.

### Common Causes
Wrong provider; path invalid for provider

### How to Fix
```powershell
Get-PSProvider
Set-Location -Path "C:\"
```

### Examples
```powershell
Set-Location -Path "C:\Users"
```
