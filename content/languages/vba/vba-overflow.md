---
title: "[Solution] VBA Overflow Error"
description: "Fix VBA Overflow error (Error 6) when a calculation exceeds the data type's maximum value."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["overflow", "error-6", "numeric", "data-type", "vba"]
weight: 5
---

## What This Error Means

Overflow (Error 6) occurs when a numeric value exceeds the maximum value that the assigned data type can hold. For example, storing a billion in an Integer (max 32,767) causes overflow.

## Common Causes

- Storing large number in small data type (Integer vs Long)
- Multiplication result too large
- Sum exceeding data type limit
- Integer intermediate calculation overflow

## How to Fix

```vba
' WRONG: Integer overflow
Dim x As Integer
x = 40000   ' Error 6 - Integer max is 32,767

' CORRECT: Use Long for larger numbers
Dim x As Long
x = 40000   ' Works fine
```

```vba
' WRONG: Integer intermediate calculation
Dim a As Integer, b As Integer, result As Long
a = 200: b = 200
result = a * b   ' 40000 exceeds Integer - overflow in intermediate

' CORRECT: Convert before calculation
result = CLng(a) * CLng(b)
```

## Examples

```vba
Sub Example()
    Dim x As Integer
    x = 32767 + 1   ' Error 6: Overflow
End Sub
```

## Related Errors

- [Division by Zero](vba-divide-by-zero) - arithmetic errors
- [Type Mismatch](vba-type-mismatch) - type errors
