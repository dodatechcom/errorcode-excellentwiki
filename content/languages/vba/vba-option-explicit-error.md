---
title: "VBA Option Explicit Missing Fix"
description: "Fix VBA errors caused by missing Option Explicit allowing typos to create silent new variables instead of raising errors."
languages: ["vba"]
error-types: ["logic-error"]
severities: ["warning"]
weight: 5
---

# VBA Option Explicit Missing Fix

Without `Option Explicit` at the top of a module, VBA silently creates new variables for any misspelled names, causing logical errors that are extremely difficult to debug.

## Common Causes

- Module does not have `Option Explicit` as the first line
- Variable name typo creates a new variable instead of erroring
- Copy-pasted code with renamed variables but typos remain
- Different casing of same variable treated as new variable (default)
- Accidentally referencing a different module's public variable

## How to Fix

```vba
' Wrong -- no Option Explicit
Sub Example()
    userName = "Alice"  ' creates implicit variable
    Debug.Print userNmae  ' typo creates another variable, prints empty
End Sub

' Correct -- add Option Explicit
Option Explicit
Sub Example()
    Dim userName As String
    userName = "Alice"
    Debug.Print userNmae  ' Compile error: variable not defined
End Sub
```

```vba
' Wrong -- implicit variant creation
Sub Process(val)
    result = val * 2  ' result is implicit variant
    Debug.Print resutl  ' typo, silent failure
End Sub

' Correct -- explicit declarations
Option Explicit
Sub Process(val As Double)
    Dim result As Double
    result = val * 2
    Debug.Print result
End Sub
```

## Examples

```vba
' Good module header
Option Explicit
Option Compare Text
Option Base 1

Sub Example1()
    Dim count As Long
    Dim total As Double
    Dim isActive As Boolean
    
    count = 10
    total = 100.5
    isActive = True
    
    Debug.Print "Count: " & count
    Debug.Print "Total: " & total
    Debug.Print "Active: " & isActive
End Sub

Sub Example2_Parameters()
    Dim items() As String
    Dim i As Long
    
    items = Split("a,b,c", ",")
    For i = LBound(items) To UBound(items)
        Debug.Print items(i)
    Next i
End Sub
```

## Related Errors

- [Compile error variable](vba-compile-error-variable) -- variable naming issues
- [Compile error syntax](vba-compile-error-syntax) -- syntax problems
