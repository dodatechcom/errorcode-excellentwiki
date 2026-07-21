---
title: "[Solution] JSON Serialization Error"
description: "JSON serialization/deserialization errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# JSON Serialization Error

JSON serialization/deserialization errors.

### Common Causes
Circular reference; depth; encoding

### How to Fix
```powershell
$ht | ConvertTo-Json -Depth 5
```

### Examples
```powershell
$json = Get-Content "data.json" -Raw | ConvertFrom-Json
$json.property
```
