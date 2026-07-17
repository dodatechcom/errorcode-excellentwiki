---
title: "[Solution] VBA: Run-time error '70': Permission denied"
description: "Fix VBA Run-time error 70 when VBA cannot access a file, folder, or resource due to permission restrictions."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime-error", "permission", "denied", "access", "file", "vba"]
weight: 5
---

## What This Error Means

Run-time error '70' occurs when VBA attempts to access a file, folder, or resource that is locked, read-only, or restricted by operating system permissions.

## Common Causes

- File already open by another process
- File or folder is read-only
- Insufficient Windows permissions
- Antivirus blocking access
- File locked by another user

## How to Fix

```vba
' WRONG: Not handling locked files
Sub Example1()
    Open "C:\data\report.txt" For Output As #1
    Print #1, "Hello"  ' Error 70 if file is locked
    Close #1
End Sub

' CORRECT: Check if file is accessible
Sub Example1()
    Dim fNum As Integer
    fNum = FreeFile
    
    On Error Resume Next
    Open "C:\data\report.txt" For Output As #fNum
    If Err.Number = 70 Then
        MsgBox "File is locked by another process"
        Exit Sub
    End If
    On Error GoTo 0
    
    Print #fNum, "Hello"
    Close #fNum
End Sub
```

```vba
' CORRECT: Kill existing file before writing
Sub Example2()
    Dim filePath As String
    filePath = "C:\data\report.txt"
    
    If Dir(filePath) <> "" Then
        Kill filePath  ' Delete existing file
    End If
    
    Open filePath For Output As #1
    Print #1, "New content"
    Close #1
End Sub
```

```vba
' CORRECT: Use FileSystemObject for better control
Sub Example3()
    Dim fso As Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    
    If fso.FileExists("C:\data\file.txt") Then
        Dim f As Object
        Set f = fso.GetFile("C:\data\file.txt")
        
        If f.Attributes And 1 Then  ' Read-only
            f.Attributes = f.Attributes Xor 1  ' Remove read-only
        End If
    End If
End Sub
```

## Related Errors

- [File Not Found](vba-file-not-found-v2) - missing files
- [Compile Error: Argument](vba-compile-error-argument) - file operations
- [ADO Connection Error](vba-adodb-connection-error) - database access
