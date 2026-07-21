---
title: "[Solution] Regex Error"
description: "Regular expression errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Regex Error

Regular expression errors.

### Common Causes
Wrong syntax; not escaped; wrong match

### How to Fix
```powershell
"hello" -match "^hel"
```

### Examples
```powershell
"test123" -replace '\d+', ''
```
