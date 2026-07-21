---
title: "[Solution] Positional Parameter Error"
description: "Positional parameter binding errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Positional Parameter Error

Positional parameter binding errors.

### Common Causes
Wrong position; ambiguous binding

### How to Fix
```powershell
Get-Process -Name "notepad"
```

### Examples
```powershell
Get-ChildItem -Path "C:\temp" -Filter "*.txt"
```
