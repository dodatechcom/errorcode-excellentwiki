---
title: "[Solution] VBA Runtime Error 53 File Not Found Fix"
description: "Fix VBA 'Run-time error 53: File not found' when trying to open or reference a file that doesn't exist."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# VBA Runtime Error 53: File Not Found Fix

This error occurs when VBA tries to open, load, or reference a file that cannot be located at the specified path. The full message is: `Run-time error '53': File not found`.

## Description

Error 53 fires when file operations — such as `Workbooks.Open`, `Kill`, `Name`, or `Open` for input/output — cannot locate the specified file. The path may be incorrect, the file may have been moved or deleted, or the current directory may differ from what the code assumes.

## Common Causes

- **Hard-coded file path that doesn't exist** — `Workbooks.Open("C:\Data\report.xlsx")` when the file isn't at that location.
- **Missing file extension** — `Open "data" For Input` instead of `Open "data.txt" For Input`.
- **Current directory differs from expected** — using a relative path when `ChDir` hasn't been called.
- **File deleted or moved since the code was written** — the referenced file no longer exists.

## How to Fix

### Fix 1: Use the full path and verify existence

```vba
' Wrong — hard-coded path might not exist
Workbooks.Open "C:\Reports\data.xlsx"

' Correct — check before opening
Dim filePath As String
filePath = "C:\Reports\data.xlsx"
If Dir(filePath) <> "" Then
    Workbooks.Open filePath
Else
    MsgBox "File not found: " & filePath
End If
```

### Fix 2: Use `Application.GetOpenFilename` to let the user choose

```vba
' Wrong — fixed path may fail on another computer
Workbooks.Open "D:\Project\input.csv"

' Correct — prompt user
Dim selectedFile As Variant
selectedFile = Application.GetOpenFilename("Excel Files,*.xlsx;*.xls", , "Select File")
If selectedFile <> False Then
    Workbooks.Open selectedFile
End If
```

### Fix 3: Set the correct current directory

```vba
' Wrong — relative path assumes a specific current directory
Workbooks.Open "input.xlsx"

' Correct — set directory first
ChDir "C:\Reports\"
Workbooks.Open "input.xlsx"
```

### Fix 4: Include the file extension

```vba
' Wrong — missing extension
Open "C:\Data\info" For Input As #1

' Correct — include extension
Open "C:\Data\info.txt" For Input As #1
```

## Examples

```vba
Sub Example()
    ' Runtime error 53: File not found
    Workbooks.Open "C:\NonExistentFolder\workbook.xlsx"
    
    ' Runtime error 53: File not found
    Kill "C:\temp\missing.txt"
End Sub
```

## Related Errors

- [Permission Denied]({{< relref "/languages/vba/permission-denied9" >}}) — file exists but cannot be accessed due to permissions.
- [Runtime Error 1004]({{< relref "/languages/vba/runtime-error1004" >}}) — application-defined error, may occur on file operations.
