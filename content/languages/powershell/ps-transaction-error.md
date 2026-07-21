---
title: "[Solution] Transaction Error"
description: "PowerShell transaction errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Transaction Error

PowerShell transaction errors.

### Common Causes
Not started; not supported; commit/rollback

### How to Fix
```powershell
Start-Transaction
Use-Transaction -TransactedScript { New-Item "C:\temp\trans.txt" }
Complete-Transaction
```

### Examples
```powershell
Start-Transaction
try {
  Use-Transaction { New-Item "C:\temp\test.txt" }
  Complete-Transaction
} catch { Undo-Transaction }
```
