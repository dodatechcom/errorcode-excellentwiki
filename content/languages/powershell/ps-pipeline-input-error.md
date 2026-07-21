---
title: "[Solution] Pipeline Input Error"
description: "Cmdlet does not accept pipeline input."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Pipeline Input Error

Cmdlet does not accept pipeline input.

### Common Causes
Parameter not pipeline-enabled; wrong binding

### How to Fix
```powershell
Get-Help Get-Process -Parameter Name
```

### Examples
```powershell
"hello", "world" | ForEach-Object { $_.ToUpper() }
```
