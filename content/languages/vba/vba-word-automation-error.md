---
title: "[Solution] VBA Word: automation error - document not saved"
description: "Fix VBA Word automation errors when Word documents fail to save, Word doesn't respond, or COM automation fails."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["word", "automation", "document", "save", "com", "vba"]
weight: 5
---

## What This Error Means

Word automation errors occur when VBA cannot properly control Microsoft Word through COM automation. Common issues include documents not saving, Word becoming unresponsive, or COM connection failures.

## Common Causes

- Word not running or crashed
- Document locked by another user
- File path too long or invalid
- Word template corruption
- COM reference not set correctly
- Word security settings blocking automation

## How to Fix

```vba
' WRONG: No error handling
Sub Example1()
    Dim wdApp As Object
    Set wdApp = CreateObject("Word.Application")
    Dim doc As Object
    Set doc = wdApp.Documents.Add
    doc.Content.Text = "Hello"
    doc.SaveAs "C:\data\report.docx"  ' May fail
    doc.Close
    wdApp.Quit
End Sub

' CORRECT: Proper error handling
Sub Example1()
    Dim wdApp As Object
    Dim doc As Object
    
    On Error GoTo ErrHandler
    Set wdApp = CreateObject("Word.Application")
    wdApp.Visible = True
    
    Set doc = wdApp.Documents.Add
    doc.Content.Text = "Hello"
    
    doc.SaveAs2 "C:\data\report.docx"
    doc.Close
    
    Set doc = Nothing
    wdApp.Quit
    Set wdApp = Nothing
    Exit Sub
    
ErrHandler:
    MsgBox "Error: " & Err.Description
    If Not doc Is Nothing Then doc.Close False
    If Not wdApp Is Nothing Then wdApp.Quit False
End Sub
```

```vba
' CORRECT: Check if Word is already running
Sub Example2()
    Dim wdApp As Object
    
    On Error Resume Next
    Set wdApp = GetObject(, "Word.Application")
    On Error GoTo 0
    
    If wdApp Is Nothing Then
        Set wdApp = CreateObject("Word.Application")
    End If
    
    ' Use wdApp
    wdApp.Quit
End Sub
```

```vba
' CORRECT: Save to safe path
Sub Example3()
    Dim savePath As String
    savePath = Environ("USERPROFILE") & "\Documents\report.docx"
    
    ' Validate path
    If Dir(savePath) <> "" Then
        Kill savePath
    End If
    
    ' Save document
    doc.SaveAs2 savePath
End Sub
```

## Related Errors

- [Excel Automation Error](vba-excel-automation-error) - Excel COM errors
- [Outlook Error](vba-outlook-error) - Outlook automation
- [Shell Error](vba-shell-error) - process control
