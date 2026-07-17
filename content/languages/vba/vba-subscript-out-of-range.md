---
title: "[Solution] VBA Subscript Out of Range"
description: "Fix VBA Subscript Out of Range error (Error 9) when accessing array elements or collection items beyond their bounds."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Subscript Out of Range (Error 9) occurs when VBA tries to access an array element or collection item using an index that doesn't exist. This is one of the most common VBA errors.

## Common Causes

- Array index exceeds upper bound
- Accessing non-existent worksheet by name
- Collection item with wrong key
- Array not dimensioned with ReDim
- Off-by-one errors in loops

## How to Fix

```vba
' WRONG: Index exceeds array bounds
Dim arr(1 To 5) As Integer
Dim x As Integer
x = arr(10)   ' Subscript out of range

' CORRECT: Check bounds before access
If index >= LBound(arr) And index <= UBound(arr) Then
    x = arr(index)
End If
```

```vba
' WRONG: Worksheet doesn't exist
Worksheets("Sheet99").Range("A1").Value = 1

' CORRECT: Check if worksheet exists
On Error Resume Next
Dim ws As Worksheet
Set ws = Worksheets("Sheet99")
On Error GoTo 0
If Not ws Is Nothing Then
    ws.Range("A1").Value = 1
Else
    MsgBox "Sheet not found"
End If
```

## Examples

```vba
Sub Example()
    Dim arr(1 To 3) As String
    arr(1) = "a": arr(2) = "b": arr(3) = "c"
    Debug.Print arr(5)   ' Subscript out of range
End Sub
```

## Related Errors

- [Runtime Error](vba-runtime-error) - general execution errors
- [Object Required](vba-object-required) - object reference issues
