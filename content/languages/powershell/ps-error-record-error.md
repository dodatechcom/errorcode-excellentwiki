---
title: "[Solution] Error Record Error"
description: "ErrorRecord object access errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Error Record Error

ErrorRecord object access errors.

### Common Causes
Wrong property; no error captured

### How to Fix
```powershell
try { 1/0 } catch { $_.Exception.Message }
```

### Examples
```powershell
try { Get-Item "C:\nonexistent" }
catch { Write-Host $_.Exception.Message }
```
