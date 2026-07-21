---
title: "VBA Select Case Fall Through Error Fix"
description: "Fix VBA Select Case errors when Case expressions overlap, fall through incorrectly, or use invalid syntax."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Select Case Fall Through Fix

Select Case errors occur when the Case expressions have overlapping ranges, use invalid syntax for multi-condition cases, or when the structure does not properly terminate.

## Common Causes

- Overlapping Case ranges that cause ambiguous matching
- Missing Case Else clause leading to unhandled values
- Using invalid syntax for multiple conditions in a single Case
- Forgetting End Select to close the block
- Case expressions with side effects that evaluate differently than expected

## How to Fix

```vba
' Wrong -- overlapping Case ranges
Select Case score
    Case Is >= 90
        grade = "A"
    Case Is >= 80
        grade = "B"
    Case Is >= 90  ' redundant, never reached
        grade = "A+"
End Select

' Correct -- remove overlap
Select Case score
    Case Is >= 90
        grade = "A"
    Case Is >= 80
        grade = "B"
    Case Else
        grade = "F"
End Select
```

```vba
' Wrong -- invalid multi-condition syntax
Select Case color
    Case "red" Or "blue"  ' syntax error
        action = "primary"
End Select

' Correct -- use comma for multiple values
Select Case color
    Case "red", "blue"
        action = "primary"
    Case "green", "yellow"
        action = "secondary"
End Select
```

## Examples

```vba
Sub Example1_GradeCalc(score As Integer)
    Dim grade As String
    Select Case score
        Case 90 To 100
            grade = "A"
        Case 80 To 89
            grade = "B"
        Case 70 To 79
            grade = "C"
        Case 60 To 69
            grade = "D"
        Case Else
            grade = "F"
    End Select
    Debug.Print grade
End Sub

Sub Example2_StringMatch(input As String)
    Select Case LCase(input)
        Case "yes", "y", "true"
            Debug.Print "Affirmative"
        Case "no", "n", "false"
            Debug.Print "Negative"
        Case Else
            Debug.Print "Unknown"
    End Select
End Sub
```

## Related Errors

- [If Then Else error](vba-if-then-else-error) -- conditional branching issues
- [Runtime error](vba-runtime-error) -- general runtime failures
