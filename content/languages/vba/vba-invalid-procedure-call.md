---
title: "[Solution] VBA Invalid Procedure Call"
description: "Function called with invalid argument value."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Invalid Procedure Call

Function called with invalid argument value.

### Common Causes
Out of range value; wrong format

### How to Fix
```vba
Dim d As Date
d = DateSerial(2024, 1, 15)
```

### Examples
```vba
' Check argument validity before calling
If IsDate(dateStr) Then
    d = CDate(dateStr)
End If
```
