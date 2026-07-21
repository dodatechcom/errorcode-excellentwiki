---
title: "[Solution] ConvertFrom-Json Error"
description: "ConvertFrom-Json parsing errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# ConvertFrom-Json Error

ConvertFrom-Json parsing errors.

### Common Causes
Malformed JSON; BOM; encoding

### How to Fix
```powershell
'{"name":"test"}' | ConvertFrom-Json
```

### Examples
```powershell
Invoke-RestMethod "https://api.example.com/data" | ConvertTo-Json -Depth 10
```
