---
title: "[Solution] Object Member Not Found"
description: "Property or method does not exist on object."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Object Member Not Found

Property or method does not exist on object.

### Common Causes
Wrong name; object type different; typo

### How to Fix
```powershell
Get-Process | Get-Member -MemberType NoteProperty
```

### Examples
```powershell
$proc = Get-Process -Name "explorer"
$proc.Id
$proc.Kill()
```
