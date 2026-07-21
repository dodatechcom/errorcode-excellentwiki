---
title: "[Solution] Test-Path Error"
description: "Test-Path returns unexpected results."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Test-Path Error

Test-Path returns unexpected results.

### Common Causes
Wildcards in path; registry vs filesystem

### How to Fix
```powershell
Test-Path "C:\temp\file.txt"
```

### Examples
```powershell
Test-Path "HKLM:\Software\Microsoft\Windows"
```
