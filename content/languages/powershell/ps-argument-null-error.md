---
title: "[Solution] Argument Null Error"
description: "Null argument errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Argument Null Error

Null argument errors.

### Common Causes
Parameter not provided; null value

### How to Fix
```powershell
function Test-NotNull {
  param([Parameter(Mandatory)][string]$Name)
  "Hello $Name"
}
```

### Examples
```powershell
if (-not $Name) { throw "Name is required" }
```
