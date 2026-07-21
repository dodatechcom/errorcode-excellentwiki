---
title: "[Solution] Type Casting Error"
description: "Type casting errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Type Casting Error

Type casting errors.

### Common Causes
Incompatible types; not castable

### How to Fix
```powershell
[int]$num = "42"
[string]$str = 123
```

### Examples
```powershell
$value = [int]"42"
$value = [string]$value
```
