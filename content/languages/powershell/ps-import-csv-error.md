---
title: "[Solution] Import-Csv Error"
description: "Import-Csv fails to parse CSV."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Import-Csv Error

Import-Csv fails to parse CSV.

### Common Causes
Wrong delimiter; encoding; header issues

### How to Fix
```powershell
Import-Csv "C:\data\file.csv"
```

### Examples
```powershell
Import-Csv "C:\data\file.csv" -Delimiter "\t" -Encoding UTF8
```
