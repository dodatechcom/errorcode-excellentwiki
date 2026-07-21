---
title: "[Solution] VBA ReDim Without Dim"
description: "ReDim used on variable not previously Dim'd."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA ReDim Without Dim

ReDim used on variable not previously Dim'd.

### Common Causes
Missing Dim statement

### How to Fix
```vba
Dim arr() As Long  ' Required first
ReDim arr(1 To 100)
```

### Examples
```vba
Dim matrix() As Double
ReDim matrix(1 To 10, 1 To 10)
```
