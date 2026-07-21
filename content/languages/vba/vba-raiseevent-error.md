---
title: "VBA RaiseEvent Without Event Declaration Fix"
description: "Fix VBA RaiseEvent errors when firing events that are not properly declared with the Event keyword."
languages: ["vba"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# VBA RaiseEvent Without Event Declaration Fix

RaiseEvent fails with compile error if the event name was not declared using the `Event` keyword in the class module, or if the calling code is not using `WithEvents` to handle the event.

## Common Causes

- Missing `Event` declaration in the class module
- Using RaiseEvent with a misspelled event name
- Calling RaiseEvent from outside the declaring class
- Forgetting `WithEvents` in the handler module
- Event declared as Private but raised from a different module

## How to Fix

```vba
' Wrong -- no Event declaration in class
' Class: clsProcessor
Public Sub Process()
    RaiseEvent Complete  ' Compile error: event not declared
End Sub

' Correct -- declare the event
' Class: clsProcessor
Public Event Complete()

Public Sub Process()
    ' do work
    RaiseEvent Complete
End Sub
```

```vba
' Wrong -- WithEvents missing in handler
' Module:
Dim processor As New clsProcessor
Private Sub processor_Complete()  ' never fires
End Sub

' Correct -- declare WithEvents
Dim WithEvents processor As clsProcessor

Private Sub processor_Complete()
    MsgBox "Done!"
End Sub
```

## Examples

```vba
' Class: clsWorker
Public Event Progress(percent As Integer)
Public Event Finished(result As String)

Public Sub DoWork()
    Dim i As Integer
    For i = 1 To 100
        RaiseEvent Progress(i)
    Next i
    RaiseEvent Finished("Complete")
End Sub

' Module:
Dim WithEvents worker As clsWorker

Private Sub worker_Progress(percent As Integer)
    Debug.Print "Progress: " & percent & "%"
End Sub

Private Sub worker_Finished(result As String)
    Debug.Print "Result: " & result
End Sub
```

## Related Errors

- [Event handler error](vba-event-handler-error) -- event wiring problems
- [Class module error](vba-compile-error) -- class module structure issues
