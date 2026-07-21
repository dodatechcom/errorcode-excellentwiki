---
title: "[Solution] Credential Error"
description: "Credential retrieval or usage fails."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Credential Error

Credential retrieval or usage fails.

### Common Causes
User cancelled; invalid format; expired

### How to Fix
```powershell
$cred = Get-Credential
$cred.UserName
```

### Examples
```powershell
$cred = Get-Credential -Message "Enter admin credentials"
Invoke-Command -ComputerName server -Credential $cred -ScriptBlock { Get-Process }
```
