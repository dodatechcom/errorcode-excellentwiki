---
title: "[Solution] Scope Error"
description: "PowerShell scope errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Scope Error

PowerShell scope errors.

### Common Causes
Variable not visible; wrong scope

### How to Fix
```powershell
$script:myVar = "visible in script"
```

### Examples
```powershell
function Test-Scope {
  $local:var = "local"
  $script:var = "script"
  Write-Output $local:var
}
```
