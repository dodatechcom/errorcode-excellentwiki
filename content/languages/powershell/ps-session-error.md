---
title: "[Solution] PSSession Error"
description: "PowerShell session errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# PSSession Error

PowerShell session errors.

### Common Causes
Session limit; disconnected; not authenticated

### How to Fix
```powershell
Get-PSSession
Remove-PSSession -Id 1
```

### Examples
```powershell
$s = New-PSSession -ComputerName server
Enter-PSSession $s
```
