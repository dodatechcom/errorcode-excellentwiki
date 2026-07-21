---
title: "[Solution] Switch Parameter Error"
description: "Switch parameter usage errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Switch Parameter Error

Switch parameter usage errors.

### Common Causes
Wrong syntax; used as value

### How to Fix
```powershell
Get-Process -Name "notepad" -ErrorAction SilentlyContinue
```

### Examples
```powershell
Get-ChildItem -Recurse -Force
```
