---
title: "[Solution] Tee-Object Error"
description: "Tee-Object fails to write and pass through."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Tee-Object Error

Tee-Object fails to write and pass through.

### Common Causes
File path invalid; permissions

### How to Fix
```powershell
Get-Process | Tee-Object -FilePath "processes.txt"
```

### Examples
```powershell
Get-Process | Tee-Object -Variable myProcesses | Measure-Object
```
