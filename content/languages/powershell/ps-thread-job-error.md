---
title: "[Solution] Thread Job Error"
description: "ThreadJob errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Thread Job Error

ThreadJob errors.

### Common Causes
Thread not started; module missing

### How to Fix
```powershell
Start-ThreadJob -ScriptBlock { Get-Date }
```

### Examples
```powershell
Install-Module ThreadJob -Scope CurrentUser
Start-ThreadJob { 1..10 | ForEach-Object { $_ * 2 } }
```
