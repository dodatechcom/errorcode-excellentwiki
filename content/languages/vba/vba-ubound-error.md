---
title: "VBA UBound LBound Array Index Error Fix"
description: "Fix VBA UBound and LBound errors when accessing arrays with incorrect index bounds or unidimensional assumptions."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA UBound LBound Array Index Error Fix

UBound and LBound errors occur when accessing array dimensions that do not exist, or when the array has not been initialized (is empty).

## Common Causes

- Using UBound on a dynamic array that was never ReDim'd
- Passing wrong dimension index to UBound for multi-dimensional arrays
- Assuming LBound is always 0 (VBA arrays can start at any index)
- Array contains Variant containing empty after failed ReDim
- Using UBound on a fixed-size array with mismatched bounds

## How to Fix

```vba
' Wrong -- accessing uninitialized array
Dim arr() As Integer
Dim x As Integer
x = UBound(arr)  ' Error 9: array not initialized

' Correct -- check if array is initialized
Dim arr() As Integer
If IsArrayInitialized(arr) Then
    x = UBound(arr)
Else
    ReDim arr(1 To 10)
End If

Function IsArrayInitialized(arr As Variant) As Boolean
    On Error Resume Next
    Dim s As String
    s = UBound(arr)
    IsArrayInitialized = (Err.Number = 0)
    On Error GoTo 0
End Function
```

```vba
' Wrong -- wrong dimension for multi-dimensional array
Dim matrix(1 To 3, 1 To 4) As Double
Debug.Print UBound(matrix, 1)  ' 3
Debug.Print UBound(matrix, 3)  ' Error: dimension 3 does not exist

' Correct -- use proper dimension
Debug.Print UBound(matrix, 1)  ' 3 (rows)
Debug.Print UBound(matrix, 2)  ' 4 (columns)
```

## Examples

```vba
Sub Example1_BasicBounds()
    Dim arr(1 To 10) As Integer
    Debug.Print "LBound: " & LBound(arr)  ' 1
    Debug.Print "UBound: " & UBound(arr)  ' 10
End Sub

Sub Example2_DynamicArray()
    Dim arr() As String
    ReDim arr(0 To 4)
    Debug.Print LBound(arr)  ' 0
    Debug.Print UBound(arr)  ' 4
End Sub

Sub Example3_MultiDimension()
    Dim m(1 To 5, 1 To 3) As Double
    Dim r As Long, c As Long
    For r = LBound(m, 1) To UBound(m, 1)
        For c = LBound(m, 2) To UBound(m, 2)
            m(r, c) = r * c
        Next c
    Next r
End Sub
```

## Related Errors

- [Subscript out of range](vba-subscript-out-of-range) -- index beyond bounds
- [Redim without Dim](vba-redim-without-dim) -- array not declared
