---
title: "[Solution] Scheduled Task Not Running Error Fix"
description: "Fix Windows Task Scheduler task that is enabled but not running on schedule. Resolve task execution failures and scheduling errors on Windows."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Scheduled Task Not Running Error Fix

A scheduled task that is enabled but not running fails to execute at its configured time. This affects automated backups, maintenance scripts, and critical system operations.

## Common Causes
- Task configured to run only when user is logged on
- Incorrect trigger configuration or missing time conditions
- Task configured with expired credentials
- Power settings preventing task wake-up
- Task history disabled making debugging difficult

## How to Fix

### Solution 1: Check Task History

```powershell
Get-ScheduledTask -TaskName "TaskName" | Get-ScheduledTaskInfo | Select-Object LastRunTime, LastTaskResult, NextRunTime
```

### Solution 2: Enable Task History

Right-click Task Scheduler Library in Task Scheduler and select Enable Task History.

### Solution 3: Verify Run Whether User Is Logged On

Change to Run whether user is logged on or not in Task Properties.

### Solution 4: Update Stored Credentials

```powershell
Set-ScheduledTask -TaskName "TaskName" -User "DOMAIN\user" -Password "NewPassword"
```

### Solution 5: Check Wake to Run Setting

In Task Properties > Conditions, enable Wake the computer to run this task.

## Examples
```powershell
Get-ScheduledTask | Where-Object { $_.State -ne 'Running' -and $_.TaskPath -notlike '\Microsoft\*' } | Select-Object TaskName, State, LastRunTime
```
