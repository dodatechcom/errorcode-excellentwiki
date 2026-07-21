---
title: "VBA Type Name Function Error Fix"
description: "Fix VBA TypeName errors when using TypeName on uninitialized variants or Nothing references incorrectly."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA TypeName Function Error Fix

TypeName returns "Empty" for uninitialized variants and "Nothing" for object references set to Nothing, which can cause unexpected behavior when type-checking code does not account for these cases.

## Common Causes

- Not handling "Empty" return from TypeName on uninitialized Variant
- Using TypeName result in string comparison without considering casing
- TypeName on a Variant containing an Error returns "Error"
- Confusing TypeName with VarType (different return values)
- Using TypeName on an array does not return element type

## How to Fix

```vba
' Wrong -- not handling Empty
Dim v As Variant
If TypeName(v) = "String" Then  ' False for Empty
    ' code never executes for empty variant
End If

' Correct -- check for Empty first
Dim v As Variant
If IsEmpty(v) Then
    v = "default"
End If
If TypeName(v) = "String" Then
    Debug.Print "It's a string"
End If
```

```vba
' Wrong -- expecting element type from array
Dim arr() As Integer
Debug.Print TypeName(arr)  ' "Integer()" not "Integer"

' Correct -- check element type separately
Debug.Print TypeName(arr)  ' "Integer()"
' Or use VarType for more detail
Debug.Print VarType(arr)   ' 8209 (vbArray + vbInteger)
```

## Examples

```vba
Sub Example1_TypeChecks()
    Dim v As Variant
    v = 42
    Debug.Print TypeName(v)  ' "Long"
    
    v = "hello"
    Debug.Print TypeName(v)  ' "String"
    
    v = Now
    Debug.Print TypeName(v)  ' "Date"
End Sub

Sub Example2_ObjectType()
    Dim ws As Worksheet
    Set ws = ActiveSheet
    Debug.Print TypeName(ws)  ' "Worksheet"
    
    Set ws = Nothing
    Debug.Print TypeName(ws)  ' "Nothing"
End Sub

Sub Example3_EmptyVariant()
    Dim v As Variant
    Debug.Print TypeName(v)  ' "Empty"
    
    If TypeName(v) = "Empty" Then
        v = 0
    End If
    Debug.Print TypeName(v)  ' "Integer"
End Sub
```

## Related Errors

- [Type mismatch error](vba-type-mismatch) -- wrong type assignments
- [Runtime error](vba-runtime-error) -- type-related runtime failures
