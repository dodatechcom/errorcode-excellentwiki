---
title: "[Solution] Rename-Item Error"
description: "Rename-Item fails to rename."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Rename-Item Error

Rename-Item fails to rename.

### Common Causes
New name exists; in use; permissions

### How to Fix
```powershell
Rename-Item "C:\temp\file.txt" -NewName "renamed.txt"
```

### Examples
```powershell
Get-ChildItem "C:\temp\*.txt" | Rename-Item -NewName { $_.Name -replace 'old','new' }
```
