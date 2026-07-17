---
title: "[Solution] VBA Division by Zero Error"
description: "Fix VBA Division by Zero error (Error 11) when dividing a number by zero in VBA code."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Division by Zero (Error 11) occurs when VBA attempts to divide a number by zero. Unlike some languages that return Infinity, VBA raises a runtime error.

## Common Causes

- Divisor variable is zero
- User input resulted in zero divisor
- Computed divisor happens to be zero
- Integer division by zero

## How to Fix

```vba
' WRONG: No check
Sub Calc()
    Dim a As Double, b As Double
    a = 10: b = 0
    Debug.Print a / b   ' Error 11
End Sub

' CORRECT: Check before dividing
Sub Calc()
    Dim a As Double, b As Double
    a = 10: b = 0
    If b <> 0 Then
        Debug.Print a / b
    Else
        MsgBox "Cannot divide by zero"
    End If
End Sub
```

```vba
' Safe division function
Function SafeDiv(a As Double, b As Double) As Variant
    If b = 0 Then
        SafeDiv = CVErr(xlErrDiv0)   ' Return #DIV/0!
    Else
        SafeDiv = a / b
    End If
End Function
```

## Examples

```vba
Sub Example()
    Dim result As Double
    result = 100 / 0   ' Error 11: Division by zero
End Sub
```

## Related Errors

- [Overflow](vba-overflow) - numeric overflow errors
- [Runtime Error](vba-runtime-error) - general execution errors
