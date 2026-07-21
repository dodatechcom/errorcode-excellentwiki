---
title: "[Solution] VBA Control Error"
description: "UserForm control errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Control Error

UserForm control errors.

### Common Causes
Control not found; wrong type; missing event

### How to Fix
```vba
' Check control type
Debug.Print TypeName(TextBox1)
```

### Examples
```vba
Private Sub UserForm_QueryClose(Cancel As Integer, CloseMode As Integer)
    If CloseMode = vbFormControlMenu Then
        Cancel = True
        MsgBox "Use the Close button"
    End If
End Sub
```
