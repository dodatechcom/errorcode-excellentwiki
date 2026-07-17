---
title: "[Solution] VBA: Run-time error '11': Division by zero"
description: "Fix VBA Run-time error 11 when dividing a number by zero."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime-error", "division", "zero", "arithmetic", "vba"]
weight: 5
---

## What This Error Means

Run-time error '11' occurs when you attempt to divide a number by zero. This is undefined mathematically and causes a runtime exception.

## Common Causes

- Variable holding zero used as divisor
- Empty cell used in calculation
- Uninitialized variable (default 0)
- Result of previous calculation is zero
- Missing input validation

## How to Fix

```vba
' WRONG: No zero check
Sub Example1()
    Dim a As Double, b As Double
    a = 10
    b = 0
    Debug.Print a / b  ' Error 11
End Sub

' CORRECT: Check before dividing
Sub Example1()
    Dim a As Double, b As Double
    a = 10
    b = 0
    If b <> 0 Then
        Debug.Print a / b
    Else
        MsgBox "Cannot divide by zero"
    End If
End Sub
```

```vba
' CORRECT: Safe division function
Function SafeDivide(a As Double, b As Double) As Variant
    If b <> 0 Then
        SafeDivide = a / b
    Else
        SafeDivide = CVErr(xlErrDiv0)  ' Return #DIV/0! error
    End If
End Function
```

```vba
' CORRECT: Check cells before calculation
Sub Example2()
    Dim dividend As Double, divisor As Double
    dividend = Range("A1").Value
    divisor = Range("B1").Value
    
    If divisor <> 0 Then
        Range("C1").Value = dividend / divisor
    Else
        Range("C1").Value = "N/A"
    End If
End Sub
```

## Related Errors

- [Overflow](vba-overflow-v2) - numeric overflow
- [Type Mismatch](vba-type-mismatch-v2) - type errors
- [Runtime Error 11](/languages/fortran/fortran-division-by-zero-v2) - division by zero
