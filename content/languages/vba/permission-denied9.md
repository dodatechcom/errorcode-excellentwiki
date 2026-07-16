---
title: "[Solution] VBA Runtime Error 70 Permission Denied Fix"
description: "Fix VBA 'Run-time error 70: Permission denied' when trying to access a file, registry key, or resource that is protected."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtime-error-70", "permission-denied", "vba"]
weight: 5
---

# VBA Runtime Error 70: Permission Denied Fix

This error occurs when VBA attempts to access a file, folder, registry entry, or other resource that the current user does not have permission to read, write, or modify. The full message is: `Run-time error '70': Permission denied`.

## Description

Error 70 typically occurs in file I/O operations when the file is read-only, locked by another process, or located in a protected directory. It can also occur when trying to write to the Windows Registry without the necessary privileges, or when attempting to modify a document property on a protected document.

## Common Causes

- **File is read-only** — trying to write to or delete a file with the read-only attribute set.
- **File is locked by another process** — another application (or the same VBA project) has the file open.
- **Insufficient OS permissions** — the user account lacks write access to the target directory.
- **Trying to write to a protected location** — attempting to save to `C:\Program Files` or `C:\Windows` without elevation.

## How to Fix

### Fix 1: Remove read-only attribute before writing

```vba
' Wrong — fails on read-only files
Kill "C:\Reports\protected.xlsx"

' Correct — remove read-only attribute first
Dim filePath As String
filePath = "C:\Reports\protected.xlsx"
If GetAttr(filePath) And vbReadOnly Then
    SetAttr filePath, vbNormal
End If
Kill filePath
```

### Fix 2: Check if the file is already open

```vba
' Wrong — file might be in use
Open "C:\Reports\data.xlsx" For Binary Access Write As #1

' Correct — try with error handling
On Error Resume Next
Open "C:\Reports\data.xlsx" For Binary Access Write As #1
If Err.Number = 70 Then
    MsgBox "File is in use by another process"
    Close #1
Else
    ' Proceed with file operations
    Put #1, , someData
    Close #1
End If
```

### Fix 3: Use a writable location

```vba
' Wrong — writing to a protected system directory
Open "C:\Program Files\output.txt" For Output As #1

' Correct — write to user's temp or documents folder
Dim tempPath As String
tempPath = Environ("TEMP") & "\output.txt"
Open tempPath For Output As #1
```

### Fix 4: Run Excel as administrator or adjust permissions

```vba
' Check if running with administrative rights
' (VBA cannot directly elevate privileges)

Dim isAdmin As Boolean
On Error Resume Next
' Try writing to a test location in Program Files
Open Environ("ProgramFiles") & "\test.tmp" For Output As #1
If Err.Number <> 0 Then
    MsgBox "Please run Excel as Administrator to access this location"
Else
    Close #1
    Kill Environ("ProgramFiles") & "\test.tmp"
End If
```

## Examples

```vba
Sub Example()
    ' Runtime error 70: Permission denied
    SetAttr "C:\Reports\locked.xlsx", vbReadOnly
    Kill "C:\Reports\locked.xlsx"  ' Error 70
    
    ' Runtime error 70: Permission denied
    Open "\\server\readonlyshare\output.txt" For Output As #1  ' Network folder may be read-only
End Sub
```

## Related Errors

- [File Not Found]({{< relref "/languages/vba/file-not-found5" >}}) — file cannot be located at the specified path.
- [Runtime Error 1004]({{< relref "/languages/vba/runtime-error1004" >}}) — application-defined error during file operations.
