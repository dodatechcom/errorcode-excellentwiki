---
title: "[Solution] VBA CreateObject Error"
description: "CreateObject fails to create COM object."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA CreateObject Error

CreateObject fails to create COM object.

### Common Causes
Object not registered; wrong ProgID; permissions

### How to Fix
```vba
Dim fso As Object
Set fso = CreateObject("Scripting.FileSystemObject")
```

### Examples
```vba
On Error Resume Next
Set app = CreateObject("Outlook.Application")
If app Is Nothing Then
    MsgBox "Outlook not installed"
End If
```
