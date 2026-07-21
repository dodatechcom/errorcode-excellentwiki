---
title: "[Solution] If/Else Statement Error"
description: "If/Else syntax errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# If/Else Statement Error

If/Else syntax errors.

### Common Causes
Missing braces; wrong comparison operator

### How to Fix
```powershell
if ($value -gt 10) { "big" } else { "small" }
```

### Examples
```powershell
if ($value -eq $null) { Write-Warning "Null value" }
```
