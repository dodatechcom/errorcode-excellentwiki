---
title: "[Solution] Foreach Loop Error"
description: "ForEach loop errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Foreach Loop Error

ForEach loop errors.

### Common Causes
Wrong collection; null elements

### How to Fix
```powershell
$items | ForEach-Object { Write-Output $_ }
```

### Examples
```powershell
foreach ($proc in Get-Process) { if ($proc.CPU -gt 10) { Write-Output $proc.Name } }
```
