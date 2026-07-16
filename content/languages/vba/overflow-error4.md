---
title: "[Solution] VBA Runtime Error 6 Overflow Fix"
description: "Fix VBA 'Run-time error 6: Overflow' when a numeric value exceeds the range of the target data type."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtime-error-6", "overflow", "vba"]
weight: 5
---

# VBA Runtime Error 6: Overflow Fix

This error occurs when a numeric value is too large or too small for the variable type it is being assigned to. The full message is: `Run-time error '6': Overflow`.

## Description

Each VBA numeric data type has a finite range. An `Integer` can hold values from -32,768 to 32,767, a `Long` from -2,147,483,648 to 2,147,483,647, and so on. When a calculation produces a result outside that range — or when a division by zero occurs — VBA raises an overflow error.

## Common Causes

- **Integer variable exceeds its limit** — assigning a value larger than 32,767 to an `Integer`.
- **Division by zero** — denominator in a calculation evaluates to zero.
- **Intermediate calculation overflow** — a large intermediate result before the final result fits in the variable.
- **Using Integer instead of Long for large numbers** — `Integer` is often too small for worksheet row counts.

## How to Fix

### Fix 1: Use Long instead of Integer

```vba
' Wrong — Integer overflows at 32,767
Dim rowCount As Integer
rowCount = Range("A1:A50000").Rows.Count

' Correct — use Long for large values
Dim rowCount As Long
rowCount = Range("A1:A50000").Rows.Count
```

### Fix 2: Check for division by zero

```vba
' Wrong — denominator might be zero
Dim result As Double
result = 100 / someVariable

' Correct — check first
Dim result As Double
If someVariable <> 0 Then
    result = 100 / someVariable
Else
    MsgBox "Division by zero"
End If
```

### Fix 3: Use Double or Currency for larger ranges

```vba
' Wrong — Long overflows with very large values
Dim bigNum As Long
bigNum = 10 ^ 15

' Correct — use Double
Dim bigNum As Double
bigNum = 10 ^ 15
```

### Fix 4: Use CLng for safe conversion

```vba
' Wrong — direct assignment may overflow
Dim total As Long
total = Range("A1").Value * 1000

' Correct — convert with CLng, check for errors
On Error Resume Next
Dim total As Long
total = CLng(Range("A1").Value * 1000)
If Err.Number <> 0 Then
    MsgBox "Value too large for Long type"
End If
```

## Examples

```vba
Sub Example()
    Dim smallNum As Integer
    smallNum = 40000  ' Runtime error 6: Overflow (max is 32767)
    
    Dim result As Integer
    result = 200 * 200  ' Runtime error 6: Overflow (40000 > 32767)
    
    Dim divisor As Integer
    divisor = 0
    result = 100 / divisor  ' Runtime error 6: Overflow
End Sub
```

## Related Errors

- [Type Mismatch]({{< relref "/languages/vba/type-mismatch13" >}}) — incompatible types in an assignment or expression.
- [Runtime Error 1004]({{< relref "/languages/vba/runtime-error1004" >}}) — application-defined error that may occur in calculations.
