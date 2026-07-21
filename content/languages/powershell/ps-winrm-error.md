---
title: "[Solution] WinRM Error"
description: "Windows Remote Management errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# WinRM Error

Windows Remote Management errors.

### Common Causes
Service not running; not configured; SSL issues

### How to Fix
```powershell
Get-Service WinRM
Start-Service WinRM
```

### Examples
```powershell
winrm quickconfig
```
