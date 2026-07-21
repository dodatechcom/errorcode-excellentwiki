---
title: "[Solution] Set-Item Error"
description: "Set-Item fails to set item value."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Set-Item Error

Set-Item fails to set item value.

### Common Causes
Path read-only; wrong type; permissions

### How to Fix
```powershell
Set-Item -Path "C:\temp\file.txt" -Value "new content"
```

### Examples
```powershell
Set-Item -Path "HKLM:\Software\MyApp" -Name "Version" -Value "1.0"
```
