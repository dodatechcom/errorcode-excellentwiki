---
title: "[Solution] PSObject Error"
description: "PSObject creation errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# PSObject Error

PSObject creation errors.

### Common Causes
Wrong member types; add-member errors

### How to Fix
```powershell
$obj = [PSCustomObject]@{Name="Test"; Value=42}
```

### Examples
```powershell
$obj | Add-Member -NotePropertyName "Extra" -NotePropertyValue "data"
```
