---
title: "[Solution] Add-Content Error"
description: "Add-Content fails to append."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Add-Content Error

Add-Content fails to append.

### Common Causes
Path not found; encoding; permissions

### How to Fix
```powershell
Add-Content "C:\temp\log.txt" -Value "New line"
```

### Examples
```powershell
Get-Date | Add-Content "C:\temp\log.txt"
```
