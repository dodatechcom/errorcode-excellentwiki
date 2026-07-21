---
title: "[Solution] VBA RegExp Error"
description: "Regular expression errors in VBA."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA RegExp Error

Regular expression errors in VBA.

### Common Causes
Wrong pattern; not creating object

### How to Fix
```vba
Dim regex As Object
Set regex = CreateObject("VBScript.RegExp")
regex.Pattern = "^\d{4}-\d{2}-\d{2}$"
regex.Global = True
```

### Examples
```vba
If regex.Test(inputStr) Then
    Debug.Print "Match found"
End If
```
