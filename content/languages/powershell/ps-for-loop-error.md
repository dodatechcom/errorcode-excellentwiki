---
title: "[Solution] For Loop Error"
description: "For loop syntax errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# For Loop Error

For loop syntax errors.

### Common Causes
Wrong syntax; off-by-one; not iterating

### How to Fix
```powershell
for ($i = 0; $i -lt 10; $i++) { Write-Output $i }
```

### Examples
```powershell
foreach ($file in Get-ChildItem "C:\temp") { Write-Output $file.Name }
```
