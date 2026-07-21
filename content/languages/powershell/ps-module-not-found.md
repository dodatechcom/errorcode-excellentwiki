---
title: "[Solution] Module Not Found Error"
description: "PowerShell cannot find the specified module."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Module Not Found Error

PowerShell cannot find the specified module.

### Common Causes
Not installed; wrong name; not in PSModulePath

### How to Fix
```powershell
Get-Module -ListAvailable | Where-Object { $_.Name -like "*MyModule*" }
Find-Module MyModule
```

### Examples
```powershell
Install-Module -Name Az -Scope CurrentUser
Import-Module Az
```
