---
title: "[Solution] ConvertTo-Csv Error"
description: "ConvertTo-Csv conversion errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# ConvertTo-Csv Error

ConvertTo-Csv conversion errors.

### Common Causes
Wrong delimiter; non-convertible objects

### How to Fix
```powershell
Get-Process | ConvertTo-Csv
```

### Examples
```powershell
Get-Process | Select-Object Name, Id | ConvertTo-Csv -NoTypeInformation
```
