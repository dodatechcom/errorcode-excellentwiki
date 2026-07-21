---
title: "[Solution] CmdletBinding Error"
description: "CmdletBinding attribute errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# CmdletBinding Error

CmdletBinding attribute errors.

### Common Causes
Wrong position; conflicting attributes

### How to Fix
```powershell
function Get-Item {
  [CmdletBinding()]
  param([string]$Name)
  $Name
}
```

### Examples
```powershell
function Remove-ItemSafe {
  [CmdletBinding(SupportsShouldProcess, ConfirmImpact = "High")]
  param([string]$Path)
}
```
