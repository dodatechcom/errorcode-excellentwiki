---
title: "[Solution] Invoke-Expression Error"
description: "Invoke-Expression (IEX) injection risks."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Invoke-Expression Error

Invoke-Expression (IEX) injection risks.

### Common Causes
Code injection; unexpected execution

### How to Fix
```powershell
Invoke-Expression "Get-Process"
```

### Examples
```powershell
$safeValue = [System.Management.Automation.Language.Parser]::ParseInput($userInput, [ref]$null, [ref]$null)
```
