---
title: "[Solution] VBA With Block Not Set"
description: "With statement referencing Nothing."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA With Block Not Set

With statement referencing Nothing.

### Common Causes
Missing Set; object not initialized

### How to Fix
```vba
With ws.Range("A1")
    .Value = "Hello"
    .Font.Bold = True
End With
```

### Examples
```vba
Set ws = ThisWorkbook.ActiveSheet
With ws
    .Range("A1").Value = "Test"
End With
```
