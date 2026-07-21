---
title: "[Solution] VBA Project Not Found Error"
description: "Referenced project or library not available."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Project Not Found Error

Referenced project or library not available.

### Common Causes
Missing reference; broken reference

### How to Fix
```vba
' Tools > References > Check needed libraries
```

### Examples
```vba
' Late binding avoids reference issues
Dim fso As Object
Set fso = CreateObject("Scripting.FileSystemObject")
```
