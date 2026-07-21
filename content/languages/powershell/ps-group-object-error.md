---
title: "[Solution] Group-Object Error"
description: "Group-Object fails on grouping property."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Group-Object Error

Group-Object fails on grouping property.

### Common Causes
Property not found; null values

### How to Fix
```powershell
Get-Process | Group-Object { $_.Name.Substring(0,3) }
```

### Examples
```powershell
Get-Process | Group-Object Name -NoElement
```
