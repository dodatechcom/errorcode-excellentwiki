---
title: "[Solution] Where-Object Filter Error"
description: "Where-Object filter expression syntax error."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Where-Object Filter Error

Where-Object filter expression syntax error.

### Common Causes
Missing braces; wrong operator

### How to Fix
```powershell
Get-Process | Where-Object { $_.CPU -gt 10 }
```

### Examples
```powershell
Get-Process | Where-Object { $_.Name -like "*sql*" }
```
