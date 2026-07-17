---
title: "[Solution] VBA: Run-time error '91': Object variable not set"
description: "Fix VBA Run-time error 91 when an object variable has not been set with the Set statement."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime-error", "object", "not-set", "nothing", "set", "vba"]
weight: 5
---

## What This Error Means

Run-time error '91' occurs when you attempt to use an object variable that is Nothing (not set). This is similar to accessing a null pointer in other languages.

## Common Causes

- Forgetting `Set` keyword when assigning objects
- Object returned as Nothing from function
- Collection item doesn't exist
- Worksheet or range not found
- Object was set to Nothing explicitly

## How to Fix

```vba
' WRONG: Missing Set keyword
Sub Example1()
    Dim ws As Worksheet
    ws = Worksheets("Data")  ' Error 91
End Sub

' CORRECT: Use Set
Sub Example1()
    Dim ws As Worksheet
    Set ws = Worksheets("Data")
End Sub
```

```vba
' WRONG: Not checking for Nothing
Sub Example2()
    Dim ws As Worksheet
    Set ws = Worksheets("NonExistent")
    ws.Range("A1").Value = 5  ' Error 91
End Sub

' CORRECT: Always check
Sub Example2()
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = Worksheets("NonExistent")
    On Error GoTo 0
    
    If Not ws Is Nothing Then
        ws.Range("A1").Value = 5
    Else
        MsgBox "Worksheet not found"
    End If
End Sub
```

```vba
' CORRECT: Safe wrapper function
Function GetWorksheet(name As String) As Worksheet
    On Error Resume Next
    Set GetWorksheet = ThisWorkbook.Worksheets(name)
    On Error GoTo 0
End Function
```

## Related Errors

- [Object Required](vba-object-required-v2) - object reference
- [Type Mismatch](vba-type-mismatch-v2) - type conversion
- [Runtime Error 91](vba-runtime-error-v2) - object not set
