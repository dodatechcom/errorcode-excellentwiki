---
title: "[Solution] Argument Error"
description: "Argument validation errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Argument Error

Argument validation errors.

### Common Causes
Wrong type; mandatory missing; out of range

### How to Fix
```powershell
function Test-Args { param([string]$Name) "Hello $Name" }
```

### Examples
```powershell
function Test-Validate {
  param([ValidateRange(1,100)][int]$Count)
  1..$Count
}
```
