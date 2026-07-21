---
title: "[Solution] ConvertTo-String Error"
description: "ConvertTo-String fails on input."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# ConvertTo-String Error

ConvertTo-String fails on input.

### Common Causes
Non-convertible type; null value

### How to Fix
```powershell
42 | Out-String
```

### Examples
```powershell
Get-Process | Select-Object -First 5 | Out-String -Width 200
```
