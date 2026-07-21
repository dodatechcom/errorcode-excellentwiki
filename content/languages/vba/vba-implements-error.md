---
title: "[Solution] VBA Implements Error"
description: "Interface implementation errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Implements Error

Interface implementation errors.

### Common Causes
Missing interface; wrong method signature

### How to Fix
```vba
' Define interface in class module
' In implementing class:
Implements MyInterface
```

### Examples
```vba
Private Sub MyInterface_DoWork()
    ' implementation
End Sub
```
