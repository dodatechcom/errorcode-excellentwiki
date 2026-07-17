---
title: "[Solution] VBA Permission Denied Error"
description: "Fix VBA Permission Denied error (Error 70) when VBA cannot access a file, folder, or resource due to permissions."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["permission-denied", "error-70", "file", "access", "vba"]
weight: 5
---

## What This Error Means

Permission Denied (Error 70) occurs when VBA tries to access a file, folder, or resource that it doesn't have permission to read, write, or modify.

## Common Causes

- File is read-only or write-protected
- File is open in another application
- Insufficient OS-level permissions
- Network drive permissions
- File path is a system directory

## How to Fix

```vba
' WRONG: No permission check
Open "C:\Windows\test.txt" For Output As #1

' CORRECT: Check file attributes first
Dim fso As Object
Set fso = CreateObject("Scripting.FileSystemObject")
If fso.FileExists("C:\path\file.txt") Then
    Open "C:\path\file.txt" For Output As #1
End If
```

```vba
' CORRECT: Check if file is already open
On Error Resume Next
Open "C:\path\file.txt" For Input As #1
If Err.Number = 70 Then
    MsgBox "File is locked by another application"
Else
    ' Process file
    Close #1
End If
On Error GoTo 0
```

## Examples

```vba
Sub Example()
    Open "C:\read-only.txt" For Output As #1
    Print #1, "Hello"   ' Error 70: Permission denied
    Close #1
End Sub
```

## Related Errors

- [File Not Found](vba-file-not-found) - file access errors
- [Runtime Error](vba-runtime-error) - general execution errors
