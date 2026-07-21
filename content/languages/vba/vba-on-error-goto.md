---
title: "[Solution] VBA On Error Error"
description: "On Error GoTo syntax errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA On Error Error

On Error GoTo syntax errors.

### Common Causes
Missing label; Resume without error; wrong handling

### How to Fix
```vba
On Error GoTo ErrHandler
' code
Exit Sub
ErrHandler:
    MsgBox Err.Description
```

### Examples
```vba
On Error Resume Next
Set fso = CreateObject("Scripting.FileSystemObject")
If Err.Number <> 0 Then
    MsgBox "Error creating object"
End If
```
