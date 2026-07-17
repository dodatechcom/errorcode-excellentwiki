---
title: "[Solution] VBA Runtime Error 9 Subscript Out of Range Fix"
description: "Fix VBA 'Run-time error 9: Subscript out of range' when accessing a nonexistent index or sheet."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# VBA Runtime Error 9: Subscript Out of Range Fix

This error occurs when you try to access an element in a collection, array, or worksheet using an index or key that doesn't exist. The full message is: `Run-time error '9': Subscript out of range`.

## Description

VBA collections, arrays, and worksheet references all use indices. If you reference an index beyond the bounds of an array, a sheet name that doesn't exist, or a dictionary key that hasn't been added, this error fires. It's especially common when looping through worksheets or arrays without bounds checking.

## Common Causes

- **Referencing a worksheet that doesn't exist** — `Worksheets("Sheet99")` when only 3 sheets exist.
- **Array index out of bounds** — accessing `arr(10)` when the array has only 5 elements.
- **Dictionary key not found** — `dict("missingKey")` without checking if the key exists.
- **Off-by-one error in loops** — using 1-based index on a 0-based array or vice versa.

## How to Fix

### Fix 1: Check if a sheet exists before referencing it

```vba
' Wrong — sheet might not exist
Worksheets("Summary").Range("A1").Value = "Hello"

' Correct — check first
Function SheetExists(sheetName As String) As Boolean
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = ThisWorkbook.Worksheets(sheetName)
    SheetExists = Not ws Is Nothing
    On Error GoTo 0
End Function

If SheetExists("Summary") Then
    Worksheets("Summary").Range("A1").Value = "Hello"
End If
```

### Fix 2: Use LBound and UBound for array loops

```vba
' Wrong — hard-coded bounds
Dim arr(1 To 5) As String
For i = 1 To 10  ' Error at i = 6
    Debug.Print arr(i)
Next i

' Correct — use bounds
Dim arr(1 To 5) As String
For i = LBound(arr) To UBound(arr)
    Debug.Print arr(i)
Next i
```

### Fix 3: Check dictionary keys before access

```vba
' Wrong — key might not exist
Dim dict As Object
Set dict = CreateObject("Scripting.Dictionary")
Debug.Print dict("missingKey")

' Correct — check with Exists
If dict.Exists("missingKey") Then
    Debug.Print dict("missingKey")
Else
    Debug.Print "Key not found"
End If
```

### Fix 4: Use error handling for dynamic indices

```vba
' Correct — use On Error for safe access
On Error Resume Next
Dim ws As Worksheet
Set ws = Worksheets("DynamicSheetName")
On Error GoTo 0

If ws Is Nothing Then
    MsgBox "Sheet not found"
Else
    ws.Range("A1").Value = "Data"
End If
```

## Examples

```vba
Sub Example()
    Dim arr(1 To 3) As Integer
    arr(1) = 10
    arr(2) = 20
    arr(3) = 30
    Debug.Print arr(4)  ' Runtime error 9: Subscript out of range
    
    Worksheets("NonExistentSheet").Activate  ' Runtime error 9
End Sub
```

## Related Errors

- [Type Mismatch]({{< relref "/languages/vba/type-mismatch" >}}) — value assigned to an incompatible variable type.
- [Runtime Error 1004]({{< relref "/languages/vba/runtime-error1004" >}}) — application-defined or object-defined error.
