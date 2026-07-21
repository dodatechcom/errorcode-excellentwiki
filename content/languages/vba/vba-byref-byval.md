---
title: "[Solution] VBA ByRef/ByVal Error"
description: "Wrong parameter passing mode."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA ByRef/ByVal Error

Wrong parameter passing mode.

### Common Causes
ByRef modifies original; ByVal copies

### How to Fix
```vba
Sub Increment(ByRef x As Long)
    x = x + 1
End Sub
```

### Examples
```vba
Sub SetValue(ByVal x As Long, ByRef y As Long)
    x = 100  ' doesn't change original
    y = 100  ' changes original
End Sub
```
