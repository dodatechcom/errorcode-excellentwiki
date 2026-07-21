---
title: "VBA String Function Len Zero Error Fix"
description: "Fix VBA string function errors when passing empty strings to Left, Right, Mid, or InStr functions."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA String Function Len Zero Fix

String functions like Left, Right, Mid, and InStr behave unexpectedly or raise errors when the input string is empty (Len = 0) or when the length argument exceeds the string length.

## Common Causes

- Left or Right called with length greater than string length returns full string without error but confuses logic
- Mid on an empty string returns empty string but callers expect non-empty result
- InStr on empty string always returns 0, leading to logic bugs
- Left("", 1) returns "" silently, but code may assume it has content
- Negative or zero length arguments cause runtime error 5

## How to Fix

```vba
' Wrong -- not checking string length
Dim text As String
text = ""
Dim first As String
first = Left(text, 1)  ' returns "" -- may cause downstream issues

' Correct -- validate before string operations
Dim text As String
text = ""
If Len(text) > 0 Then
    first = Left(text, 1)
Else
    first = ""
End If
```

```vba
' Wrong -- negative length
Dim s As String
s = "hello"
Debug.Print Left(s, -1)  ' Runtime error 5

' Correct -- ensure non-negative length
Dim n As Long
n = -1
If n >= 0 Then
    Debug.Print Left(s, n)
End If
```

## Examples

```vba
Sub Example1_LeftRight()
    Dim s As String: s = "Hello World"
    Debug.Print Left(s, 5)   ' "Hello"
    Debug.Print Right(s, 5)  ' "World"
    Debug.Print Mid(s, 7, 3) ' "Wor"
End Sub

Sub Example2_InStr()
    Dim s As String: s = "Hello World"
    Debug.Print InStr(s, "World")  ' 7
    Debug.Print InStr(s, "xyz")    ' 0
    Debug.Print InStr(1, s, "l", vbTextCompare)  ' 3
End Sub

Sub Example3_Replace()
    Dim s As String: s = "abcabc"
    Debug.Print Replace(s, "a", "x")  ' "xbcxbc"
    Debug.Print Replace(s, "a", "", 1, 2)  ' "xbcabc" -- replaces first 2 only
End Sub
```

## Related Errors

- [Subscript out of range](vba-subscript-out-of-range) -- string index out of bounds
- [Type mismatch](vba-type-mismatch) -- wrong type for string functions
