---
title: "[Solution] Select-Object Error"
description: "Select-Object fails with wrong properties."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Select-Object Error

Select-Object fails with wrong properties.

### Common Causes
Property not found; typo in name

### How to Fix
```powershell
Get-Process | Select-Object Name, Id, CPU
```

### Examples
```powershell
Get-Process | Select-Object -Property Name, Id -First 5
```
