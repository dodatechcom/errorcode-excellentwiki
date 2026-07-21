---
title: "[Solution] VBA ListBox Error"
description: "ListBox errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA ListBox Error

ListBox errors.

### Common Causes
No items; wrong selection; multi-select issues

### How to Fix
```vba
ListBox1.AddItem "Item 1"
ListBox1.AddItem "Item 2"
Debug.Print ListBox1.Value
```

### Examples
```vba
Dim i As Long
For i = 0 To ListBox1.ListCount - 1
    If ListBox1.Selected(i) Then
        Debug.Print ListBox1.List(i)
    End If
Next i
```
