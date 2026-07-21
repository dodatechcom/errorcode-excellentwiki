---
title: "[Solution] Encoding Error"
description: "Character encoding errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Encoding Error

Character encoding errors.

### Common Causes
Wrong encoding; BOM; UTF-8 issues

### How to Fix
```powershell
Get-Content "file.txt" -Encoding UTF8
```

### Examples
```powershell
Set-Content "file.txt" -Value "Hello" -Encoding UTF8
```
