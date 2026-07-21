---
title: "[Solution] ConvertFrom-Csv Error"
description: "ConvertFrom-Csv parsing errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# ConvertFrom-Csv Error

ConvertFrom-Csv parsing errors.

### Common Causes
Wrong delimiter; missing headers

### How to Fix
```powershell
"Name,Id\nNotepad,1234" | ConvertFrom-Csv
```

### Examples
```powershell
Import-Csv "data.csv" | ForEach-Object { $_.Name }
```
