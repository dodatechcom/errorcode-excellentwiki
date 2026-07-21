---
title: "[Solution] VBA Nested With Error"
description: "Nested With blocks confusion."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Nested With Error

Nested With blocks confusion.

### Common Causes
Ambiguous reference; wrong With context

### How to Fix
```vba
With ws
    With .Range("A1")
        .Value = "Hello"
    End With
End With
```

### Examples
```vba
With ws.Range("A1")
    .Value = "Test"
    .Font.Bold = True
    .Font.Size = 14
End With
```
