---
title: "[Solution] Get-Item Error"
description: "Get-Item fails to retrieve item."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Get-Item Error

Get-Item fails to retrieve item.

### Common Causes
Path not found; wildcard issues; permissions

### How to Fix
```powershell
Get-Item "C:\temp\file.txt"
```

### Examples
```powershell
Get-Item "C:\Windows\System32\drivers\etc\hosts"
```
