---
title: "[Solution] VBA Cells Error"
description: "Cells property errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Cells Error

Cells property errors.

### Common Causes
Wrong row/column; exceeding limits

### How to Fix
```vba
ws.Cells(1, 1).Value = "A1"
ws.Cells(2, 1).Value = "A2"
```

### Examples
```vba
Dim lastRow As Long
lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
ws.Cells(lastRow + 1, 1).Value = "new"
```
