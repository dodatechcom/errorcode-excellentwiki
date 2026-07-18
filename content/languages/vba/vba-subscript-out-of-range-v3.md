---
title: "[Solution] VBA Subscript Out of Range in Array Fix"
description: "Fix VBA 'Subscript out of range' errors (error 9). Learn why array indexing fails and how to validate bounds before access."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The VBA Subscript Out of Range error (error 9) occurs when you try to access an array element using an index that does not exist. This also happens when referencing a collection item, dictionary key, or worksheet by name when it does not exist. The index is either negative, zero (for 1-based arrays), or greater than the upper bound.

## Why It Happens

- Accessing an array index beyond its declared bounds
- Referencing a worksheet, chart, or collection item by a name that does not exist
- Using `ReDim` without `Preserve` and then accessing old elements
- Loop bounds that exceed the actual array size
- Accessing a Dictionary key that was never added
- Hardcoded index values that do not account for dynamic data sizes
- Accessing `Worksheets("SheetName")` when the sheet was renamed or deleted

## How to Fix It

### Check array bounds before accessing elements

```vba
' WRONG: Hardcoded index may exceed bounds
Sub ReadValue()
    Dim arr() As Long
    ReDim arr(1 To 5)
    Dim val As Long
    val = arr(10)  ' Subscript out of range
End Sub

' CORRECT: Validate index against bounds
Sub ReadValue()
    Dim arr() As Long
    ReDim arr(1 To 5)
    Dim idx As Long
    idx = 10
    
    If idx >= LBound(arr) And idx <= UBound(arr) Then
        Dim val As Long
        val = arr(idx)
    Else
        MsgBox "Index " & idx & " is out of range (" & LBound(arr) & "-" & UBound(arr) & ")"
    End If
End Sub
```

### Check collection and dictionary keys exist

```vba
' WRONG: Accessing non-existent key
Sub ReadConfig()
    Dim cfg As Object
    Set cfg = CreateObject("Scripting.Dictionary")
    Dim val As String
    val = cfg("timeout")  ' key doesn't exist
End Sub

' CORRECT: Check before accessing
Sub ReadConfig()
    Dim cfg As Object
    Set cfg = CreateObject("Scripting.Dictionary")
    
    If cfg.Exists("timeout") Then
        Dim val As String
        val = cfg("timeout")
    Else
        val = "30"  ' default
    End If
End Sub
```

### Use dynamic loop bounds

```vba
' WRONG: Loop exceeds array size
Sub ProcessItems()
    Dim items() As String
    ReDim items(1 To 5)
    Dim i As Long
    For i = 1 To 10  ' only 5 elements
        Debug.Print items(i)
    Next i
End Sub

' CORRECT: Use UBound for loop bound
Sub ProcessItems()
    Dim items() As String
    ReDim items(1 To 5)
    Dim i As Long
    For i = LBound(items) To UBound(items)
        Debug.Print items(i)
    Next i
End Sub
```

### Verify worksheet exists before referencing

```vba
' WRONG: Worksheet may not exist
Sub GetSheetData()
    Dim ws As Worksheet
    Set ws = Worksheets("Report")  ' may not exist
    Dim val As Variant
    val = ws.Range("A1").Value
End Sub

' CORRECT: Check worksheet exists first
Sub GetSheetData()
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = Worksheets("Report")
    On Error GoTo 0
    
    If ws Is Nothing Then
        MsgBox "Worksheet 'Report' not found"
        Exit Sub
    End If
    Dim val As Variant
    val = ws.Range("A1").Value
End Sub
```

### Handle empty or uninitialized arrays

```vba
' WRONG: Accessing uninitialized array
Sub ReadData()
    Dim arr() As Variant
    Dim val As Variant
    val = arr(1)  ' array not dimensioned
End Sub

' CORRECT: Check if array is dimensioned
Sub ReadData()
    Dim arr() As Variant
    
    On Error Resume Next
    Dim lb As Long
    lb = LBound(arr)
    If Err.Number <> 0 Then
        MsgBox "Array not initialized"
        Exit Sub
    End If
    On Error GoTo 0
    
    Dim val As Variant
    val = arr(1)
End Sub
```

## Common Mistakes

- Assuming arrays always start at index 1 when they may start at 0
- Not re-checking array bounds after `ReDim Preserve`
- Hardcoding worksheet names instead of using variables
- Using `For Each` on a collection and modifying it during iteration
- Not handling the case where a Dynamic Array has zero elements

## Related Pages

- [VBA Application-Defined Error](vba-application-defined-error) - application error
- [VBA Type Mismatch](vba-type-mismatch-v3) - type error
- [VBA Invalid Use of Null](vba-invalid-use-of-null) - Null value error
- [VBA Runtime Error](vba-runtime-error) - general runtime issue
