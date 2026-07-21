---
title: "[Solution] VBA While...Wend Error"
description: "While...Wend outdated syntax."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA While...Wend Error

While...Wend outdated syntax.

### Common Causes
Use Do While instead

### How to Fix
```vba
' Outdated - use Do While
While Not EOF(1)
    Line Input #1, textLine
Wend
```

### Examples
```vba
Do While Not EOF(1)
    Line Input #1, textLine
Loop
```
