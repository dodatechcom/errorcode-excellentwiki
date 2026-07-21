---
title: "[Solution] Background Job Error"
description: "Background job errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Background Job Error

Background job errors.

### Common Causes
Job not started; wrong command; output issues

### How to Fix
```powershell
Start-Job -ScriptBlock { Get-Process }
Get-Job | Receive-Job
```

### Examples
```powershell
$job = Start-Job -ScriptBlock { Start-Sleep 5; "Done" }
Wait-Job $job
Receive-Job $job
```
