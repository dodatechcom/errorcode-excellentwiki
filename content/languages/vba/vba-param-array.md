---
title: "[Solution] VBA ParamArray Error"
description: "ParamArray parameter errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA ParamArray Error

ParamArray parameter errors.

### Common Causes
Wrong syntax; must be last parameter

### How to Fix
```vba
Function Sum(ParamArray numbers() As Variant) As Double
    Dim i As Long
    For i = LBound(numbers) To UBound(numbers)
        Sum = Sum + numbers(i)
    Next i
End Function
```

### Examples
```vba
Debug.Print Sum(1, 2, 3, 4, 5)
```
