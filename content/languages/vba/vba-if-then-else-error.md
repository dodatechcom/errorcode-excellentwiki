---
title: "[Solution] VBA If...Then...Else Error"
description: "If...Then syntax errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA If...Then...Else Error

If...Then syntax errors.

### Common Causes
Missing Then; wrong End If; nested issues

### How to Fix
```vba
If x > 0 Then
    result = x
Else
    result = 0
End If
```

### Examples
```vba
If x > 10 Then
    Debug.Print "Large"
ElseIf x > 5 Then
    Debug.Print "Medium"
Else
    Debug.Print "Small"
End If
```
