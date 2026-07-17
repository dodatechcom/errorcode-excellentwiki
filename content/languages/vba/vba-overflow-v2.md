---
title: "[Solution] VBA: Run-time error '6': Overflow"
description: "Fix VBA Run-time error 6 when a numeric value exceeds the data type's maximum capacity."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime-error", "overflow", "numeric", "data-type", "vba"]
weight: 5
---

## What This Error Means

Run-time error '6' occurs when the result of a calculation exceeds the maximum value that the variable's data type can hold.

## Common Causes

- Result exceeds Integer range (-32,768 to 32,767)
- Multiplication producing very large numbers
- Using wrong data type for calculations
- Accumulated values in loops

## How to Fix

```vba
' WRONG: Integer overflow
Sub Example1()
    Dim x As Integer
    x = 40000  ' Error 6: Exceeds Integer max
End Sub

' CORRECT: Use Long or Double
Sub Example1()
    Dim x As Long
    x = 40000  ' OK: Long max is ~2.1 billion
End Sub
```

```vba
' WRONG: Multiplication overflow
Sub Example2()
    Dim a As Integer, b As Integer, result As Integer
    a = 200
    b = 200
    result = a * b  ' Error 6: 40000 > 32767
End Sub

' CORRECT: Use larger data type
Sub Example2()
    Dim a As Integer, b As Integer
    Dim result As Long
    a = 200
    b = 200
    result = CLng(a) * CLng(b)  ' 40000 - OK
End Sub
```

```vba
' CORRECT: Use Double for large calculations
Sub Example3()
    Dim largeVal As Double
    largeVal = 9999999999#  ' No overflow with Double
    Debug.Print largeVal
End Sub
```

## Related Errors

- [Division by Zero](vba-divide-by-zero-v2) - arithmetic errors
- [Type Mismatch](vba-type-mismatch-v2) - type conversion
- [Out of Memory](vba-out-of-memory-v2) - memory limits
