---
title: "[Solution] Permission Error"
description: "Permission denied errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Permission Error

Permission denied errors.

### Common Causes
Not admin; wrong ACL; ownership

### How to Fix
```powershell
Start-Process powershell -Verb RunAs
```

### Examples
```powershell
icacls "C:\data" /grant "DOMAIN\User:(OI)(CI)F"
```
