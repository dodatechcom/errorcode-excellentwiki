---
title: "[Solution] Runspace Error"
description: "Runspace pool errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Runspace Error

Runspace pool errors.

### Common Causes
Pool not opened; wrong state

### How to Fix
```powershell
$pool = [RunspaceFactory]::CreateRunspacePool(1, 5)
$pool.Open()
```

### Examples
```powershell
$ps = [PowerShell]::Create().AddScript("Get-Process")
$ps.Runspace.RunspacePool = $pool
```
