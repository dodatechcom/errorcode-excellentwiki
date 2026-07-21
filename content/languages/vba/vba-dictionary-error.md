---
title: "[Solution] VBA Dictionary Error"
description: "Scripting.Dictionary errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Dictionary Error

Scripting.Dictionary errors.

### Common Causes
Key not found; wrong comparison mode

### How to Fix
```vba
Dim dict As Object
Set dict = CreateObject("Scripting.Dictionary")
dict.Add "key1", "value1"
If dict.Exists("key1") Then
    Debug.Print dict("key1")
End If
```

### Examples
```vba
dict.CompareMode = 1  ' Text compare
Debug.Print dict.Keys
```
