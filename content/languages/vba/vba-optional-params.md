---
title: "[Solution] VBA Optional Parameters"
description: "Optional parameter errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Optional Parameters

Optional parameter errors.

### Common Causes
Missing default value; wrong syntax

### How to Fix
```vba
Function Greet(name As String, Optional greeting As String = "Hello") As String
    Greet = greeting & ", " & name
End Function
```

### Examples
```vba
Debug.Print Greet("John")  ' Hello, John
Debug.Print Greet("John", "Hi")  ' Hi, John
```
