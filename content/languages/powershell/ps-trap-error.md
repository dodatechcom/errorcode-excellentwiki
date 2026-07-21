---
title: "[Solution] Trap Error"
description: "Trap error handling syntax errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Trap Error

Trap error handling syntax errors.

### Common Causes
Missing script block; wrong scope

### How to Fix
```powershell
trap { Write-Error "Error: $_" }
```

### Examples
```powershell
trap {
  Write-Host "Caught error: $_"
  continue
}
1/0
```
