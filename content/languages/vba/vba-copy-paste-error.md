---
title: "[Solution] VBA Copy/Paste Error"
description: "Copy/Paste operations errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Copy/Paste Error

Copy/Paste operations errors.

### Common Causes
Wrong destination; PasteSpecial needed

### How to Fix
```vba
ws.Range("A1:A10").Copy ws.Range("B1")
```

### Examples
```vba
ws.Range("A1:A10").Copy
ws.Range("B1").PasteSpecial xlPasteValues
Application.CutCopyMode = False
```
