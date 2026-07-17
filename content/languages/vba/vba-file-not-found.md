---
title: "[Solution] VBA File Not Found Error"
description: "Fix VBA File Not Found error (Error 53) when trying to open or access a file that doesn't exist."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["file-not-found", "error-53", "path", "file", "vba"]
weight: 5
---

## What This Error Means

File Not Found (Error 53) occurs when VBA tries to open or access a file at a path that doesn't exist on the system.

## Common Causes

- File path is incorrect (typo)
- File was moved or deleted
- Using relative path from wrong directory
- Network drive disconnected

## How to Fix

```vba
' WRONG: No file existence check
Open "C:\data\report.csv" For Input As #1

' CORRECT: Check if file exists first
If Dir("C:\data\report.csv") <> "" Then
    Open "C:\data\report.csv" For Input As #1
Else
    MsgBox "File not found: C:\data\report.csv"
End If
```

```vba
' CORRECT: Using FileSystemObject
Dim fso As Object
Set fso = CreateObject("Scripting.FileSystemObject")
If fso.FileExists("C:\data\report.csv") Then
    ' Process file
Else
    MsgBox "File does not exist"
End If
```

## Examples

```vba
Sub Example()
    Open "C:\nonexistent.txt" For Input As #1   ' Error 53
End Sub
```

## Related Errors

- [Permission Denied](vba-permission-denied) - file access errors
- [Runtime Error](vba-runtime-error) - general execution errors
