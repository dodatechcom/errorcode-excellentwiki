---
title: "[Solution] VBA Library Not Registered"
description: "ActiveX component not registered on system."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Library Not Registered

ActiveX component not registered on system.

### Common Causes
DLL missing; wrong version; 32/64 bit mismatch

### How to Fix
```vba
' Use late binding instead
Dim app As Object
Set app = CreateObject("Excel.Application")
```

### Examples
```vba
' Check references
Dim ref As Reference
For Each ref In ThisProject.VBProject.References
    Debug.Print ref.Description
Next
```
