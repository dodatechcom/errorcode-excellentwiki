---
title: "[Solution] VBA Runtime Error"
description: "Fix general VBA runtime errors that occur during code execution, including unhandled exceptions and invalid operations."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

VBA runtime errors occur when code encounters an invalid operation during execution. Unlike compile-time errors, these happen at runtime and can be unpredictable depending on data and state.

## Common Causes

- Division by zero
- Accessing uninitialized object variables
- Invalid file operations
- Data type mismatches
- Missing error handling

## How to Fix

```vba
' WRONG: No error handling
Sub ProcessData()
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")  ' May not exist
    ws.Range("A1").Value = 42
End Sub

' CORRECT: With error handling
Sub ProcessData()
    On Error GoTo ErrHandler
    Dim ws As Worksheet
    Set ws = Worksheets("Sheet1")
    ws.Range("A1").Value = 42
    Exit Sub
ErrHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description
End Sub
```

```vba
' WRONG: Division by zero
Sub Calc()
    Dim a, b, result
    a = 10
    b = 0
    result = a / b   ' Runtime error
End Sub

' CORRECT: Check before dividing
Sub Calc()
    Dim a, b, result
    a = 10: b = 0
    If b <> 0 Then
        result = a / b
    Else
        MsgBox "Cannot divide by zero"
    End If
End Sub
```

## Examples

```vba
Sub Example()
    Dim x As Integer
    x = 1 / 0          ' Runtime error 11: Division by zero
    Range("XFD1").Value = 1  ' Runtime error 1004: out of range
End Sub
```

## Related Errors

- [Type Mismatch](vba-type-mismatch) - type conversion errors
- [Object Required](vba-object-required) - object reference errors
