---
title: "[Solution] Event ID 1002 Application Hang Error Fix"
description: "Fix Windows Event ID 1002 application hang event when a program becomes unresponsive. Resolve application freezing and hang detection events."
platforms: ["windows"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# [Solution] Event ID 1002 Application Hang Error Fix

Event ID 1002 records when an application becomes unresponsive and Windows terminates it after the hang detection timeout. The event includes the application name, PID, and hang duration.

## Common Causes
- Application waiting on a locked resource or deadlock
- Network request timeout causing the UI thread to block
- Excessive memory usage causing the application to page fault
- Third-party DLL causing the application to hang
- Corrupted application installation

## How to Fix

### Solution 1: Review Hang Details

```powershell
Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1002} -MaxEvents 5 | Format-Table TimeCreated, Message -Wrap
```

### Solution 2: Update the Application

Download and install the latest version of the hanging application.

### Solution 3: Check for Conflicting Software

Temporarily disable overlays, plugins, or extensions that may be causing the hang.

### Solution 4: Increase Application Priority

Open Task Manager, right-click the application, go to Details tab, and set priority to High or Above Normal.

### Solution 5: Reinstall the Application

Uninstall and perform a clean reinstall to rule out corrupted files.

## Examples
```powershell
Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1002} -MaxEvents 10 | ForEach-Object { [xml]$_.ToXml() } | Select-Object -ExpandProperty EventData
```
