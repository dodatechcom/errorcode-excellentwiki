---
title: "[Solution] Module Not Loaded Error"
description: "Required module is not loaded in the session."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Module Not Loaded Error

Required module is not loaded in the session.

### Common Causes
Module not imported; wrong path; missing dependency

### How to Fix
```powershell
Get-Module -Name MyModule -ListAvailable
Import-Module MyModule
```

### Examples
```powershell
Import-Module ActiveDirectory -ErrorAction Stop
```
