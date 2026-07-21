---
title: "VBA String Concatenation Performance Error Fix"
description: "Fix VBA string concatenation performance issues using StringBuilder pattern instead of repeated ampersand joins."
languages: ["vba"]
error-types: ["performance-error"]
severities: ["warning"]
weight: 5
---

# VBA String Concatenation Performance Fix

Repeated string concatenation with `&` in VBA creates new string objects each time, causing severe performance degradation with large numbers of concatenations. The solution uses an array or StringBuilder approach.

## Common Causes

- Loop that appends to a string variable thousands of times
- Building large SQL strings by concatenating row values
- Generating HTML or XML output by repeated concatenation
- Not pre-sizing strings or arrays
- Using string concatenation inside nested loops

## How to Fix

```vba
' Wrong -- O(n^2) string concatenation
Dim result As String
For i = 1 To 10000
    result = result & CStr(i) & ","  ' very slow
Next i

' Correct -- use array + Join for O(n) performance
Dim parts() As String
ReDim parts(1 To 10000)
For i = 1 To 10000
    parts(i) = CStr(i)
Next i
result = Join(parts, ",")
```

```vba
' Wrong -- concatenation in inner loop
Dim output As String
For Each row In rows
    For Each col In cols
        output = output & row & "," & col & vbCrLf  ' O(n^2)
    Next col
Next row

' Correct -- accumulate in array
Dim buf() As String
ReDim buf(1 To rowCount * colCount)
Dim idx As Long: idx = 1
For Each row In rows
    For Each col In cols
        buf(idx) = row & "," & col
        idx = idx + 1
    Next col
Next row
output = Join(buf, vbCrLf)
```

## Examples

```vba
Sub Example1_ArrayBuilder()
    Dim parts() As String
    ReDim parts(1 To 3)
    parts(1) = "Hello"
    parts(2) = "Beautiful"
    parts(3) = "World"
    Debug.Print Join(parts, " ")  ' "Hello Beautiful World"
End Sub

Sub Example2_CsvBuilder()
    Dim data(1 To 3) As String
    data(1) = "Name,Age,City"
    data(2) = "Alice,30,NYC"
    data(3) = "Bob,25,LA"
    Dim csv As String
    csv = Join(data, vbCrLf)
    Debug.Print csv
End Sub

Sub Example3_PerformanceTest()
    Dim t As Double: t = Timer
    Dim parts() As String
    ReDim parts(1 To 50000)
    Dim i As Long
    For i = 1 To 50000
        parts(i) = "item" & i
    Next i
    Dim result As String
    result = Join(parts, ",")
    Debug.Print "Array method: " & Format(Timer - t, "0.000") & "s"
End Sub
```

## Related Errors

- [Out of memory](vba-out-of-memory) -- memory exhaustion from string building
- [Performance error](vba-runtime-error) -- general performance issues
