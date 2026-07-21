---
title: "[Solution] VBA Range Object Error"
description: "Range object reference errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Range Object Error

Range object reference errors.

### Common Causes
Wrong range address; using Cells wrong

### How to Fix
```vba
ws.Range("A1:D10").Value = "test"
ws.Cells(1, 1).Value = 100
```

### Examples
```vba
Dim rng As Range
Set rng = ws.Range("A1:A" & lastRow)
rng.Copy Destination:=ws2.Range("A1")
```
