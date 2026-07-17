---
title: "[Solution] VBA: Compile error: wrong number of arguments"
description: "Fix VBA compile error when calling a function or Sub with incorrect number or types of arguments."
languages: ["vba"]
error-types: ["compile-error"]
severities: ["error"]
tags: ["compile-error", "argument", "parameter", "function", "vba"]
weight: 5
---

## What This Error Means

This compile error occurs when you call a Sub or Function with a different number of arguments than it expects, or when required arguments are missing.

## Common Causes

- Missing required arguments
- Extra arguments passed
- Optional argument not provided when required
- Function signature changed
- Wrong argument order

## How to Fix

```vba
' WRONG: Missing required argument
Sub Example1()
    MsgBox  ' Error: MsgBox requires prompt argument
End Sub

' CORRECT: Provide required arguments
Sub Example1()
    MsgBox "Hello World"
End Sub
```

```vba
' WRONG: Extra arguments
Sub Example2()
    Dim result As Integer
    result = Abs(-5, 10)  ' Error: Abs takes only 1 argument
End Sub

' CORRECT: Correct number of arguments
Sub Example2()
    Dim result As Integer
    result = Abs(-5)  ' OK: 1 argument
End Sub
```

```vba
' CORRECT: Handle optional arguments
Function SafeProcess(data As Variant, Optional output As String = "") As Variant
    If output = "" Then
        SafeProcess = data
    Else
        SafeProcess = output & ": " & CStr(data)
    End If
End Function

Sub Example3()
    ' Call with optional argument
    Debug.Print SafeProcess(42)  ' OK
    Debug.Print SafeProcess(42, "Result")  ' OK
End Sub
```

```vba
' CORRECT: Check function signature
Sub Example4()
    ' Use Object Browser (F2) to check:
    ' - Number of arguments
    ' - Required vs Optional
    ' - Argument types
    
    ' Example: WorksheetFunction.VLookup
    Dim result As Variant
    result = Application.WorksheetFunction.VLookup( _
        "Key", Range("A1:B10"), 2, False)
End Sub
```

## Related Errors

- [Compile Error: Syntax](vba-compile-error-syntax) - syntax issues
- [Compile Error: Variable](vba-compile-error-variable) - declaration
- [Type Mismatch](vba-type-mismatch-v2) - argument types
