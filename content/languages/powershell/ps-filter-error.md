---
title: "[Solution] Filter Definition Error"
description: "Filter definition errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Filter Definition Error

Filter definition errors.

### Common Causes
Missing filter keyword; wrong syntax

### How to Fix
```powershell
filter Get-Odd { if ($_ % 2 -ne 0) { $_ } }
```

### Examples
```powershell
filter Measure-String {
  param([string]$text)
  $text.Length
}
```
