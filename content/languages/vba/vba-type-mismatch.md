---
title: "[Solution] VBA Type Mismatch Error"
description: "Fix VBA Type Mismatch error (Error 13) when assigning or comparing values of incompatible data types."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["type-mismatch", "error-13", "conversion", "variant", "vba"]
weight: 5
---

## What This Error Means

Type Mismatch (Error 13) occurs when VBA tries to use a value of one type where a different type is expected. This commonly happens with Variant variables, string-to-number conversions, or object assignments.

## Common Causes

- Assigning a string to a numeric variable
- Comparing incompatible types
- Using Variant with unexpected data
- Passing wrong argument type to a function
- Worksheet function returning unexpected type

## How to Fix

```vba
' WRONG: String assigned to Integer
Dim x As Integer
x = "hello"   ' Type Mismatch

' CORRECT: Validate before assignment
Dim x As Integer
Dim inputVal As String
inputVal = InputBox("Enter a number:")
If IsNumeric(inputVal) Then
    x = CInt(inputVal)
Else
    MsgBox "Please enter a valid number"
End If
```

```vba
' WRONG: Comparing string to number
Dim v As Variant
v = "abc"
If v > 10 Then ...   ' Type Mismatch

' CORRECT: Check type first
If IsNumeric(v) Then
    If CDbl(v) > 10 Then ...
End If
```

## Examples

```vba
Sub Example()
    Dim arr(1 To 5) As Integer
    Dim v As Variant
    v = arr
    Dim x As Integer
    x = v   ' Type Mismatch - can't assign array to Integer
End Sub
```

## Related Errors

- [Runtime Error](vba-runtime-error) - general execution errors
- [Object Required](vba-object-required) - object reference issues
- [Overflow](vba-overflow) - numeric overflow errors
