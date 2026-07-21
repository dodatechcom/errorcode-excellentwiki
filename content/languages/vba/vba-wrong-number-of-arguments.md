---
title: "[Solution] VBA Wrong Number of Arguments"
description: "Function or Sub called with wrong argument count."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Wrong Number of Arguments

Function or Sub called with wrong argument count.

### Common Causes
Missing arguments; extra arguments; wrong order

### How to Fix
```vba
Function Calc(a As Double, b As Double) As Double
    Calc = a * b
End Function
```

### Examples
```vba
' Call with correct number of args
result = Calc(5, 10)
```
