---
title: "[Solution] VBA Runtime Error 1004 Fix"
description: "Fix VBA 'Run-time error 1004' when an application-defined or object-defined error occurs in Excel."
languages: ["vba"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtime-error-1004", "application-error", "vba"]
weight: 5
---

# VBA Runtime Error 1004 Fix

This error occurs when VBA encounters an error defined by the host application (Excel, Access, etc.) rather than VBA itself. The full message is: `Run-time error '1004': Application-defined or object-defined error`.

## Description

Error 1004 is a catch-all for errors raised by the host application. In Excel, it commonly appears when trying to modify a protected worksheet, use an invalid range reference, or interact with a workbook or sheet that is unavailable. The exact meaning depends on the context and host application.

## Common Causes

- **Trying to modify a protected cell or worksheet** — writing to a cell in a sheet with protection enabled.
- **Invalid range reference** — using a malformed or nonexistent range address.
- **Method not applicable on a range** — calling a method on a Range that doesn't support that operation.
- **PasteSpecial or clipboard issues** — attempting to paste when the clipboard is empty or incompatible.

## How to Fix

### Fix 1: Unprotect the worksheet before modification

```vba
' Wrong — sheet is protected
Worksheets("Sheet1").Range("A1").Value = "Data"

' Correct — unprotect first (with password if required)
Worksheets("Sheet1").Unprotect "password"
Worksheets("Sheet1").Range("A1").Value = "Data"
Worksheets("Sheet1").Protect "password"
```

### Fix 2: Validate range references

```vba
' Wrong — invalid range name
Range("InvalidName!A1").Value = "Test"

' Correct — check if named range exists
On Error Resume Next
Dim rng As Range
Set rng = Range("ValidName")
On Error GoTo 0

If Not rng Is Nothing Then
    rng.Value = "Test"
Else
    MsgBox "Named range does not exist"
End If
```

### Fix 3: Use explicit workbook and worksheet references

```vba
' Wrong — ambiguous reference when multiple workbooks are open
Range("A1").Value = 42

' Correct — fully qualified reference
ThisWorkbook.Worksheets("Sheet1").Range("A1").Value = 42
```

### Fix 4: Clear clipboard before PasteSpecial

```vba
' Wrong — paste with empty clipboard
Selection.PasteSpecial Paste:=xlPasteValues

' Correct — copy first, then paste
Range("A1").Copy
Range("B1").PasteSpecial Paste:=xlPasteValues
Application.CutCopyMode = False
```

## Examples

```vba
Sub Example()
    ' Error 1004: trying to write to a protected sheet
    Worksheets("Sheet1").Protect
    Worksheets("Sheet1").Range("A1").Value = "Hello"  ' Runtime error 1004
    
    ' Error 1004: invalid range reference
    Range("A1:B:C").Select  ' Runtime error 1004
End Sub
```

## Related Errors

- [Object Required]({{< relref "/languages/vba/object-required" >}}) — object reference not set.
- [Application-defined Error]({{< relref "/languages/vba/application-defined" >}}) — general application-level error.
