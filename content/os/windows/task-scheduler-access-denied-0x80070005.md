---
title: "[Solution] Task Scheduler Access Denied Error 0x80070005 Fix"
description: "Fix Task Scheduler error 0x80070005 access denied when creating or modifying tasks on Windows. Resolve permissions issues in Task Scheduler."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Task Scheduler Access Denied Error 0x80070005 Fix

Task Scheduler returns error 0x80070005 (Access Denied) when the user lacks permission to create, modify, or run a scheduled task.

## Common Causes
- User is not an administrator
- Task stored in a protected folder
- Group Policy restricting task creation
- UAC blocking task creation without elevation
- Task requires elevated permissions not granted

## How to Fix

### Solution 1: Run Task Scheduler as Administrator

Right-click Task Scheduler and select Run as administrator.

### Solution 2: Create Task in User Folder

```powershell
Register-ScheduledTask -TaskName "MyTask" -Action $action -Trigger $trigger -TaskPath \
```

### Solution 3: Use System Account

```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\Scripts\task.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At "03:00"
Register-ScheduledTask -TaskName "MyTask" -Action $action -Trigger $trigger -User "SYSTEM" -RunLevel Highest
```

### Solution 4: Check Group Policy Restrictions

```powershell
gpresult /h C:\gpreport.html
```

### Solution 5: Modify Task XML Directly

Export the task XML, edit it to include proper principal settings, and re-import.

## Examples
```powershell
Get-ScheduledTask | Where-Object { $_.TaskPath -eq '\' } | Select-Object TaskName, State
```
