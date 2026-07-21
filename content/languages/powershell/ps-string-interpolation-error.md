---
title: "[Solution] String Interpolation Error"
description: "String interpolation issues."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# String Interpolation Error

String interpolation issues.

### Common Causes
Wrong quotes; nested quotes; subexpression

### How to Fix
```powershell
"Hello $name"
'Hello $name'  # literal, not interpolated
```

### Examples
```powershell
"The result is $(Get-Date -Format 'yyyy-MM-dd')"
```
