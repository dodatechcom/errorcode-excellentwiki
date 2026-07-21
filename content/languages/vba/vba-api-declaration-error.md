---
title: "[Solution] VBA API Declaration Error"
description: "Windows API declaration errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA API Declaration Error

Windows API declaration errors.

### Common Causes
Wrong calling convention; wrong types

### How to Fix
```vba
#If VBA7 Then
    Private Declare PtrSafe Function FindWindow Lib "user32" Alias "FindWindowA" _
        (ByVal lpClassName As String, ByVal lpWindowName As String) As LongPtr
#Else
    Private Declare Function FindWindow Lib "user32" Alias "FindWindowA" _
        (ByVal lpClassName As String, ByVal lpWindowName As String) As Long
#End If
```

### Examples
```vba
Declare PtrSafe Function GetTickCount Lib "kernel32" () As Long
```
