---
title: "[Solution] VBA UserForm Error"
description: "UserForm errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA UserForm Error

UserForm errors.

### Common Causes
Missing controls; wrong properties; events

### How to Fix
```vba
Private Sub UserForm_Initialize()
    ComboBox1.AddItem "Option 1"
    ComboBox1.AddItem "Option 2"
End Sub
```

### Examples
```vba
Private Sub btnSubmit_Click()
    If TextBox1.Value = "" Then
        MsgBox "Please enter a value"
        Exit Sub
    End If
    ' process
    Unload Me
End Sub
```
