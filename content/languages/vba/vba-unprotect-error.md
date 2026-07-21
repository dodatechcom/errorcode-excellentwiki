---
title: "[Solution] VBA Unprotect Error"
description: "Sheet/Workbook unprotect errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Unprotect Error

Sheet/Workbook unprotect errors.

### Common Causes
Wrong password; not protected; already unprotected

### How to Fix
```vba
ws.Unprotect Password:="mypassword"
```

### Examples
```vba
On Error Resume Next
ws.Unprotect "password"
If Err.Number <> 0 Then
    Debug.Print "Sheet not protected or wrong password"
End If
```
