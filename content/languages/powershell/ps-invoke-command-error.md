---
title: "[Solution] Invoke-Command Error"
description: "Invoke-Command remote execution fails."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Invoke-Command Error

Invoke-Command remote execution fails.

### Common Causes
Computer unreachable; authentication failure

### How to Fix
```powershell
Invoke-Command -ComputerName server -ScriptBlock { Get-Process }
```

### Examples
```powershell
$sess = New-PSSession -ComputerName server
Invoke-Command -Session $sess -ScriptBlock { Get-Service }
```
