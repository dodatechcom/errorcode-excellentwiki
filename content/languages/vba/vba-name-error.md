---
title: "[Solution] VBA Name Error"
description: "Named range errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Name Error

Named range errors.

### Common Causes
Name not found; duplicate name; scope issues

### How to Fix
```vba
ThisWorkbook.Names.Add Name:="MyRange", RefersTo:=Range("A1:A10")
```

### Examples
```vba
Dim nm As Name
Set nm = ThisWorkbook.Names("MyRange")
Debug.Print nm.RefersTo
```
