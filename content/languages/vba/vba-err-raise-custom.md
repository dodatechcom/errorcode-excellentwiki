---
title: "VBA Err Raise Custom Error Number Fix"
description: "Fix VBA Err.Raise errors when raising custom error numbers that conflict with built-in VBA errors."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Err.Raise Custom Error Number Fix

Using error numbers below 50000 in Err.Raise can conflict with built-in VBA errors, causing unexpected behavior. Custom application errors should use numbers above 50000.

## Common Causes

- Custom error number overlaps with a built-in VBA error
- Forgetting to provide the source or description parameters
- Raising an error inside an error handler without Resume first
- Error number 0 does not trigger error handling
- Mixing error numbers across modules inconsistently

## How to Fix

```vba
' Wrong -- using built-in error number
Err.Raise 5  ' "Invalid procedure call" -- may confuse callers

' Correct -- use application-defined range
Const ERR_INVALID_CONFIG As Long = 50001
Err.Raise ERR_INVALID_CONFIG, "Config.Load", "Invalid configuration file"
```

```vba
' Wrong -- raising error inside handler without Resume
Handler:
    Err.Raise vbObjectError + 1001  ' nested error
    Resume Next  ' never reached

' Correct -- Resume first, then raise if needed
Handler:
    Resume ClearError
ClearError:
    Err.Raise vbObjectError + 1001, "Module.Sub", "Something went wrong"
```

## Examples

```vba
Sub Example1_RaiseError()
    Const ERR_MISSING_PARAM As Long = 50001
    Dim name As String
    If Len(name) = 0 Then
        Err.Raise ERR_MISSING_PARAM, "Example1_RaiseError", _
            "Parameter 'name' is required"
    End If
End Sub

Sub Example2_CatchCustom()
    On Error GoTo Handler
    Call Example1_RaiseError
    Exit Sub
Handler:
    If Err.Number = 50001 Then
        MsgBox "Custom error: " & Err.Description
    Else
        MsgBox "Unexpected error: " & Err.Number
    End If
    Resume Next
End Sub

Sub Example3_ErrorModule()
    ' ErrorCodes module
    Public Const ERR_FILE_OPEN As Long = 50100
    Public Const ERR_FILE_READ As Long = 50101
    Public Const ERR_FILE_WRITE As Long = 50102
End Sub
```

## Related Errors

- [Error handling pattern](vba-error-handling-pattern) -- structured error handling
- [On Error GoTo](vba-on-error-goto) -- error handler setup
