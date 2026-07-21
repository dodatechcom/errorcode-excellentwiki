---
title: "[Solution] VBA Error Handling Pattern"
description: "Proper error handling patterns."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Error Handling Pattern

Proper error handling patterns.

### Common Causes
Not using On Error; swallowed errors

### How to Fix
```vba
Sub SafeDivide()
    On Error GoTo ErrHandler
    Dim result As Double
    result = 1 / 0
    Exit Sub
ErrHandler:
    MsgBox "Error: " & Err.Description
End Sub
```

### Examples
```vba
Function SafeDivide(a As Double, b As Double) As Variant
    On Error GoTo ErrHandler
    If b = 0 Then GoTo ErrHandler
    SafeDivide = a / b
    Exit Function
ErrHandler:
    SafeDivide = CVErr(xlErrDiv0)
End Function
```
