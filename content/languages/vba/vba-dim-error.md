---
title: "VBA Dim Statement Without Matching End Sub Fix"
description: "Fix VBA Dim statement errors when variable declarations conflict with existing names or are placed incorrectly."
languages: ["vba"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# VBA Dim Statement Fix

VBA Dim errors occur when variable declarations conflict with reserved words, duplicate existing names in scope, or are placed in positions that violate VBA's declaration rules.

## Common Causes

- Declaring a variable with the same name as a Sub, Function, or property
- Using reserved words like `Date`, `Name`, `Value` as variable names
- Placing Dim statements after executable code in strict mode
- Redeclaring a variable with a different type in the same scope
- Using special characters in variable names

## How to Fix

```vba
' Wrong -- variable name conflicts with property
Sub Example()
    Dim Name As String  ' conflicts with workbook Name property
    Name = "test"
End Sub

' Correct -- use a unique name
Sub Example()
    Dim userName As String
    userName = "test"
End Sub
```

```vba
' Wrong -- Dim after executable code (Module level is fine)
Sub Example()
    x = 10       ' executable code
    Dim y As Integer  ' warning: variable after code
    y = 20
End Sub

' Correct -- declare all variables at the top
Sub Example()
    Dim x As Integer
    Dim y As Integer
    x = 10
    y = 20
End Sub
```

## Examples

```vba
Sub Example1_Types()
    Dim count As Long
    Dim total As Currency
    Dim isActive As Boolean
    Dim data() As Variant
End Sub

Sub Example2_Conflict()
    Dim Print As String  ' Error: Print is a keyword
    Dim Open As Integer  ' Error: Open is a keyword
    ' Use prefixed names instead
    Dim strPrint As String
    Dim intOpen As Integer
End Sub

Sub Example3_Array()
    Dim arr() As Variant
    ReDim arr(1 To 10)
    Dim matrix(1 To 3, 1 To 3) As Double
End Sub
```

## Related Errors

- [Compile error syntax](vba-compile-error-syntax) -- general syntax problems
- [Variable name error](vba-compile-error-variable) -- naming convention issues
