---
title: "[Solution] Disk Space Error"
description: "Disk operation errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Disk Space Error

Disk operation errors.

### Common Causes
Not enough space; wrong drive; permissions

### How to Fix
```powershell
Get-PSDrive C
```

### Examples
```powershell
Get-Volume | Where-Object { $_.DriveLetter -eq "C" }
```
