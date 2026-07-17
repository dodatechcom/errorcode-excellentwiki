---
title: "[Solution] VBA Runtime Error 424 Object Required Fix"
description: "Fix VBA 'Run-time error 424: Object required' when a variable or expression is expected to be an object but is not."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# VBA Runtime Error 424: Object Required Fix

This error occurs when VBA encounters a variable or expression where an object is expected, but the value is `Nothing` or a simple data type. The full message is: `Run-time error '424': Object required`.

## Description

In VBA, object variables must be set with the `Set` keyword. If you omit `Set`, or if an object variable is `Nothing` when you try to access its properties or methods, VBA raises error 424. This error also occurs when trying to use a non-object variable (such as a `String` or `Long`) as an object.

## Common Causes

- **Missing `Set` keyword** — `Dim ws As Worksheet: ws = Worksheets("Sheet1")` instead of `Set ws =`.
- **Object variable is `Nothing`** — attempting to access a property on an unset object reference.
- **Using a value type as an object** — trying to call a method on a `String` or numeric variable.
- **Incorrect early binding declaration** — declaring an object with the wrong class name.

## How to Fix

### Fix 1: Always use Set for object assignment

```vba
' Wrong — missing Set keyword
Dim ws As Worksheet
ws = Worksheets("Sheet1")

' Correct — use Set
Dim ws As Worksheet
Set ws = Worksheets("Sheet1")
```

### Fix 2: Check for Nothing before accessing properties

```vba
' Wrong — object might be Nothing
Dim wb As Workbook
Set wb = Workbooks("Missing.xlsx")
Debug.Print wb.Name  ' Error 424 if wb is Nothing

' Correct — check first
Set wb = Workbooks("Missing.xlsx")
If Not wb Is Nothing Then
    Debug.Print wb.Name
End If
```

### Fix 3: Ensure functions return objects properly

```vba
' Wrong — function doesn't return the object correctly
Function GetSheet(name As String) As Worksheet
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = Worksheets(name)
    On Error GoTo 0
    ' No assignment to the function name
End Function

' Correct — assign the object to the function
Function GetSheet(name As String) As Worksheet
    On Error Resume Next
    Set GetSheet = Worksheets(name)
    On Error GoTo 0
End Function
```

### Fix 4: Use CreateObject for late binding

```vba
' Wrong — object not created
Dim app As Object
app.Application.Visible = True  ' app is Nothing

' Correct — create the object first
Dim app As Object
Set app = CreateObject("Excel.Application")
app.Visible = True
```

## Examples

```vba
Sub Example()
    ' Error 424: Missing Set
    Dim rng As Range
    rng = Range("A1")  ' Runtime error 424: Object required
    
    ' Error 424: Accessing property on Nothing
    Dim ws As Worksheet
    Debug.Print ws.Name  ' Runtime error 424: Object required
End Sub
```

## Related Errors

- [Type Mismatch]({{< relref "/languages/vba/type-mismatch13" >}}) — assigning an incompatible value to a variable.
- [Runtime Error 1004]({{< relref "/languages/vba/runtime-error1004" >}}) — application-defined error when working with objects.
