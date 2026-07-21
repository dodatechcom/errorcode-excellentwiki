---
title: "[Solution] Parameter Attribute Error"
description: "Parameter attribute errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Parameter Attribute Error

Parameter attribute errors.

### Common Causes
Wrong validation; conflicting attributes

### How to Fix
```powershell
function Test {
  param([ValidateRange(1,100)][int]$Count)
  $Count
}
```

### Examples
```powershell
function Test {
  param([ValidateSet("A","B","C")][string]$Choice)
  $Choice
}
```
