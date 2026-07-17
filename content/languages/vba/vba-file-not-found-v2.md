---
title: "[Solution] VBA: Run-time error '53': File not found"
description: "Fix VBA Run-time error 53 when a file path doesn't exist or the file cannot be located."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime-error", "file", "not-found", "path", "directory", "vba"]
weight: 5
---

## What This Error Means

Run-time error '53' occurs when VBA tries to open a file that doesn't exist at the specified path. This is common with hardcoded file paths.

## Common Causes

- File moved or deleted
- Incorrect file path
- Typo in filename
- File on network drive not mapped
- Relative path resolving incorrectly

## How to Fix

```vba
' WRONG: Hardcoded path without checking
Sub Example1()
    Open "C:\data\report.xlsx" For Input As #1  ' Error 53
    Close #1
End Sub

' CORRECT: Check if file exists first
Sub Example1()
    Dim filePath As String
    filePath = "C:\data\report.xlsx"
    
    If Dir(filePath) <> "" Then
        Open filePath For Input As #1
        Close #1
    Else
        MsgBox "File not found: " & filePath
    End If
End Sub
```

```vba
' CORRECT: Use FileDialog for user selection
Sub Example2()
    Dim fd As FileDialog
    Set fd = Application.FileDialog(msoFileDialogFilePicker)
    
    With fd
        .Title = "Select a file"
        .Filters.Clear
        .Filters.Add "Excel Files", "*.xlsx;*.xls"
        
        If .Show = -1 Then
            Open .SelectedItems(1) For Input As #1
            Close #1
        Else
            MsgBox "No file selected"
        End If
    End With
End Sub
```

```vba
' CORRECT: Safe file open wrapper
Function SafeOpenFile(filePath As String) As Boolean
    SafeOpenFile = False
    
    If Dir(filePath) = "" Then
        MsgBox "File not found: " & filePath
        Exit Function
    End If
    
    On Error GoTo ErrHandler
    Open filePath For Input As #1
    SafeOpenFile = True
    Exit Function
    
ErrHandler:
    MsgBox "Cannot open file: " & Err.Description
End Function
```

## Related Errors

- [Permission Denied](vba-permission-denied-v2) - access issues
- [ADO Connection Error](vba-adodb-connection-error) - database files
- [Shell Error](vba-shell-error) - process/file access
