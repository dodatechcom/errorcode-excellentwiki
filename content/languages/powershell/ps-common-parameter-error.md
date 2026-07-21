---
title: "[Solution] Common Parameter Error"
description: "Common parameter errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Common Parameter Error

Common parameter errors.

### Common Causes
$ErrorActionPreference; $VerbosePreference

### How to Fix
```powershell
$ErrorActionPreference = "Stop"
```

### Examples
```powershell
Get-Process -Verbose -Debug
```
