---
title: "[Solution] Execution Policy Error"
description: "Script execution blocked by execution policy."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Execution Policy Error

Script execution blocked by execution policy.

### Common Causes
Policy set to Restricted; wrong scope

### How to Fix
```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Examples
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```
