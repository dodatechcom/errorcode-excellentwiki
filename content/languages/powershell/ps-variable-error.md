---
title: "[Solution] Variable Errors"
description: "Variable assignment and usage errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Variable Errors

Variable assignment and usage errors.

### Common Causes
Not declared; wrong scope; type mismatch

### How to Fix
```powershell
$value = 42
```

### Examples
```powershell
$ErrorActionPreference = "Stop"
$result = Get-Process -Name "nonexistent" -ErrorAction SilentlyContinue
```
