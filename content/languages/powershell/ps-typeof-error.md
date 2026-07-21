---
title: "[Solution] Type Detection Error"
description: "Type detection errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Type Detection Error

Type detection errors.

### Common Causes
Wrong type check; object type unexpected

### How to Fix
```powershell
$value.GetType()
$value -is [int]
```

### Examples
```powershell
$value -is [string]
$value -isnot [array]
```
