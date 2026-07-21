---
title: "VBA Worksheet Activate Error Fix"
description: "Fix VBA Worksheet.Activate errors when activating sheets across workbooks or hidden sheets."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Worksheet Activate Error Fix

Worksheet.Activate can fail when the sheet belongs to a different workbook, is very hidden (xlSheetVeryHidden), or when called from an event handler that prevents sheet switching.

## Common Causes

- Sheet belongs to a workbook other than the active one
- Sheet is hidden with xlSheetVeryHidden property
- Activate called from Workbook_SheetActivate event causing recursion
- Sheet is protected in a way that prevents activation
- Application state prevents switching (e.g., modal dialog)

## How to Fix

```vba
' Wrong -- activating sheet in wrong workbook
Workbooks("Other.xlsx").Sheets(1).Activate  ' may fail

' Correct -- activate workbook first, then sheet
Workbooks("Other.xlsx").Activate
Workbooks("Other.xlsx").Sheets(1).Activate
```

```vba
' Wrong -- activating very hidden sheet
Dim ws As Worksheet
Set ws = ThisWorkbook.Sheets("Hidden")
ws.Activate  ' Error: sheet is very hidden

' Correct -- change visibility first
ws.Visible = xlSheetVisible
ws.Activate
```

## Examples

```vba
Sub Example1_SafeActivate()
    On Error Resume Next
    ThisWorkbook.Sheets("Data").Activate
    If ActiveSheet.Name <> "Data" Then
        MsgBox "Sheet 'Data' not found"
    End If
    On Error GoTo 0
End Sub

Sub Example2_CycleThroughSheets()
    Dim ws As Worksheet
    For Each ws In ThisWorkbook.Worksheets
        ws.Activate
        Debug.Print "Now viewing: " & ws.Name
    Next ws
End Sub

Sub Example3_ActivateByIndex()
    If ThisWorkbook.Sheets.Count >= 3 Then
        ThisWorkbook.Sheets(3).Activate
    End If
End Sub
```

## Related Errors

- [Sheet not found error](vba-name-error) -- sheet name issues
- [Activate error](vba-activate-error) -- activation failures
