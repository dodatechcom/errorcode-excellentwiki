---
title: "VBA Class Module Initialize Terminate Fix"
description: "Fix VBA Class_Initialize and Class_Terminate errors when class lifecycle events fail or have incorrect syntax."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Class Module Initialize Terminate Fix

Class_Initialize runs when an object is created (New keyword) and Class_Terminate when the object goes out of scope. Errors in these events can prevent object creation or cause silent failures.

## Common Causes

- Class_Initialize raises an error, preventing object creation
- Accessing Nothing references in Class_Terminate
- Circular references where two objects hold Set references to each other
- Forgetting that Set Nothing triggers Class_Terminate
- Class_Terminate takes too long, blocking memory cleanup

## How to Fix

```vba
' Wrong -- error in Class_Initialize prevents creation
Private Sub Class_Initialize()
    Set conn = New ADODB.Connection
    conn.Open "invalid connection string"  ' error here
    ' object creation fails
End Sub

' Correct -- handle errors gracefully
Private Sub Class_Initialize()
    On Error GoTo Cleanup
    Set conn = New ADODB.Connection
    conn.Open GetConnectionString()
    Exit Sub
Cleanup:
    Debug.Print "Connection failed: " & Err.Description
    Set conn = Nothing
End Sub
```

```vba
' Wrong -- not checking for Nothing in Terminate
Private Sub Class_Terminate()
    conn.Close  ' Error if conn is Nothing
End Sub

' Correct -- safe cleanup
Private Sub Class_Terminate()
    If Not conn Is Nothing Then
        If conn.State = adStateOpen Then conn.Close
        Set conn = Nothing
    End If
End Sub
```

## Examples

```vba
' Class: clsDatabase
Private conn As Object
Private isOpen As Boolean

Private Sub Class_Initialize()
    isOpen = False
    Debug.Print "Database object created"
End Sub

Private Sub Class_Terminate()
    If isOpen Then
        conn.Close
        Set conn = Nothing
    End If
    Debug.Print "Database object destroyed"
End Sub

Public Function Connect(connectionString As String) As Boolean
    On Error GoTo Fail
    Set conn = CreateObject("ADODB.Connection")
    conn.Open connectionString
    isOpen = True
    Connect = True
    Exit Function
Fail:
    Connect = False
End Function

' Usage:
Sub Example()
    Dim db As clsDatabase
    Set db = New clsDatabase  ' triggers Class_Initialize
    db.Connect "Provider=..."
    Set db = Nothing  ' triggers Class_Terminate
End Sub
```

## Related Errors

- [Compile error argument](vba-compile-error-argument) -- parameter issues
- [Object required](vba-object-required) -- missing object references
