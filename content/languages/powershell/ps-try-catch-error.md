---
title: "[Solution] Try/Catch Error"
description: "Try/Catch block syntax errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Try/Catch Error

Try/Catch block syntax errors.

### Common Causes
Missing catch; wrong exception type

### How to Fix
```powershell
try { Get-Item "C:\missing" -ErrorAction Stop }
catch [System.IO.FileNotFoundException] { "Not found" }
```

### Examples
```powershell
try {
  $result = 1 / 0
} catch {
  Write-Error "Division by zero"
}
```
