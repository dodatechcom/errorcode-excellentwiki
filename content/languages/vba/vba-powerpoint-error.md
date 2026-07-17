---
title: "[Solution] VBA PowerPoint: presentation not found error"
description: "Fix VBA PowerPoint errors when presentations cannot be opened, found, or manipulated through COM automation."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

PowerPoint automation errors occur when VBA cannot locate or manipulate presentations through COM. Common issues include presentations not opening, slides not found, or COM connection failures.

## Common Causes

- PowerPoint not running
- Presentation file doesn't exist at path
- File path too long
- PowerPoint version incompatibility
- COM reference not set
- Presentation protected or encrypted

## How to Fix

```vba
' WRONG: No error handling
Sub Example1()
    Dim pptApp As Object
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Presentations.Open "C:\slides\presentation.pptx"  ' May fail
End Sub

' CORRECT: Proper error handling
Sub Example1()
    Dim pptApp As Object
    Dim pres As Object
    
    On Error GoTo ErrHandler
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Visible = True
    
    Dim filePath As String
    filePath = "C:\slides\presentation.pptx"
    
    If Dir(filePath) = "" Then
        MsgBox "File not found: " & filePath
        Exit Sub
    End If
    
    Set pres = pptApp.Presentations.Open(filePath)
    
    ' Work with presentation
    pres.SlideShowSettings.Run
    
    pres.Close
    pptApp.Quit
    
    Set pres = Nothing
    Set pptApp = Nothing
    Exit Sub
    
ErrHandler:
    MsgBox "Error: " & Err.Description
    If Not pres Is Nothing Then pres.Close
    If Not pptApp Is Nothing Then pptApp.Quit
End Sub
```

```vba
' CORRECT: Create new presentation
Sub Example2()
    Dim pptApp As Object
    Dim pres As Object
    Dim sld As Object
    
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Visible = True
    
    Set pres = pptApp.Presentations.Add
    
    ' Add slide
    Set sld = pres.Slides.Add(1, 1)  ' ppLayoutBlank = 1
    sld.Shapes(1).TextFrame.TextRange.Text = "Hello World"
    
    pres.SaveAs "C:\slides\new.pptx"
    pres.Close
    pptApp.Quit
End Sub
```

## Related Errors

- [Word Automation Error](vba-word-automation-error) - Word COM errors
- [Excel Automation Error](vba-excel-automation-error) - Excel COM errors
- [Shell Error](vba-shell-error) - process control
