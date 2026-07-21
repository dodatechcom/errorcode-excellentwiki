---
title: "[Solution] VBA GetObject Error"
description: "GetObject fails to retrieve running object."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA GetObject Error

GetObject fails to retrieve running object.

### Common Causes
Object not running; wrong path

### How to Fix
```vba
Dim xlApp As Object
Set xlApp = GetObject(, "Excel.Application")
```

### Examples
```vba
On Error Resume Next
Set xlApp = GetObject(, "Excel.Application")
If xlApp Is Nothing Then
    Set xlApp = CreateObject("Excel.Application")
End If
```
