---
title: "[Solution] Get-Service Error"
description: "Get-Service fails to retrieve service info."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Get-Service Error

Get-Service fails to retrieve service info.

### Common Causes
Service not found; wrong name; permissions

### How to Fix
```powershell
Get-Service -Name "*sql*"
```

### Examples
```powershell
Get-Service | Where-Object { $_.Status -eq "Running" }
```
