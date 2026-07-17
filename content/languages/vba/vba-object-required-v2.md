---
title: "[Solution] VBA: Run-time error '424': Object required"
description: "Fix VBA Run-time error 424 when an object is required but a value or Nothing was provided."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Run-time error '424' occurs when VBA expects an object reference but receives a value type, Nothing, or an uninitialized variable instead.

## Common Causes

- Using a method on a value instead of an object
- Object not properly initialized
- Missing object reference in method call
- Late-bound object not created
- Typo in object name

## How to Fix

```vba
' WRONG: Using value as object
Sub Example1()
    Dim x As Integer
    x = 5
    x.Name = "Test"  ' Error 424: Integer is not an object
End Sub

' CORRECT: Use actual object
Sub Example1()
    Dim ws As Worksheet
    Set ws = ActiveSheet
    ws.Name = "Test"
End Sub
```

```vba
' WRONG: Object not set
Sub Example2()
    Dim rng As Range
    rng.Value = 10  ' Error 424: rng is Nothing
End Sub

' CORRECT: Initialize object first
Sub Example2()
    Dim rng As Range
    Set rng = Range("A1")
    rng.Value = 10
End Sub
```

```vba
' CORRECT: Safe object creation
Sub SafeCreate()
    Dim obj As Object
    On Error Resume Next
    Set obj = CreateObject("Scripting.FileSystemObject")
    On Error GoTo 0
    
    If obj Is Nothing Then
        MsgBox "Failed to create object"
        Exit Sub
    End If
    
    ' Use obj safely
End Sub
```

## Related Errors

- [Object Not Set](vba-object-not-set-v2) - null object
- [Type Mismatch](vba-type-mismatch-v2) - type errors
- [Compile Error: Variable](vba-compile-error-variable) - declaration
