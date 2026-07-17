---
title: "[Solution] VBA: Run-time error '13': Type mismatch"
description: "Fix VBA Run-time error 13 when a variable type doesn't match the expected type for an operation."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime-error", "type", "mismatch", "conversion", "vba"]
weight: 5
---

## What This Error Means

Run-time error '13' occurs when you try to assign a value of one type to a variable of an incompatible type, or when you pass the wrong type to a function or operation.

## Common Causes

- Assigning string to numeric variable
- Passing wrong object type to a method
- Comparing incompatible types
- Using Variant with unexpected type
- Implicit type conversion failure

## How to Fix

```vba
' WRONG: Type mismatch in assignment
Sub Example1()
    Dim x As Integer
    x = "Hello"  ' Error 13: String to Integer
End Sub

' CORRECT: Use proper conversion
Sub Example1()
    Dim x As Integer
    x = CInt("42")  ' Convert string to integer
End Sub
```

```vba
' WRONG: Comparing different types
Sub Example2()
    Dim val1 As String
    Dim val2 As Long
    val1 = "ABC"
    val2 = 123
    If val1 = val2 Then  ' Error 13
        Debug.Print "Equal"
    End If
End Sub

' CORRECT: Convert before comparing
Sub Example2()
    Dim val1 As String
    Dim val2 As Long
    val1 = "ABC"
    val2 = 123
    If val1 = CStr(val2) Then
        Debug.Print "Equal"
    End If
End Sub
```

```vba
' CORRECT: Safe type checking with Variant
Sub SafeTypeCheck()
    Dim v As Variant
    v = "123"
    If IsNumeric(v) Then
        Debug.Print CDbl(v)
    End If
End Sub
```

## Related Errors

- [Object Required](vba-object-required-v2) - object type errors
- [Overflow](vba-overflow-v2) - numeric overflow
- [Compile Error: Variable](vba-compile-error-variable) - type declaration
