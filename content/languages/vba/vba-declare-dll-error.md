---
title: "[Solution] VBA Declare DLL Error"
description: "Declare statement for API calls errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Declare DLL Error

Declare statement for API calls errors.

### Common Causes
Wrong syntax; 32/64 bit issues; wrong lib

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
Private Declare PtrSafe Function Sleep Lib "kernel32" (ByVal ms As LongPtr) As Long
```
