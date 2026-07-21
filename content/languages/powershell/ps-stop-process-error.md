---
title: "[Solution] Stop-Process Error"
description: "Stop-Process fails to terminate process."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Stop-Process Error

Stop-Process fails to terminate process.

### Common Causes
Process not found; access denied; system process

### How to Fix
```powershell
Get-Process | Where-Object { $_.CPU -gt 50 }
Stop-Process -Name "notepad" -Force
```

### Examples
```powershell
Stop-Process -Id (Get-Process notepad).Id -Force -ErrorAction SilentlyContinue
```
