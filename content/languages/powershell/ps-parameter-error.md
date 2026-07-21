---
title: "[Solution] Parameter Binding Error"
description: "Parameter binding errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Parameter Binding Error

Parameter binding errors.

### Common Causes
Wrong type; value not accepted; mandatory missing

### How to Fix
```powershell
Get-Process -Name "notepad"
```

### Examples
```powershell
function Test-Param {
  param([Parameter(Mandatory)][string]$Name)
  Write-Output "Name: $Name"
}
```
