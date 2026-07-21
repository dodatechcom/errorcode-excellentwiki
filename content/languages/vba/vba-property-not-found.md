---
title: "[Solution] VBA Property Not Found Error"
description: "Object does not have the specified property."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Property Not Found Error

Object does not have the specified property.

### Common Causes
Wrong property name; typo

### How to Fix
```vba
' Check object properties
Dim prop As Variant
For Each prop In rng.Properties
    Debug.Print prop.Name
Next
```

### Examples
```vba
Debug.Print ws.Name
Debug.Print ws.Range("A1").Value
```
