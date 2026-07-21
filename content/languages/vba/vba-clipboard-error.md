---
title: "[Solution] VBA Clipboard Error"
description: "Clipboard operations errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Clipboard Error

Clipboard operations errors.

### Common Causes
Data formats; not text; clearing issues

### How to Fix
```vba
MSForms.DataObject.SetText "Hello"
MSForms.DataObject.PutInClipboard
```

### Examples
```vba
Dim clipBoard As MSForms.DataObject
Set clipBoard = New MSForms.DataObject
clipBoard.GetText
```
