---
title: "[Solution] VBA RaiseEvent Error"
description: "RaiseEvent errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA RaiseEvent Error

RaiseEvent errors.

### Common Causes
No handler connected; wrong arguments

### How to Fix
```vba
' In class module
Public Event DataLoaded(count As Long)
Public Sub LoadData()
    RaiseEvent DataLoaded(100)
End Sub
```

### Examples
```vba
' In form module
Private WithEvents loader As DataLoader
Private Sub loader_DataLoaded(count As Long)
    MsgBox count & " records loaded"
End Sub
```
