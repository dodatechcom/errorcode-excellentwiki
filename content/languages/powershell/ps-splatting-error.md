---
title: "[Solution] Splatting Error"
description: "Splatting syntax errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Splatting Error

Splatting syntax errors.

### Common Causes
Wrong @; hashtable keys; missing keys

### How to Fix
```powershell
$params = @{Name = "MyModule"; Force = $true}
Import-Module @params
```

### Examples
```powershell
Get-Process @params
```
