---
title: "[Solution] Array Error"
description: "Array creation and access errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Array Error

Array creation and access errors.

### Common Causes
Wrong syntax; index out of bounds; null array

### How to Fix
```powershell
$arr = @(1, 2, 3)
$arr[0]
```

### Examples
```powershell
$arr = 1..10
$arr | ForEach-Object { $_ }
```
