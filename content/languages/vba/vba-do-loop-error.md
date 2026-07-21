---
title: "[Solution] VBA Do...Loop Error"
description: "Do...Loop errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Do...Loop Error

Do...Loop errors.

### Common Causes
Infinite loop; missing Loop; wrong condition

### How to Fix
```vba
Do While Cells(i, 1).Value <> ""
    i = i + 1
Loop
```

### Examples
```vba
Do
    i = i + 1
Loop Until Cells(i, 1).Value = ""
```
