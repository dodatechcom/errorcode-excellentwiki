---
title: "[Solution] Throw Error"
description: "throw statement syntax errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Throw Error

throw statement syntax errors.

### Common Causes
Not in function; wrong expression

### How to Fix
```powershell
throw "Error message"
```

### Examples
```powershell
function Test-Value {
  param($x)
  if ($x -lt 0) { throw "Value must be non-negative" }
  return $x * 2
}
```
