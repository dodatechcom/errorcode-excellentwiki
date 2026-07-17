---
title: "[Solution] VBA Object Variable Not Set"
description: "Fix VBA Object Variable Not Set error (Error 91) when using an object variable that hasn't been initialized with Set."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["object-variable", "not-set", "error-91", "nothing", "vba"]
weight: 5
---

## What This Error Means

Object Variable Not Set (Error 91) occurs when you try to use an object variable that has never been assigned an object reference, or that was explicitly set to `Nothing`.

## Common Causes

- Object variable declared but never assigned
- Set statement was omitted
- Object was set to Nothing
- Failed object lookup returned Nothing

## How to Fix

```vba
' WRONG: Variable not set
Dim rng As Range
rng.Value = 1   ' Error 91

' CORRECT: Assign before use
Dim rng As Range
Set rng = Range("A1")
rng.Value = 1
```

```vba
' WRONG: Not checking after lookup
Dim ws As Worksheet
Set ws = Nothing
ws.Activate   ' Error 91

' CORRECT: Always check
If Not ws Is Nothing Then
    ws.Activate
Else
    MsgBox "Worksheet not found"
End If
```

## Examples

```vba
Sub Example()
    Dim c As Object
    ' c is Nothing - not set to any object
    c.Name   ' Error 91: Object variable not set
End Sub
```

## Related Errors

- [Object Required](vba-object-required) - missing Set keyword
- [Runtime Error](vba-runtime-error) - general execution errors
