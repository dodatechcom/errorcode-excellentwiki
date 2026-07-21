---
title: "VBA ActiveWorkbook Reference Error Fix"
description: "Fix VBA ActiveWorkbook errors when no workbook is open or the reference points to the wrong workbook."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA ActiveWorkbook Reference Fix

ActiveWorkbook returns Nothing when no workbook is open, causing runtime error 91 when you try to access its properties or methods without checking first.

## Common Causes

- No workbook is open when ActiveWorkbook is referenced
- ActiveWorkbook is a different workbook than intended
- Workbook is being closed while code is running
- Using ActiveWorkbook in a timer or event context where no workbook exists
- Forgetting that Add New creates a temporary workbook

## How to Fix

```vba
' Wrong -- no check for Nothing
Dim ws As Worksheet
Set ws = ActiveWorkbook.Sheets(1)  ' Error 91 if no workbook

' Correct -- check first
If Not ActiveWorkbook Is Nothing Then
    Set ws = ActiveWorkbook.Sheets(1)
Else
    MsgBox "No workbook is open"
End If
```

```vba
' Wrong -- ActiveWorkbook may not be the right one
Workbooks("Report.xlsx").Activate
ActiveWorkbook.Sheets(1).Range("A1").Value = "test"  ' could be wrong book

' Correct -- use direct reference
Dim wb As Workbook
Set wb = Workbooks("Report.xlsx")
wb.Sheets(1).Range("A1").Value = "test"
```

## Examples

```vba
Sub Example1_SafeReference()
    Dim wb As Workbook
    Set wb = ActiveWorkbook
    If wb Is Nothing Then Exit Sub
    
    wb.Sheets(1).Activate
    Debug.Print wb.Name
End Sub

Sub Example2_ListOpenWorkbooks()
    Dim wb As Workbook
    For Each wb In Application.Workbooks
        Debug.Print wb.Name & " - " & wb.FullName
    Next wb
End Sub

Sub Example3_CreateIfMissing()
    If Workbooks.Count = 0 Then
        Workbooks.Add
    End If
    ActiveWorkbook.Sheets(1).Range("A1").Value = "Data"
End Sub
```

## Related Errors

- [Object required error](vba-object-required) -- missing object reference
- [Object not set error](vba-object-not-set-v2) -- Nothing reference
