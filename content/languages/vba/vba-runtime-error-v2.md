---
title: "[Solution] VBA: Run-time error '91': Object variable not set"
description: "Fix VBA Run-time error 91 when an object variable has not been set with the Set statement before use."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime-error", "object", "variable", "not-set", "vba"]
weight: 5
---

## What This Error Means

Run-time error '91' occurs when you use an object variable that hasn't been assigned using the `Set` keyword. Unlike value types, object variables must be explicitly initialized before use.

## Common Causes

- Forgetting to use `Set` when assigning object variables
- Object returned from a function is Nothing
- Object was set but later set to Nothing
- Late-bound object creation failure
- Accessing collection item that doesn't exist

## How to Fix

```vba
' WRONG: Missing Set statement
Sub Example1()
    Dim ws As Worksheet
    ws = Worksheets("Sheet1")  ' Error 91
End Sub

' CORRECT: Use Set keyword
Sub Example1()
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    ws.Range("A1").Value = "Hello"
End Sub
```

```vba
' WRONG: Not checking for Nothing
Sub Example2()
    Dim rng As Range
    Set rng = Nothing
    rng.Value = 5  ' Error 91
End Sub

' CORRECT: Check before use
Sub Example2()
    Dim rng As Range
    Set rng = Nothing
    If Not rng Is Nothing Then
        rng.Value = 5
    Else
        MsgBox "Range not set"
    End If
End Sub
```

```vba
' CORRECT: Safe object assignment pattern
Sub SafeAssignment()
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = ThisWorkbook.Worksheets("Data")
    On Error GoTo 0
    
    If ws Is Nothing Then
        Set ws = ThisWorkbook.Worksheets.Add
        ws.Name = "Data"
    End If
End Sub
```

## Related Errors

- [Type Mismatch](vba-type-mismatch-v2) - type conversion errors
- [Object Required](vba-object-required-v2) - object reference errors
- [Subscript Out of Range](vba-subscript-out-of-range-v2) - collection/array errors
