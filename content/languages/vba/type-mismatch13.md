---
title: "[Solution] VBA Runtime Error 13 Type Mismatch Fix"
description: "Fix VBA 'Run-time error 13: Type mismatch' when a value is assigned to an incompatible variable type."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtime-error-13", "type-mismatch", "vba"]
weight: 5
---

# VBA Runtime Error 13: Type Mismatch Fix

This error occurs when you try to assign a value to a variable of an incompatible type, or pass an argument to a function that doesn't match the expected type. The full message is: `Run-time error '13': Type mismatch`.

## Description

VBA is strongly typed in many contexts. When a `String` is expected but a `Variant` containing an object is provided, or when a number is passed where a `String` is required, this error fires. It's one of the most common VBA runtime errors.

## Common Causes

- **Assigning wrong type to typed variable** — `Dim x As Integer: x = "hello"`.
- **Cell value not converted before arithmetic** — using a cell containing text in a math operation.
- **Function return type mismatch** — a function returns a type different from what the caller expects.
- **Using `=` instead of `Like` or `StrComp` for text comparison** on non-string types.

## How to Fix

### Fix 1: Use proper type conversion functions

```vba
' Wrong — cell might contain text
Dim total As Double
total = Range("A1").Value + Range("B1").Value

' Correct — convert explicitly
Dim total As Double
total = CDbl(Range("A1").Value) + CDbl(Range("B1").Value)
```

### Fix 2: Use Variant for uncertain types

```vba
' Wrong — assuming cell contains a number
Dim val As Long
val = Range("A1").Value  ' Error if A1 contains text

' Correct — use Variant first, then check
Dim val As Variant
val = Range("A1").Value
If IsNumeric(val) Then
    Dim numVal As Long
    numVal = CLng(val)
End If
```

### Fix 3: Check variable types before operations

```vba
' Wrong
Dim result As String
result = 42 + "hello"

' Correct — validate before combining
Dim result As String
If IsNumeric(someValue) Then
    result = CStr(CDbl(someValue) + 42)
Else
    result = "Invalid input"
End If
```

### Fix 4: Ensure function return types match expectations

```vba
' Wrong — function returns Nothing
Dim ws As Worksheet
Set ws = GetSheetByName("NonExistent")  ' Returns Nothing
Debug.Print ws.Name  ' Type mismatch when accessing Nothing

' Correct — check for Nothing first
Dim ws As Worksheet
Set ws = GetSheetByName("NonExistent")
If Not ws Is Nothing Then
    Debug.Print ws.Name
End If
```

## Examples

```vba
Sub Example()
    Dim x As Integer
    x = "hello"  ' Runtime error 13: Type mismatch
    
    Dim rng As Range
    Set rng = Range("A1")
    Dim val As Double
    val = rng.Value  ' Error if A1 contains "N/A"
End Sub
```

## Related Errors

- [Subscript Out of Range]({{< relref "/languages/vba/subscript-out-of-range" >}}) — accessing a nonexistent collection element or array index.
- [Object Required]({{< relref "/languages/vba/object-required" >}}) — object variable not set.
