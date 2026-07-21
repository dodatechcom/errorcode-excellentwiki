---
title: "VBA Timer Event Callback Error Fix"
description: "Fix VBA Application.OnTime timer callback errors when scheduled procedures fail or conflict with workbook state."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Timer Event Callback Error Fix

Application.OnTime schedules procedures to run at specific times, but the callback can fail if the workbook is closed, the procedure name is wrong, or the scheduled time has already passed.

## Common Causes

- Workbook is closed before the OnTime callback fires
- Procedure name string does not match an existing Sub name
- Scheduling a callback with a past time
- Multiple OnTime callbacks interfering with each other
- OnTime callback raises its own error, creating unhandled cascade

## How to Fix

```vba
' Wrong -- procedure name does not exist
Application.OnTime Now + TimeValue("00:00:05"), "NonExistentSub"
' Error when timer fires

' Correct -- verify procedure exists
Application.OnTime Now + TimeValue("00:00:05"), "MyCallback"

Sub MyCallback()
    MsgBox "Timer fired!"
End Sub
```

```vba
' Wrong -- not cancelling old timer before setting new one
Sub StartTimer()
    Application.OnTime Now + TimeValue("00:01:00"), "DoWork"
End Sub
' Calling StartTimer multiple times creates multiple timers

' Correct -- cancel previous timer
Dim nextTime As Date
Sub StartTimer()
    If nextTime > 0 Then
        On Error Resume Next
        Application.OnTime nextTime, "DoWork", , False
        On Error GoTo 0
    End If
    nextTime = Now + TimeValue("00:01:00")
    Application.OnTime nextTime, "DoWork"
End Sub
```

## Examples

```vba
Sub Example1_SimpleTimer()
    Application.OnTime Now + TimeValue("00:00:10"), "TimerFired"
End Sub

Sub TimerFired()
    MsgBox "10 seconds have passed!"
End Sub

Sub Example2_RepeatingTimer()
    Dim nextRun As Date
    nextRun = Now + TimeValue("00:00:05")
    Application.OnTime nextRun, "RepeatTimer"
End Sub

Sub RepeatTimer()
    MsgBox "Tick"
    Example2_RepeatingTimer  ' schedule next tick
End Sub

Sub Example3_CancelTimer()
    On Error Resume Next
    Application.OnTime Now, "DoWork", , False
    On Error GoTo 0
End Sub
```

## Related Errors

- [Timer error](vba-timer-error) -- timer event conflicts
- [Shell error](vba-shell-error) -- external process timing
