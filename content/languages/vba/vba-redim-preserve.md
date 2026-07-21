---
title: "[Solution] VBA ReDim Preserve Error"
description: "ReDim Preserve errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA ReDim Preserve Error

ReDim Preserve errors.

### Common Causes
Wrong syntax; cannot change dimensions

### How to Fix
```vba
Dim arr() As Long
ReDim arr(1 To 10)
ReDim Preserve arr(1 To 20)  ' OK
```

### Examples
```vba
' Can only change last dimension
Dim arr() As Long
ReDim arr(1 To 10, 1 To 5)
ReDim Preserve arr(1 To 10, 1 To 10)  ' OK
```
