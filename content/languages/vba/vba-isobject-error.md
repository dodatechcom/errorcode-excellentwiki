---
title: "VBA IsObject Check Error Fix"
description: "Fix VBA IsObject misuse when testing for object existence and handling Nothing references."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA IsObject Check Error Fix

IsObject returns True even when the variable contains Nothing, leading to runtime errors when you attempt to access properties on a Nothing reference. The correct approach is to check for Nothing explicitly.

## Common Causes

- Using IsObject to check if an object exists (it checks type, not existence)
- Assuming IsObject returns False when variable is Nothing
- Not differentiating between Nothing and a valid object reference
- IsObject on a Variant containing Nothing returns True
- Forgetting that IsObject returns True for any object type

## How to Fix

```vba
' Wrong -- IsObject returns True even for Nothing
Dim ws As Worksheet
Set ws = Nothing
If IsObject(ws) Then
    ws.Name = "test"  ' Runtime error 91
End If

' Correct -- check for Nothing explicitly
Dim ws As Worksheet
Set ws = Nothing
If Not ws Is Nothing Then
    ws.Name = "test"
End If
```

```vba
' Wrong -- trusting IsObject on Variant
Dim v As Variant
Set v = Nothing
If IsObject(v) And Not v Is Nothing Then  ' this works but is confusing
    Debug.Print v.Name
End If

' Correct -- just check Nothing
Dim v As Variant
Set v = Nothing
If Not v Is Nothing Then
    Debug.Print v.Name
End If
```

## Examples

```vba
Sub Example1_CheckNothing()
    Dim obj As Object
    Set obj = Nothing
    If obj Is Nothing Then
        Debug.Print "Object is Nothing"
    End If
End Sub

Sub Example2_SafeAccess()
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = ThisWorkbook.Sheets("Data")
    On Error GoTo 0
    If Not ws Is Nothing Then
        ws.Range("A1").Value = "Found"
    Else
        Debug.Print "Sheet not found"
    End If
End Sub

Sub Example3_CollectionAccess()
    Dim coll As Collection
    Dim item As Variant
    On Error Resume Next
    Set item = coll("key")
    On Error GoTo 0
    If Not item Is Nothing Then
        Debug.Print item
    End If
End Sub
```

## Related Errors

- [Object required error](vba-object-required) -- Nothing reference usage
- [Object not set](vba-object-not-set-v2) -- unset object variables
