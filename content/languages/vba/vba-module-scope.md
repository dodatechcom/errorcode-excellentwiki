---
title: "[Solution] VBA Module Scope Error"
description: "Variable scope issues."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Module Scope Error

Variable scope issues.

### Common Causes
Wrong scope; not accessible from other modules

### How to Fix
```vba
' Public - accessible everywhere
Public gblValue As Long

' Private - only in this module
Private modValue As Long
```

### Examples
```vba
' In Module1
Public Function GetConfig() As String
    GetConfig = "value"
End Function

' In any module
Debug.Print Module1.GetConfig
```
