---
title: "[Solution] Get-ChildItem Error"
description: "Get-ChildItem fails with wrong path."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Get-ChildItem Error

Get-ChildItem fails with wrong path.

### Common Causes
Path not found; recursive issues; hidden files

### How to Fix
```powershell
Get-ChildItem "C:\temp" -Recurse -Filter "*.log"
```

### Examples
```powershell
Get-ChildItem "C:\temp" -Force -Include *.txt, *.log
```
