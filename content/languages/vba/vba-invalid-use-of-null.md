---
title: "[Solution] VBA Invalid Use of Null Error Fix"
description: "Fix VBA 'Invalid use of Null' errors (error 94). Learn why Null causes runtime errors and how to check for Null before using values."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The VBA Invalid Use of Null error (error 94) occurs when a Null value is used in a context that does not allow it. Null represents the absence of a valid data value and is distinct from Empty, zero-length string, or Nothing. Most VBA functions and operators cannot handle Null and will raise this error.

## Why It Happens

- Reading a cell that contains Null (common with database fields)
- Using Null in string concatenation without handling it first
- Passing Null to functions that expect non-Null values
- Comparing Null with `=`, which returns Null instead of True or False
- Using Null in arithmetic operations
- Accessing recordset fields that contain Null values
- Using `IsEmpty()` on Null values (should use `IsNull()`)

## How to Fix It

### Use IsNull to check before operations

```vba
' WRONG: Concatenating Null
Sub BuildName()
    Dim firstName As Variant
    firstName = Range("A1").Value  ' may be Null
    Dim fullName As String
    fullName = "Mr. " & firstName  ' Invalid use of Null
End Sub

' CORRECT: Check for Null first
Sub BuildName()
    Dim firstName As Variant
    firstName = Range("A1").Value
    
    If IsNull(firstName) Then
        firstName = ""
    End If
    Dim fullName As String
    fullName = "Mr. " & firstName
End Sub
```

### Use Nz function for Null-safe conversions

```vba
' WRONG: Null in arithmetic
Sub Calculate()
    Dim val As Variant
    val = Range("B1").Value  ' may be Null
    Dim total As Double
    total = val * 1.1  ' Invalid use of Null
End Sub

' CORRECT: Use Nz to convert Null to a default
Sub Calculate()
    Dim val As Variant
    val = Range("B1").Value
    Dim total As Double
    total = Nz(val, 0) * 1.1  ' treats Null as 0
End Sub
```

### Handle Null in recordset operations

```vba
' WRONG: Accessing Null recordset field
Sub ReadRecord()
    Dim rs As Object
    Set rs = CreateObject("ADODB.Recordset")
    ' ... open recordset ...
    Dim name As String
    name = rs.Fields("name").Value  ' may be Null
End Sub

' CORRECT: Check each field for Null
Sub ReadRecord()
    Dim rs As Object
    Set rs = CreateObject("ADODB.Recordset")
    ' ... open recordset ...
    Dim name As String
    If Not IsNull(rs.Fields("name").Value) Then
        name = rs.Fields("name").Value
    Else
        name = "Unknown"
    End If
End Sub
```

### Use proper Null comparison

```vba
' WRONG: Null comparison returns Null, not True/False
Sub CheckNull()
    Dim val As Variant
    val = Range("A1").Value
    
    If val = Null Then  ' always False, even if val is Null
        MsgBox "Null"
    End If
End Sub

' CORRECT: Use IsNull function
Sub CheckNull()
    Dim val As Variant
    val = Range("A1").Value
    
    If IsNull(val) Then
        MsgBox "Null"
    End If
End Sub
```

### Filter Null values from arrays

```vba
' WRONG: Null in array operations
Sub ProcessArray()
    Dim arr As Variant
    arr = Range("A1:A100").Value
    Dim i As Long
    For i = 1 To UBound(arr, 1)
        arr(i, 1) = arr(i, 1) + 1  ' Null causes error
    Next i
End Sub

' CORRECT: Skip Null entries
Sub ProcessArray()
    Dim arr As Variant
    arr = Range("A1:A100").Value
    Dim i As Long
    For i = 1 To UBound(arr, 1)
        If Not IsNull(arr(i, 1)) Then
            arr(i, 1) = arr(i, 1) + 1
        End If
    Next i
    Range("A1:A100").Value = arr
End Sub
```

## Common Mistakes

- Confusing Null with Empty (Empty = uninitialized Variant, Null = explicitly invalid)
- Using `val = Null` instead of `IsNull(val)` for comparison
- Not checking for Null when reading from databases or pivot tables
- Forgetting that `IsNull()` only works with Variant types
- Using `Len(Null)` which returns 0 instead of raising an error

## Related Pages

- [VBA Type Mismatch](vba-type-mismatch-v3) - type error
- [VBA Application-Defined Error](vba-application-defined-error) - application error
- [VBA ADO Connection Error](vba-adodb-connection-error) - database error
- [VBA Recordset Error](vba-recordset-error) - recordset failure
