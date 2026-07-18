---
title: "[Solution] VBA Type Mismatch Error in Function Fix"
description: "Fix VBA Type mismatch errors (error 13). Learn why VBA raises type mismatch and how to validate variable types before operations."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The VBA Type Mismatch error (error 13) occurs when a variable or expression has a data type that is not compatible with the operation being performed. This includes assigning a string to a numeric variable, calling a function with the wrong argument types, or using `Variant` variables with incompatible values.

## Why It Happens

- Assigning a non-numeric value to a Long, Integer, or Double variable
- Passing a Range object where a string or numeric value is expected
- Comparing values of incompatible types
- Using `CInt`, `CLng`, or `CDbl` on non-numeric strings
- Calling a function with a Range object instead of its `.Value`
- Mixing `Variant` and strongly typed variables without conversion
- Using `Like` operator on non-string values

## How to Fix It

### Convert types explicitly before assignment

```vba
' WRONG: String assigned to Long
Sub WrongExample()
    Dim total As Long
    total = "123abc"  ' Type mismatch
End Sub

' CORRECT: Validate and convert
Sub CorrectExample()
    Dim total As Long
    Dim inputVal As String
    inputVal = "123abc"
    
    If IsNumeric(inputVal) Then
        total = CLng(inputVal)
    Else
        MsgBox "Invalid number: " & inputVal
    End If
End Sub
```

### Pass cell values correctly to functions

```vba
' WRONG: Passing Range object to numeric parameter
Sub CalculateTotal()
    Dim result As Double
    result = SumValues(Range("A1:A10"))  ' Type mismatch
End Sub

' CORRECT: Pass the value property
Sub CalculateTotal()
    Dim result As Double
    result = SumValues(Range("A1:A10").Value)
End Sub

Function SumValues(arr As Variant) As Double
    Dim i As Long
    For i = LBound(arr, 1) To UBound(arr, 1)
        If IsNumeric(arr(i, 1)) Then
            SumValues = SumValues + arr(i, 1)
        End If
    Next i
End Function
```

### Use Variant for flexible type handling

```vba
' WRONG: Strong typing where flexibility is needed
Sub ProcessInput()
    Dim val As Long
    val = Application.InputBox("Enter a number:", Type:=1)  ' may get error
End Sub

' CORRECT: Use Variant and validate
Sub ProcessInput()
    Dim val As Variant
    val = Application.InputBox("Enter a number:", Type:=1)
    
    If val = False Then Exit Sub  ' user cancelled
    
    If IsNumeric(val) Then
        Dim numVal As Long
        numVal = CLng(val)
        MsgBox "You entered: " & numVal
    Else
        MsgBox "Please enter a valid number"
    End If
End Sub
```

### Validate Array dimensions before access

```vba
' WRONG: Accessing wrong array dimension
Sub ReadArray()
    Dim arr As Variant
    arr = Range("A1:C3").Value
    Dim val As String
    val = arr(1, 1, 1)  ' Type mismatch - wrong dimensions
End Sub

' CORRECT: Match dimension count
Sub ReadArray()
    Dim arr As Variant
    arr = Range("A1:C3").Value
    
    If IsArray(arr) Then
        Dim val As Variant
        val = arr(1, 1)  ' 2D array from Range
        If Not IsEmpty(val) Then
            Debug.Print val
        End If
    End If
End Sub
```

### Handle empty cells gracefully

```vba
' WRONG: Empty cell causes type mismatch
Sub ReadCell()
    Dim ws As Worksheet
    Set ws = ActiveSheet
    Dim val As Long
    val = ws.Range("A1").Value  ' empty cell = ""
End Sub

' CORRECT: Check for empty cells
Sub ReadCell()
    Dim ws As Worksheet
    Set ws = ActiveSheet
    Dim val As Variant
    val = ws.Range("A1").Value
    
    If IsEmpty(val) Or val = "" Then
        val = 0  ' default
    ElseIf IsNumeric(val) Then
        val = CLng(val)
    Else
        MsgBox "Cell A1 is not numeric"
        Exit Sub
    End If
End Sub
```

## Common Mistakes

- Not using `.Value` when passing a Range to a function expecting a scalar
- Forgetting that empty cells are treated as empty strings, not zero
- Using `CInt` on values outside the Integer range (-32,768 to 32,767)
- Assuming `Variant` will automatically convert between incompatible types
- Comparing a `Nothing` object with `=` instead of `Is Nothing`

## Related Pages

- [VBA Application-Defined Error](vba-application-defined-error) - application-defined error
- [VBA Subscript Out of Range](vba-subscript-out-of-range) - array index error
- [VBA Invalid Use of Null](vba-invalid-use-of-null) - Null value error
- [VBA Compile Error](vba-compile-error) - compilation issue
