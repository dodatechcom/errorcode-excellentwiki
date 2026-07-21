---
title: "[Solution] VBA Find Method Error"
description: "Find method errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Find Method Error

Find method errors.

### Common Causes
Wrong parameters; no results; wrong order

### How to Fix
```vba
Dim rng As Range
Set rng = ws.UsedRange.Find(What:=searchVal, LookIn:=xlValues)
If Not rng Is Nothing Then
    Debug.Print rng.Address
End If
```

### Examples
```vba
Dim rng As Range
Set rng = ws.Range("A:A").Find(What:="text", After:=ws.Range("A1"), _
    LookIn:=xlValues, LookAt:=xlWhole)
```
