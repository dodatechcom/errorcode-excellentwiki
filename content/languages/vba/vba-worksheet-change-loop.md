---
title: "VBA Worksheet_Change Event Infinite Loop Fix"
description: "Fix VBA Worksheet_Change event infinite loops when code modifies cells that trigger the event recursively."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Worksheet_Change Event Infinite Loop Fix

Worksheet_Change events fire whenever a cell is modified. If the event handler itself modifies cells, it triggers the event again, creating an infinite recursion that hangs Excel.

## Common Causes

- Event handler writes to cells on the same sheet without disabling events
- Using Range.Value assignment inside the Change handler
- Format changes via Interior.Color or NumberFormat trigger re-entry
- Multiple event handlers on different sheets calling each other
- Not using EnableEvents = False before modifying cells in handler

## How to Fix

```vba
' Wrong -- modifying cells triggers recursive call
Private Sub Worksheet_Change(ByVal Target As Range)
    Target.Offset(0, 1).Value = "Updated"  ' triggers event again
End Sub

' Correct -- disable events during modification
Private Sub Worksheet_Change(ByVal Target As Range)
    Application.EnableEvents = False
    Target.Offset(0, 1).Value = "Updated"
    Application.EnableEvents = True
End Sub
```

```vba
' Wrong -- no error handling if something fails mid-handler
Private Sub Worksheet_Change(ByVal Target As Range)
    Application.EnableEvents = False
    ' if error occurs here, events stay disabled
    Target.Offset(0, 1).Value = "test"
    Application.EnableEvents = True  ' never reached on error
End Sub

' Correct -- use error handler to re-enable events
Private Sub Worksheet_Change(ByVal Target As Range)
    On Error GoTo Cleanup
    Application.EnableEvents = False
    Target.Offset(0, 1).Value = "Updated"
Cleanup:
    Application.EnableEvents = True
    If Err.Number <> 0 Then Resume Next
End Sub
```

## Examples

```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    On Error GoTo Cleanup
    Application.EnableEvents = False
    
    ' Auto-fill timestamp in column B when column A changes
    If Not Intersect(Target, Me.Columns(1)) Is Nothing Then
        If Target.Value <> "" Then
            Target.Offset(0, 1).Value = Now
        Else
            Target.Offset(0, 1).ClearContents
        End If
    End If

Cleanup:
    Application.EnableEvents = True
    If Err.Number <> 0 Then Resume Next
End Sub

Private Sub Worksheet_Change(ByVal Target As Range)
    On Error GoTo Cleanup
    Application.EnableEvents = False
    
    ' Capitalize all text in changed cells
    Dim cell As Range
    For Each cell In Intersect(Target, Me.UsedRange)
        If VarType(cell.Value) = vbString Then
            cell.Value = StrConv(cell.Value, vbUpperCase)
        End If
    Next cell

Cleanup:
    Application.EnableEvents = True
    If Err.Number <> 0 Then Resume Next
End Sub
```

## Related Errors

- [Event handler error](vba-event-handler-error) -- event wiring issues
- [DoEvents error](vba-doevents-loop-error) -- loop and event conflicts
