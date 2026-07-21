---
title: "[Solution] Command Not Recognized"
description: "PowerShell does not recognize the command name."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Command Not Recognized

PowerShell does not recognize the command name.

### Common Causes
Typo; module not imported; not a cmdlet

### How to Fix
```powershell
Get-Command my-command
```

### Examples
```powershell
Get-Command Get-Process
Get-Process
```
