---
title: "[Solution] ConvertTo-Json Error"
description: "ConvertTo-Json conversion errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# ConvertTo-Json Error

ConvertTo-Json conversion errors.

### Common Causes
Depth exceeded; nested objects; null values

### How to Fix
```powershell
Get-Process | ConvertTo-Json -Depth 2
```

### Examples
```powershell
@{name="test"; value=42} | ConvertTo-Json
```
