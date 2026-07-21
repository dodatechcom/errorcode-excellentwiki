---
title: "[Solution] VBA Worksheet Function Error"
description: "WorksheetFunction method errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Worksheet Function Error

WorksheetFunction method errors.

### Common Causes
Wrong function; not available in VBA

### How to Fix
```vba
' Use Application.WorksheetFunction
result = Application.WorksheetFunction.VLookup(val, rng, 2, False)
```

### Examples
```vba
On Error Resume Next
result = Application.WorksheetFunction.Match(val, rng, 0)
If Err.Number <> 0 Then
    Debug.Print "Not found"
End If
```
