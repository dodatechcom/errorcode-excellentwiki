---
title: "VBA Split Function Error Fix"
description: "Fix VBA Split function errors when delimiter handling returns unexpected array dimensions or empty results."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Split Function Error Fix

The Split function errors occur when the delimiter is not found in the input string, returning a single-element array instead of the expected multiple elements, or when the limit parameter causes unexpected truncation.

## Common Causes

- Delimiter character does not exist in the input string
- Using case-sensitive delimiter when data has mixed casing
- Limit parameter set too low, truncating expected elements
- Expecting Split to handle multiple delimiters (it only handles one)
- Splitting on empty string returns the full string as single element

## How to Fix

```vba
' Wrong -- assuming delimiter is always present
Dim parts() As String
parts = Split("hello world", ",")  ' parts(0) = "hello world"
Debug.Print parts(1)  ' Subscript out of range

' Correct -- check array bounds first
Dim parts() As String
parts = Split("hello world", " ")
If UBound(parts) >= 1 Then
    Debug.Print parts(1)
End If
```

```vba
' Wrong -- single delimiter only
Dim data As String
data = "apple,banana;orange"
Dim parts() As String
parts = Split(data, ",")  ' Only splits on comma

' Correct -- use Replace or multiple splits
Dim parts() As String
data = Replace(data, ";", ",")
parts = Split(data, ",")
```

## Examples

```vba
Sub Example1_BasicSplit()
    Dim csv As String
    csv = "Alice,30,Engineer"
    Dim fields() As String
    fields = Split(csv, ",")
    Debug.Print fields(0)  ' Alice
    Debug.Print fields(1)  ' 30
End Sub

Sub Example2_SplitWithLimit()
    Dim text As String
    text = "one-two-three-four-five"
    Dim parts() As String
    parts = Split(text, "-", 3)
    ' parts(0) = "one", parts(1) = "two", parts(2) = "three-four-five"
End Sub

Sub Example3_EmptyDelimiters()
    Dim text As String
    text = "A,,B,,C"
    Dim parts() As String
    parts = Split(text, ",")
    ' Returns: "A", "", "B", "", "C"
    Debug.Print UBound(parts) + 1  ' 5 elements
End Sub
```

## Related Errors

- [Subscript out of range](vba-subscript-out-of-range) -- accessing non-existent array index
- [Type mismatch](vba-type-mismatch) -- wrong data type in array
