---
title: "[Solution] Interface Definition Error"
description: "Interface definition errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Interface Definition Error

Interface definition errors.

### Common Causes
Missing method; wrong syntax

### How to Fix
```powershell
interface ILogger {
  void Log([string]$message)
}
```

### Examples
```powershell
function Write-Log([string]$msg) { $msg }
```
