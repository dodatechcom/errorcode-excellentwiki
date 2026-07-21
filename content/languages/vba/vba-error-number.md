---
title: "[Solution] VBA Error Number Error"
description: "Wrong error number handling."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Error Number Error

Wrong error number handling.

### Common Causes
Not checking Err.Number; wrong error code

### How to Fix
```vba
On Error Resume Next
' risky operation
If Err.Number <> 0 Then
    Debug.Print "Error " & Err.Number & ": " & Err.Description
End If
```

### Examples
```vba
Const ERR_FILE_NOT_FOUND = 53
If Err.Number = ERR_FILE_NOT_FOUND Then
    MsgBox "File not found"
End If
```
