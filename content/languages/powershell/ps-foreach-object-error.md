---
title: "[Solution] ForEach-Object Error"
description: "ForEach-Object script block errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# ForEach-Object Error

ForEach-Object script block errors.

### Common Causes
Missing script block; wrong variable

### How to Fix
```powershell
1..10 | ForEach-Object { Write-Output $_ }
```

### Examples
```powershell
Get-ChildItem *.txt | ForEach-Object { Get-Content $_.FullName }
```
