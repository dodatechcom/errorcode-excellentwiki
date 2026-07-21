---
title: "[Solution] Scheduled Task Error"
description: "Scheduled task creation/management errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Scheduled Task Error

Scheduled task creation/management errors.

### Common Causes
Wrong trigger; action path; permissions

### How to Fix
```powershell
Get-ScheduledTask | Where-Object { $_.TaskName -like "*Backup*" }
```

### Examples
```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\scripts\backup.ps1"
```
