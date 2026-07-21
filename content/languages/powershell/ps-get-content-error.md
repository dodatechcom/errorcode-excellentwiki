---
title: "[Solution] Get-Content Error"
description: "Get-Content fails to read file."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Get-Content Error

Get-Content fails to read file.

### Common Causes
Path not found; encoding; file in use

### How to Fix
```powershell
Get-Content "C:\temp\file.txt"
```

### Examples
```powershell
Get-Content "C:\temp\file.txt" -Encoding UTF8
```
