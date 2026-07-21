---
title: "[Solution] New-Item Error"
description: "New-Item fails to create item."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# New-Item Error

New-Item fails to create item.

### Common Causes
Path exists; wrong type; permissions

### How to Fix
```powershell
New-Item -Path "C:\temp\newdir" -ItemType Directory
```

### Examples
```powershell
New-Item -Path "C:\temp\new.txt" -ItemType File -Force
```
