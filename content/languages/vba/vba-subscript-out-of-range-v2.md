---
title: "[Solution] VBA: Run-time error '9': Subscript out of range"
description: "Fix VBA Run-time error 9 when accessing an array element or collection item that doesn't exist."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Run-time error '9' occurs when you try to access an array element or collection item using an index that is outside the valid range.

## Common Causes

- Array index exceeds upper or lower bound
- Accessing non-existent collection item
- Collection item doesn't exist
- Incorrect array dimension access
- Loop boundary miscalculation

## How to Fix

```vba
' WRONG: Array index out of bounds
Sub Example1()
    Dim arr(1 To 5) As Integer
    arr(10) = 42  ' Error 9: Index 10 > 5
End Sub

' CORRECT: Check bounds first
Sub Example1()
    Dim arr(1 To 5) As Integer
    Dim idx As Integer
    idx = 10
    If idx >= LBound(arr) And idx <= UBound(arr) Then
        arr(idx) = 42
    Else
        MsgBox "Index out of range"
    End If
End Sub
```

```vba
' WRONG: Collection item doesn't exist
Sub Example2()
    Dim coll As Collection
    Set coll = New Collection
    coll.Add "First"
    Debug.Print coll(2)  ' Error 9: Only one item
End Sub

' CORRECT: Check item exists
Sub Example2()
    Dim coll As Collection
    Set coll = New Collection
    coll.Add "First"
    If coll.Count >= 2 Then
        Debug.Print coll(2)
    Else
        MsgBox "Item not found"
    End If
End Sub
```

```vba
' CORRECT: Safe collection access
Function SafeGetItem(coll As Collection, idx As Long) As Variant
    On Error Resume Next
    SafeGetItem = coll(idx)
    If Err.Number <> 0 Then
        SafeGetItem = Empty
        Err.Clear
    End If
End Function
```

## Related Errors

- [Object Not Set](vba-object-not-set-v2) - null object access
- [Array Bounds](/languages/matlab/matlab-index-out-of-range-v2) - array bounds
- [Runtime Error 91](vba-runtime-error-v2) - object not set
