---
title: "[Solution] VBA Environ Error"
description: "Environ function errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Environ Error

Environ function errors.

### Common Causes
Wrong variable name; not available

### How to Fix
```vba
Debug.Print Environ("TEMP")
Debug.Print Environ("USERNAME")
```

### Examples
```vba
Dim userPath As String
userPath = Environ("USERPROFILE") & "\Documents"
```
