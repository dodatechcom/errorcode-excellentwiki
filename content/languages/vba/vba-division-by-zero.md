---
title: "[Solution] VBA Division By Zero"
description: "Division by zero error."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Division By Zero

Division by zero error.

### Common Causes
Denominator not checked; zero value

### How to Fix
```vba
If divisor <> 0 Then
    result = numerator / divisor
End If
```

### Examples
```vba
Dim a As Double, b As Double
a = 10: b = 2
If b <> 0 Then Debug.Print a / b
```
