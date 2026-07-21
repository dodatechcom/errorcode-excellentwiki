---
title: "[Solution] VBA Late Binding Error"
description: "Late binding errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Late Binding Error

Late binding errors.

### Common Causes
Wrong ProgID; type not accessible

### How to Fix
```vba
Dim dict As Object
Set dict = CreateObject("Scripting.Dictionary")
dict.CompareMode = 1
```

### Examples
```vba
Dim app As Object
Set app = CreateObject("Excel.Application")
' Use app.Sheets instead of Worksheets
```
