---
title: "[Solution] Cmdlet Not Found Error"
description: "PowerShell cannot find the specified cmdlet."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Cmdlet Not Found Error

PowerShell cannot find the specified cmdlet.

### Common Causes
Cmdlet misspelled; module not imported; wrong module

### How to Fix
```powershell
Get-Command -Name Get-Something
```

### Examples
```powershell
Import-Module ActiveDirectory
Get-ADUser -Filter "*"
```
