---
title: "VBA Collection Key Not Found Error Fix"
description: "Fix VBA Collection key not found errors when accessing items with non-existent keys in VBA collections."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Collection Key Not Found Fix

When accessing a Collection item by key, VBA raises error 5 if the key does not exist. Unlike Dictionary objects, Collections cannot check for key existence without trapping the error.

## Common Causes

- Key string does not match the one used during Add operation
- Case mismatch in key strings (Collection keys are case-insensitive by default)
- Item was removed before the access attempt
- Key contains leading/trailing spaces
- Using wrong collection object

## How to Fix

```vba
' Wrong -- no key existence check
Dim coll As New Collection
coll.Add "Alice", "user1"
Dim val As String
val = coll("user2")  ' Error 5: key not found

' Correct -- wrap in error handler
Dim coll As New Collection
coll.Add "Alice", "user1"
On Error Resume Next
Dim val As String
val = coll("user2")
If Err.Number <> 0 Then
    val = "default"
    Err.Clear
End If
On Error GoTo 0
```

```vba
' Wrong -- key with extra space
coll.Add "value", " key"
Debug.Print coll("key")  ' Error: space in key

' Correct -- use exact key
Debug.Print coll(" key")
```

## Examples

```vba
Sub Example1_BasicCollection()
    Dim coll As New Collection
    coll.Add "Red", "color1"
    coll.Add "Green", "color2"
    coll.Add "Blue", "color3"
    Debug.Print coll("color2")  ' Green
End Sub

Sub Example2_IndexAccess()
    Dim coll As New Collection
    coll.Add "First"
    coll.Add "Second"
    Debug.Print coll(1)  ' First
    Debug.Print coll(2)  ' Second
End Sub

Sub Example3_Remove()
    Dim coll As New Collection
    coll.Add "A", "a"
    coll.Add "B", "b"
    coll.Remove "a"
    Debug.Print coll.Count  ' 1
End Sub
```

## Related Errors

- [Subscript out of range](vba-subscript-out-of-range) -- index-based access failure
- [Dictionary error](vba-dictionary-error) -- Dictionary alternative to Collection
