---
title: "[Solution] Null Reference Error"
description: "Null reference errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Null Reference Error

Null reference errors.

### Common Causes
Accessing property on null; missing null check

### How to Fix
```powershell
if ($null -ne $value) { $value.Property }
```

### Examples
```powershell
$value | ForEach-Object { $_.Name }
```
