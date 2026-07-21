---
title: "[Solution] VBA WithEvents Error"
description: "WithEvents declaration errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA WithEvents Error

WithEvents declaration errors.

### Common Causes
Wrong syntax; limited to class modules

### How to Fix
```vba
' In class module
Private WithEvents ws As Worksheet
```

### Examples
```vba
Private WithEvents app As Application
Private Sub app_WorkbookOpen(ByVal wb As Workbook)
    Debug.Print wb.Name
End Sub
```
