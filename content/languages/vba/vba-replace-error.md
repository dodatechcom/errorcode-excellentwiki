---
title: "VBA Replace Function Error Fix"
description: "Fix VBA Replace function errors when search string is empty or the function produces unexpected results."
languages: ["vba"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# VBA Replace Function Error Fix

The Replace function raises runtime error 5 when the search string is empty, or produces unexpected results when the comparison mode or start position parameters are incorrect.

## Common Causes

- Empty string passed as the search parameter (causes error 5)
- Start position exceeding string length
- Using vbBinaryCompare when case-insensitive match is needed
- Replacement string contains special characters not handled
- Replacing with empty string but expecting different behavior than removal

## How to Fix

```vba
' Wrong -- empty search string causes error 5
Dim result As String
result = Replace("hello world", "", "x")  ' Runtime error 5

' Correct -- validate input before replacing
Dim search As String
search = ""
If Len(search) > 0 Then
    result = Replace("hello world", search, "x")
Else
    result = "hello world"
End If
```

```vba
' Wrong -- case-sensitive when you need case-insensitive
Dim text As String
text = "Hello HELLO hello"
Dim result As String
result = Replace(text, "hello", "hi")  ' Only replaces lowercase

' Correct -- use vbTextCompare
result = Replace(text, "hello", "hi", , , vbTextCompare)
```

## Examples

```vba
Sub Example1_BasicReplace()
    Dim text As String
    text = "The quick brown fox"
    Debug.Print Replace(text, "quick", "slow")
    ' "The slow brown fox"
End Sub

Sub Example2_ReplaceAll()
    Dim text As String
    text = "aabbccaabbcc"
    Debug.Print Replace(text, "aa", "xx")
    ' "xxbbccxxbbcc"
End Sub

Sub Example3_CountReplace()
    Dim text As String
    text = "aaa"
    Debug.Print Replace(text, "a", "b", , 2)
    ' "aba" -- only replaces from position 2
End Sub
```

## Related Errors

- [String operations error](vba-syntax-error) -- general string handling
- [Runtime error 5](vba-runtime-error) -- invalid procedure call
