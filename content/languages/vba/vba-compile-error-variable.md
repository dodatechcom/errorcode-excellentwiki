---
title: "[Solution] VBA: Compile error: variable not defined"
description: "Fix VBA compile error when Option Explicit is used and a variable hasn't been declared with Dim."
languages: ["vba"]
error-types: ["compile-error"]
severities: ["error"]
tags: ["compile-error", "variable", "not-defined", "option-explicit", "vba"]
weight: 5
---

## What This Error Means

This compile error occurs when `Option Explicit` is used (which is recommended) and a variable is used without being declared first with `Dim`, `Private`, `Public`, or `Static`.

## Common Causes

- Option Explicit at top of module
- Variable name typo
- Missing Dim statement
- Variable declared in wrong scope
- Using undeclared variable name

## How to Fix

```vba
' WRONG: Variable not declared
Option Explicit

Sub Example1()
    x = 5  ' Error: x not declared
    MsgBox x
End Sub

' CORRECT: Declare variable
Option Explicit

Sub Example1()
    Dim x As Integer
    x = 5
    MsgBox x
End Sub
```

```vba
' WRONG: Typo in variable name
Option Explicit

Sub Example2()
    Dim userName As String
    userName = "John"
    Debug.Print userNane  ' Error: typo
End Sub

' CORRECT: Match variable name exactly
Option Explicit

Sub Example2()
    Dim userName As String
    userName = "John"
    Debug.Print userName
End Sub
```

```vba
' CORRECT: Declare all variables at top
Option Explicit

Sub Example3()
    Dim ws As Worksheet
    Dim rng As Range
    Dim i As Long
    Dim result As Double
    
    Set ws = ActiveSheet
    Set rng = ws.Range("A1:A10")
    
    For i = 1 To 10
        result = result + rng.Cells(i, 1).Value
    Next i
End Sub
```

```vba
' CORRECT: Module-level declarations
Option Explicit

Private mCounter As Long
Private mUserName As String

Public Sub UpdateCounter()
    mCounter = mCounter + 1
End Sub
```

## Related Errors

- [Compile Error: Syntax](vba-compile-error-syntax) - syntax issues
- [Compile Error: Argument](vba-compile-error-argument) - function issues
- [Type Mismatch](vba-type-mismatch-v2) - type errors
