---
title: "VBA DoEvents Loop Hang Fix"
description: "Fix VBA DoEvents issues in loops where infinite execution causes application to freeze or become unresponsive."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA DoEvents Loop Hang Fix

DoEvents yields control to the operating system but can cause infinite loops if the loop condition never becomes false, or if events triggered by DoEvents modify the state being checked.

## Common Causes

- Loop condition depends on a variable modified by event handlers during DoEvents
- Timer events fire during DoEvents and change application state
- User closes a window during the loop, invalidating object references
- No exit condition or exit condition is unreachable
- DoEvents in a tight loop with no yield mechanism

## How to Fix

```vba
' Wrong -- DoEvents causes infinite loop
Dim counter As Long
Do
    DoEvents
    ' no increment or exit condition
Loop Until counter > 100  ' counter never changes

' Correct -- ensure loop progresses
Dim counter As Long
counter = 0
Do
    DoEvents
    counter = counter + 1
Loop Until counter > 100
```

```vba
' Wrong -- user closes workbook during loop
Dim ws As Worksheet
Do
    DoEvents
    ' user may close workbook here
    ws.Range("A1").Value = "test"  ' Error if ws is gone
Loop

' Correct -- validate object each iteration
Dim ws As Worksheet
Set ws = ActiveSheet
Do
    DoEvents
    If ws Is Nothing Then Exit Do
    If Not ws.Parent Is ActiveWorkbook Then Exit Do
    ws.Range("A1").Value = "test"
Loop
```

## Examples

```vba
Sub Example1_ControlledLoop()
    Dim i As Long: i = 0
    Do While i < 1000
        DoEvents
        Cells(1, 1).Value = i
        i = i + 1
    Loop
End Sub

Sub Example2_CancellableLoop()
    Dim running As Boolean: running = True
    Dim i As Long: i = 0
    Do While running And i < 10000
        DoEvents
        If Application.StatusBar = False Then running = False
        i = i + 1
    Loop
    Application.StatusBar = False
End Sub

Sub Example3_TimerSafe()
    Dim startTime As Double: startTime = Timer
    Do
        DoEvents
        If Timer - startTime > 30 Then Exit Do  ' 30s timeout
        ' process work
    Loop
End Sub
```

## Related Errors

- [While Wend error](vba-while-wend-error) -- loop structure issues
- [Timer error](vba-timer-error) -- timer event conflicts
