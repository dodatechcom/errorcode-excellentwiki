---
title: "[Solution] VBA User-Defined Type Not Defined Error Fix"
description: "Fix VBA 'User-defined type not defined' compile errors (error 13). Learn why type declarations fail and how to resolve UDT issues."
languages: ["vba"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

## What This Error Means

The VBA User-Defined Type Not Defined error (error 13, when used as a compile error) occurs when you reference a type name in a `Dim` or `As` clause that the compiler does not recognize. This includes custom Type definitions, class modules, and references to external object libraries that are not properly registered.

## Why It Happens

- Using a custom `Type` definition before it is declared in the module
- Missing a reference to an external library that provides the type
- A referenced library was removed or unregistered from the system
- Typo in the type name
- The type is defined in a different module and is not accessible
- Using an object library type without adding the reference
- The project uses a 64-bit library on 32-bit Office or vice versa

## How to Fix It

### Define Type before use or place in a standard module

```vba
' WRONG: Type used before declaration
Sub Process()
    Dim pt As Point  ' compile error: Point not defined
    pt.X = 10
End Sub

Type Point
    X As Long
    Y As Long
End Type

' CORRECT: Place Type definition before use
Type Point
    X As Long
    Y As Long
End Type

Sub Process()
    Dim pt As Point
    pt.X = 10
    pt.Y = 20
End Sub
```

### Add missing library references

```vba
' WRONG: ADODB type not recognized
Sub Query()
    Dim rs As ADODB.Recordset  ' compile error without reference
End Sub

' CORRECT: Add reference or use late binding
' Option 1: Add reference via Tools > References > Microsoft ADO x.x
' Option 2: Use late binding
Sub Query()
    Dim rs As Object
    Set rs = CreateObject("ADODB.Recordset")
End Sub
```

### Use late binding to avoid reference issues

```vba
' WRONG: Early binding requires reference
Sub CreateWordDoc()
    Dim app As Word.Application  ' requires Word reference
    Set app = New Word.Application
End Sub

' CORRECT: Late binding works without reference
Sub CreateWordDoc()
    Dim app As Object
    Set app = CreateObject("Word.Application")
    app.Visible = True
End Sub
```

### Fix typos in type names

```vba
' WRONG: Typo in type name
Sub Test()
    Dim ws As Workseheet  ' typo: should be Worksheet
End Sub

' CORRECT: Use correct type name
Sub Test()
    Dim ws As Worksheet
    Set ws = ActiveSheet
End Sub
```

### Use class modules correctly

```vba
' WRONG: Class module name not recognized
Sub Test()
    Dim p As Person  ' compile error if Person class not in project
End Sub

' CORRECT: Ensure the class module exists in the project
' Create a class module named "Person" in the VBA project
' Then use:
Sub Test()
    Dim p As Person
    Set p = New Person
End Sub
```

## Common Mistakes

- Not realizing that custom Types must be in a standard module, not a class module
- Forgetting to re-add references after copying code to a new project
- Using `Integer` type when the library expects `Long` on 64-bit systems
- Not understanding that `Variant` avoids type errors but loses compile-time checking
- Assuming that a type from an add-in is automatically available without a reference

## Related Pages

- [VBA Compile Error](vba-compile-error) - general compile issues
- [VBA Invalid Procedure Declaration](vba-invalid-procedure-declaration) - declaration error
- [VBA Name Conflicts](vba-name-conflicts) - naming conflict
- [VBA Type Mismatch](vba-type-mismatch-v3) - runtime type error
