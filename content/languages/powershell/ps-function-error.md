---
title: "[Solution] Function Definition Error"
description: "Function definition errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Function Definition Error

Function definition errors.

### Common Causes
Missing param block; wrong syntax

### How to Fix
```powershell
function Get-Greeting { param([string]$Name) "Hello $Name" }
```

### Examples
```powershell
function Add-Numbers {
  param([int]$a, [int]$b)
  return $a + $b
}
```
