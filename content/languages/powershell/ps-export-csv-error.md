---
title: "[Solution] Export-Csv Error"
description: "Export-Csv fails to write CSV."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Export-Csv Error

Export-Csv fails to write CSV.

### Common Causes
Path not found; encoding; no objects

### How to Fix
```powershell
Get-Process | Export-Csv "C:\temp\processes.csv" -NoTypeInformation
```

### Examples
```powershell
$result | Export-Csv "C:\output\data.csv" -NoTypeInformation -Encoding UTF8
```
