---
title: "VBA Error Number to Description Lookup Fix"
description: "Fix VBA error number lookup issues when mapping Err.Number to Err.Description produces misleading messages."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Error Number to Description Lookup Fix

Err.Description does not always provide a meaningful message for application-defined errors (numbers > 50000). Using a custom error lookup table improves debugging.

## Common Causes

- Application-defined errors have generic or empty descriptions
- Err.Description may be blank after Resume Next clears the error
- Custom error numbers may conflict with built-in VBA error numbers
- Err.Description changes between VBA versions
- Not capturing error info before calling other procedures that may clear it

## How to Fix

```vba
' Wrong -- relying on generic description
On Error GoTo Handler
' ... code ...
Exit Sub
Handler:
    MsgBox "Error: " & Err.Description  ' may be empty for custom errors

' Correct -- use custom error lookup
Handler:
    MsgBox "Error " & Err.Number & ": " & GetErrorDescription(Err.Number)
    Resume Next

Function GetErrorDescription(errNum As Long) As String
    Select Case errNum
        Case 1001: GetErrorDescription = "Database connection failed"
        Case 1002: GetErrorDescription = "File not found"
        Case 1003: GetErrorDescription = "Permission denied"
        Case Else: GetErrorDescription = Err.Description
    End Select
End Function
```

```vba
' Wrong -- Err.Number cleared before logging
On Error GoTo Handler
Resume Next  ' clears error
Handler:
    LogError Err.Number  ' Err.Number is now 0

' Correct -- capture before clearing
Handler:
    Dim num As Long, desc As String
    num = Err.Number
    desc = Err.Description
    LogError num, desc
    Resume Next
```

## Examples

```vba
Sub Example1_ErrorLookup()
    On Error GoTo Handler
    Dim x As Integer
    x = CInt("abc")
    Exit Sub
Handler:
    Debug.Print "Error " & Err.Number & ": " & Err.Description
    Resume Next
End Sub

Sub Example2_CustomErrors()
    Const ERR_FILE_NOT_FOUND As Long = 1001
    Const ERR_ACCESS_DENIED As Long = 1002
    
    If Dir("C:\missing.txt") = "" Then
        Err.Raise ERR_FILE_NOT_FOUND, , "File not found: C:\missing.txt"
    End If
End Sub

Sub Example3_ErrorLog()
    On Error GoTo Handler
    Application.FileDialog(msoFileDialogOpen).Show
    Exit Sub
Handler:
    Open "C:\error.log" For Append As #1
    Print #1, Now & " - " & Err.Number & " - " & Err.Description
    Close #1
    Resume Next
End Sub
```

## Related Errors

- [Error number reference](vba-error-number) -- built-in error codes
- [Error handling pattern](vba-error-handling-pattern) -- structured error handling
