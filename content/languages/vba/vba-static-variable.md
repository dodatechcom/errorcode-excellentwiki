---
title: "[Solution] VBA Static Variable Error"
description: "Static variables not persisting between calls."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Static Variable Error

Static variables not persisting between calls.

### Common Causes
Using Dim instead of Static

### How to Fix
```vba
Static counter As Long
counter = counter + 1
```

### Examples
```vba
Function GetNextID() As Long
    Static id As Long
    id = id + 1
    GetNextID = id
End Function
```
