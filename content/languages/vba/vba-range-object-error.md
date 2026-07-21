---
title: "VBA Range Object Error Fix"
description: "Fix VBA Range errors when referencing cells with invalid address syntax or non-existent ranges."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Range Object Error Fix

Range errors occur when the address string passed to Range() or Cells() is invalid, the range references a non-existent sheet, or the address syntax uses incorrect notation.

## Common Causes

- Invalid cell address syntax like "A:1" instead of "A1"
- Range on a sheet that does not exist
- Using Range on a non-worksheet object like a chart
- Circular references created by Range writes
- Cells() arguments out of valid row/column bounds

## How to Fix

```vba
' Wrong -- invalid address syntax
Dim rng As Range
Set rng = Range("A1:C")  ' Invalid address

' Correct -- complete address
Set rng = Range("A1:C10")
```

```vba
' Wrong -- referencing non-existent sheet
Set rng = Sheets("MissingSheet").Range("A1")

' Correct -- verify sheet exists
On Error Resume Next
Set ws = Sheets("MissingSheet")
On Error GoTo 0
If Not ws Is Nothing Then
    Set rng = ws.Range("A1")
End If
```

## Examples

```vba
Sub Example1_BasicRange()
    Range("A1").Value = "Hello"
    Range("B1:D1").Value = "World"
    Range("A1:B3").Interior.Color = vbYellow
End Sub

Sub Example2_Cells()
    Dim i As Long, j As Long
    For i = 1 To 10
        For j = 1 To 5
            Cells(i, j).Value = i * j
        Next j
    Next i
End Sub

Sub Example3_UsedRange()
    Dim lastRow As Long
    lastRow = ActiveSheet.Cells(Rows.Count, 1).End(xlUp).Row
    Dim rng As Range
    Set rng = Range(Cells(1, 1), Cells(lastRow, 5))
    Debug.Print "Data range: " & rng.Address
End Sub
```

## Related Errors

- [Cells error](vba-cells-error) -- cell reference issues
- [Range error](vba-range-error) -- range manipulation problems
