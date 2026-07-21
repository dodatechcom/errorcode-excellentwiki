---
title: "[Solution] VBA For Each Error"
description: "For Each loop errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA For Each Error

For Each loop errors.

### Common Causes
Collection not iterable; nothing to iterate

### How to Fix
```vba
Dim ws As Worksheet
For Each ws In ThisWorkbook.Worksheets
    Debug.Print ws.Name
Next ws
```

### Examples
```vba
Dim cell As Range
For Each cell In ws.Range("A1:A10")
    If cell.Value > 0 Then cell.Interior.Color = vbGreen
Next cell
```
