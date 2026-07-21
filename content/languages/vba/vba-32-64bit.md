---
title: "[Solution] VBA 32/64-bit Compatibility"
description: "32-bit vs 64-bit VBA compatibility issues."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA 32/64-bit Compatibility

32-bit vs 64-bit VBA compatibility issues.

### Common Causes
PtrSafe needed; Declare wrong type

### How to Fix
```vba
#If VBA7 Then
    Declare PtrSafe Function GetTickCount Lib "kernel32" () As Long
#Else
    Declare Function GetTickCount Lib "kernel32" () As Long
#End If
```

### Examples
```vba
#If Win64 Then
    Declare PtrSafe Function FindWindow Lib "user32" Alias "FindWindowA" _
        (ByVal a As String, ByVal b As String) As LongPtr
#End If
```
