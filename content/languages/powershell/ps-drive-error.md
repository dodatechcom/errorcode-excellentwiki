---
title: "[Solution] Drive Error"
description: "PowerShell drive mapping fails."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Drive Error

PowerShell drive mapping fails.

### Common Causes
Drive already exists; invalid root; permissions

### How to Fix
```powershell
Get-PSDrive
New-PSDrive -Name Z -PSProvider FileSystem -Root "C:\temp"
```

### Examples
```powershell
New-PSDrive -Name Z -PSProvider FileSystem -Root "C:\temp" -Persist
```
