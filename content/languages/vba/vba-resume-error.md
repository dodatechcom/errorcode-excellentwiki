---
title: "VBA Resume Without Error Handler Fix"
description: "Fix VBA Resume without On Error GoTo error when Resume statement is used outside an active error handler."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Resume Without Error Handler Fix

The `Resume` statement can only be used inside an error handler triggered by `On Error GoTo`. Using it outside this context raises runtime error 20: "Resume without error".

## Common Causes

- `Resume` called in a Sub or Function that does not have `On Error GoTo`
- `Resume` placed after the error handler label has already been exited
- Calling a helper procedure that uses `Resume` without its own error handler
- Accidentally leaving a `Resume` in code after removing the error handler

## How to Fix

```vba
' Wrong -- Resume without On Error GoTo
Sub ProcessData()
    Resume  ' Runtime error 20
End Sub

' Correct -- Add error handler first
Sub ProcessData()
    On Error GoTo ErrHandler
    ' ... code ...
    Exit Sub
ErrHandler:
    Resume Next
End Sub
```

```vba
' Wrong -- Resume outside handler scope
Sub DoWork()
    On Error GoTo ErrHandler
    Dim x As Integer
    x = 1 / 0
    Exit Sub
ErrHandler:
    Debug.Print Err.Description
End Sub
Resume  ' Error: Resume without error

' Correct -- Keep Resume inside handler
Sub DoWork()
    On Error GoTo ErrHandler
    Dim x As Integer
    x = 1 / 0
    Exit Sub
ErrHandler:
    Debug.Print Err.Description
    Resume Next  ' Inside handler
End Sub
```

## Examples

```vba
Sub Example1_BasicHandler()
    On Error GoTo Handler
    Dim result As Double
    result = Application.WorksheetFunction.Sum(Range("A1:A10"))
    Exit Sub
Handler:
    MsgBox "Error: " & Err.Description
    Resume Next
End Sub

Sub Example2_ResumeAtLabel()
    On Error GoTo Handler
    Dim i As Long
    For i = 1 To 10
        Cells(i, 1).Value = i * 0  ' triggers error if cell locked
    Next i
    Exit Sub
Handler:
    MsgBox "Failed at row " & i
    Resume 0  ' Resume at beginning
End Sub
```

## Related Errors

- [On Error GoTo pattern](vba-on-error-goto) -- proper error handler setup
- [Error handling pattern](vba-error-handling-pattern) -- structured error handling
