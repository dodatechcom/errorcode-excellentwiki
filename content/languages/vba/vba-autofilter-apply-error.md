---
title: "VBA AutoFilter Apply Error Fix"
description: "Fix VBA AutoFilter errors when applying or clearing filters with invalid criteria or range references."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA AutoFilter Apply Error Fix

AutoFilter errors occur when applying filters to ranges that have incompatible data, using invalid filter criteria, or trying to filter a range that is already filtered in a conflicting way.

## Common Causes

- Applying filter to a range that is already filtered
- Filter field number exceeds the number of columns in the range
- Using invalid criteria syntax for the filter type
- Range contains merged cells which prevent filtering
- Trying to filter a protected worksheet

## How to Fix

```vba
' Wrong -- filtering already filtered range with new criteria
ActiveSheet.Range("A1:D100").AutoFilter Field:=2, Criteria1:=">100"
ActiveSheet.Range("A1:D100").AutoFilter Field:=3, Criteria1:="Yes"
' Second filter replaces the first

' Correct -- clear first or use multiple criteria
With ActiveSheet
    If .AutoFilterMode Then .AutoFilterMode = False
    .Range("A1:D100").AutoFilter Field:=2, Criteria1:=">100"
    .Range("A1:D100").AutoFilter Field:=3, Criteria1:="Yes"
End With
```

```vba
' Wrong -- field number out of range
ActiveSheet.Range("A1:C100").AutoFilter Field:=5, Criteria1:="test"
' Only 3 columns, field 5 does not exist

' Correct -- verify field exists
Dim colCount As Long
colCount = ActiveSheet.Range("A1:C100").Columns.Count
If FieldNum <= colCount Then
    ActiveSheet.Range("A1:C100").AutoFilter Field:=FieldNum, Criteria1:="test"
End If
```

## Examples

```vba
Sub Example1_BasicFilter()
    ActiveSheet.Range("A1:D100").AutoFilter _
        Field:=2, _
        Criteria1:="Sales"
End Sub

Sub Example2_MultipleCriteria()
    ActiveSheet.Range("A1:D100").AutoFilter _
        Field:=3, _
        Criteria1:=">500", _
        Operator:=xlAnd, _
        Criteria2:="<1000"
End Sub

Sub Example3_ClearFilter()
    If ActiveSheet.AutoFilterMode Then
        ActiveSheet.AutoFilterMode = False
    End If
End Sub
```

## Related Errors

- [Autofilter error](vba-autofilter-error) -- filter-related failures
- [Range error](vba-range-error) -- range reference issues
