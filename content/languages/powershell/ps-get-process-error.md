---
title: "[Solution] Get-Process Error"
description: "Get-Process fails with wrong parameters."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Get-Process Error

Get-Process fails with wrong parameters.

### Common Causes
Process not running; wrong name

### How to Fix
```powershell
Get-Process -Name "*sql*"
```

### Examples
```powershell
Get-Process -Name notepad -ErrorAction SilentlyContinue
```
