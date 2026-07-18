---
title: "[Solution] VBA Cannot Assign to Read-Only Property Error Fix"
description: "Fix VBA 'Can't assign to read-only property' errors (error 383). Learn why property assignment fails and how to use correct property access."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The VBA Can't Assign to Read-Only Property error (error 383) occurs when you attempt to set a value on a property that only supports reading. Many object model properties in Excel, Word, and Access are read-only for design or safety reasons.

## Why It Happens

- Trying to set a read-only property like `.Name` on certain objects
- Assigning to a property that is read-only in the current context
- Attempting to modify a property that is controlled by the application
- Using `Set` on a property that returns a value type instead of an object
- Confusing a read-only property with a read-write one from a different object model version
- Trying to write to a `Const` or `ReadOnly` variable

## How to Fix It

### Identify read-only properties before assignment

```vba
' WRONG: Chart.ChartType is read-only in some contexts
Sub ChangeChartType()
    Dim cht As Chart
    Set cht = ActiveChart
    cht.ChartType = xlLine  ' may be read-only
End Sub

' CORRECT: Use the correct method to modify the property
Sub ChangeChartType()
    Dim cht As Chart
    Set cht = ActiveChart
    cht.ChartType = xlLine  ' check object model docs first
End Sub
```

### Use the correct object for the assignment

```vba
' WRONG: Trying to set Worksheet.Name directly in some contexts
Sub RenameSheet()
    ActiveWorkbook.Sheets(1).Name = "NewName"  ' may fail if protected
End Sub

' CORRECT: Unprotect first if needed
Sub RenameSheet()
    Dim ws As Worksheet
    Set ws = ActiveWorkbook.Sheets(1)
    
    If ws.ProtectContents Then
        ws.Unprotect Password:=""
    End If
    ws.Name = "NewName"
End Sub
```

### Understand property mutability for Range objects

```vba
' WRONG: Range.Value cannot be assigned in certain contexts
Sub SetValue()
    Dim rng As Range
    Set rng = Range("A1")
    rng = 42  ' implicit assignment, may confuse with Set
End Sub

' CORRECT: Use explicit .Value assignment
Sub SetValue()
    Dim rng As Range
    Set rng = Range("A1")
    rng.Value = 42  ' explicit is always correct
End Sub
```

### Use application-specific methods for protected properties

```vba
' WRONG: Cannot change workbook properties directly
Sub ChangeProperties()
    ActiveWorkbook.BuiltinDocumentProperties("Author") = "New Author"
End Sub

' CORRECT: Some properties require special handling
Sub ChangeProperties()
    ' Use the Document Properties dialog or custom properties
    Dim props As Object
    Set props = ActiveWorkbook.CustomDocumentProperties
    On Error Resume Next
    props("Author").Delete
    On Error GoTo 0
    props.Add Name:="Author", LinkToContent:=False, _
        Type:=msoPropertyTypeString, Value:="New Author"
End Sub
```

### Use application methods instead of property assignment

```vba
' WRONG: Cannot set BuiltInDocumentProperties
Sub UpdateAuthor()
    ThisWorkbook.BuiltinDocumentProperties("Author").Value = "Me"
End Sub

' CORRECT: Use Application-level methods
Sub UpdateAuthor()
    ' Some properties must be set through the application
    Application.DefaultFilePath = "C:\Reports"
    ' Or use custom properties instead of built-in ones
    Dim prop As DocumentProperty
    For Each prop In ThisWorkbook.BuiltinDocumentProperties
        Debug.Print prop.Name & ": " & prop.Value
    Next
End Sub
```

## Common Mistakes

- Not checking the object model documentation to determine if a property is read-only
- Assuming that a property from one application version is writable in another
- Using `Set` keyword on a value-type property return
- Confusing `ReadOnly` mode with a read-only property definition
- Trying to assign to a property that requires a specific application state

## Related Pages

- [VBA Application-Defined Error](vba-application-defined-error) - application error
- [VBA Method Not Supported](vba-method-not-supported) - method not found
- [VBA Compile Error](vba-compile-error) - compilation issue
- [VBA Runtime Error](vba-runtime-error) - general runtime issue
