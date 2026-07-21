---
title: "[Solution] VBA Early Binding Error"
description: "Early binding (WithEvents) errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Early Binding Error

Early binding (WithEvents) errors.

### Common Causes
Wrong object type; reference missing

### How to Fix
```vba
' Early binding requires reference
Dim fso As Scripting.FileSystemObject
Set fso = New Scripting.FileSystemObject
```

### Examples
```vba
' Late binding - no reference needed
Dim fso As Object
Set fso = CreateObject("Scripting.FileSystemObject")
```
