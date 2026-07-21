---
title: "[Solution] Pipeline Error"
description: "Pipeline input/output type mismatch."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Pipeline Error

Pipeline input/output type mismatch.

### Common Causes
Wrong input type; pipeline stopped

### How to Fix
```powershell
Get-Process | Where-Object { $_.CPU -gt 10 }
```

### Examples
```powershell
1..10 | ForEach-Object { $_ * 2 }
```
