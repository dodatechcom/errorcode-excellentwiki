---
title: "[Solution] VBA Object Required Error"
description: "Fix VBA Object Required error (Error 424) when code references an object without using the Set keyword or the object is Nothing."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["object-required", "error-424", "set-keyword", "nothing", "vba"]
weight: 5
---

## What This Error Means

Object Required (Error 424) occurs when VBA expects an object reference but receives a value instead. This happens when `Set` is omitted for object assignment or when a method is called on a `Nothing` object.

## Common Causes

- Missing `Set` keyword for object assignment
- Object variable set to Nothing
- Misspelled object name
- Object was destroyed or closed
- Using default property instead of object

## How to Fix

```vba
' WRONG: Missing Set keyword
Dim ws As Worksheet
ws = Worksheets("Sheet1")   ' Object Required

' CORRECT: Use Set for object assignment
Dim ws As Worksheet
Set ws = Worksheets("Sheet1")
```

```vba
' WRONG: Object is Nothing
Dim rng As Range
Set rng = Nothing
rng.Value = 1   ' Object Required

' CORRECT: Check for Nothing
If Not rng Is Nothing Then
    rng.Value = 1
End If
```

## Examples

```vba
Sub Example()
    Dim wb As Workbook
    wb = Workbooks(1)      ' Missing Set
    wb.Activate
End Sub
```

## Related Errors

- [Object Variable Not Set](vba-object-variable-not-set) - Nothing reference
- [Runtime Error](vba-runtime-error) - general execution errors
