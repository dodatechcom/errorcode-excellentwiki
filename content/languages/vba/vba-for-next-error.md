---
title: "[Solution] VBA For...Next Error"
description: "For...Next loop errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA For...Next Error

For...Next loop errors.

### Common Causes
Missing Next; wrong step; index not incremented

### How to Fix
```vba
Dim i As Long
For i = 1 To 10
    Debug.Print i
Next i
```

### Examples
```vba
Dim i As Long
For i = 1 To 100 Step 2
    Cells(i, 1).Value = i
Next i
```
