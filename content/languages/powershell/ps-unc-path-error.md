---
title: "[Solution] UNC Path Error"
description: "PowerShell cannot access UNC network path."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# UNC Path Error

PowerShell cannot access UNC network path.

### Common Causes
Network unavailable; wrong credentials; firewall

### How to Fix
```powershell
Test-Path \\server\share
```

### Examples
```powershell
$cred = Get-Credential
New-PSDrive -Name Z -PSProvider FileSystem -Root \\server\share -Credential $cred
```
