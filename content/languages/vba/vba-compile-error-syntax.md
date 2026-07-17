---
title: "[Solution] VBA: Compile error: syntax error"
description: "Fix VBA compile error for syntax issues including missing keywords, incorrect punctuation, and malformed statements."
languages: ["vba"]
error-types: ["compile-error"]
severities: ["error"]
tags: ["compile-error", "syntax", "parse", "code", "vba"]
weight: 5
---

## What This Error Means

VBA compile errors occur when the code violates VBA syntax rules. The VBA compiler detects these before the code runs, preventing execution until fixed.

## Common Causes

- Missing keywords (Sub, End Sub, If, Then)
- Incorrect punctuation (missing colons, parentheses)
- Unclosed strings or comments
- Incorrect operator usage
- Missing line continuation character

## How to Fix

```vba
' WRONG: Missing End Sub
Sub Example1()
    MsgBox "Hello"
' Missing: End Sub

' CORRECT:
Sub Example1()
    MsgBox "Hello"
End Sub
```

```vba
' WRONG: Syntax error in If statement
Sub Example2()
    If x = 5 Then MsgBox "Five"  ' Missing Then on new line
    Else MsgBox "Not five"
End If
End Sub

' CORRECT: Proper If syntax
Sub Example2()
    If x = 5 Then
        MsgBox "Five"
    Else
        MsgBox "Not five"
    End If
End Sub
```

```vba
' WRONG: Missing line continuation
Sub Example3()
    Dim result As String
    result = "This is a very long string that " &
             "needs to continue on the next line"
End Sub

' CORRECT: Use underscore for line continuation
Sub Example3()
    Dim result As String
    result = "This is a very long string that " & _
             "needs to continue on the next line"
End Sub
```

```vba
' CORRECT: Common syntax patterns
Sub Example4()
    ' For loop
    Dim i As Integer
    For i = 1 To 10
        Debug.Print i
    Next i
    
    ' Do loop
    Do While x < 10
        x = x + 1
    Loop
    
    ' Select Case
    Select Case x
        Case 1
            Debug.Print "One"
        Case Else
            Debug.Print "Other"
    End Select
End Sub
```

## Related Errors

- [Compile Error: Variable](vba-compile-error-variable) - variable declaration
- [Compile Error: Argument](vba-compile-error-argument) - function calls
- [Runtime Error](vba-runtime-error-v2) - execution errors
