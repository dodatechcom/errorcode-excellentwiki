---
title: "[Solution] Pipeline Variable Error"
description: "$_ and $PSItem errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Pipeline Variable Error

$_ and $PSItem errors.

### Common Causes
Wrong variable in pipeline; not in pipeline

### How to Fix
```powershell
1..10 | ForEach-Object { $_ * 2 }
```

### Examples
```powershell
Get-Process | Where-Object { $_.Name -like "*sql*" }
```
