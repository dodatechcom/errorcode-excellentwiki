---
title: "[Solution] VBA: Run-time error '7': Out of memory"
description: "Fix VBA Run-time error 7 when VBA cannot allocate memory for variables, arrays, or objects."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Run-time error '7' occurs when VBA cannot allocate enough memory for an operation. This happens with excessively large arrays, too many open objects, or memory leaks.

## Common Causes

- Declaring excessively large arrays
- Too many open workbooks or worksheets
- Memory leak from unreleased objects
- Large string concatenation
- Multiple COM objects not properly released

## How to Fix

```vba
' WRONG: Massive array declaration
Sub Example1()
    Dim arr(1 To 10000000) As Double  ' ~80MB
    ' Error 7: Not enough memory
End Sub

' CORRECT: Use dynamic arrays with bounds
Sub Example1()
    Dim arr() As Double
    ReDim arr(1 To 1000000)  ' ~8MB
    ' Process in chunks if needed
End Sub
```

```vba
' WRONG: Not releasing objects
Sub Example2()
    Dim i As Integer
    For i = 1 To 100
        Dim wb As Workbook
        Set wb = Workbooks.Open("C:\temp\file" & i & ".xlsx")
        ' Memory accumulates
    Next i
End Sub

' CORRECT: Release objects properly
Sub Example2()
    Dim i As Integer
    Dim wb As Workbook
    For i = 1 To 100
        Set wb = Workbooks.Open("C:\temp\file" & i & ".xlsx")
        ' Process file
        wb.Close SaveChanges:=False
        Set wb = Nothing
    Next i
End Sub
```

```vba
' CORRECT: Optimize string operations
Sub Example3()
    Dim result As String
    Dim i As Integer
    
    ' WRONG: String concatenation in loop
    For i = 1 To 10000
        result = result & "Item " & i & vbCrLf
    Next i
    
    ' CORRECT: Use array and Join
    Dim arr() As String
    ReDim arr(1 To 10000)
    For i = 1 To 10000
        arr(i) = "Item " & i
    Next i
    result = Join(arr, vbCrLf)
End Sub
```

## Related Errors

- [Overflow](vba-overflow-v2) - numeric limits
- [Subscript Out of Range](vba-subscript-out-of-range-v2) - array bounds
- [Object Not Set](vba-object-not-set-v2) - memory issues
