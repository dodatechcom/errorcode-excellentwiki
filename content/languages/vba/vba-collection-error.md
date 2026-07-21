---
title: "[Solution] VBA Collection Error"
description: "Collection operation errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Collection Error

Collection operation errors.

### Common Causes
Key not found; duplicate key; index out of range

### How to Fix
```vba
Dim col As Collection
Set col = New Collection
col.Add "item1", "key1"
Debug.Print col("key1")
```

### Examples
```vba
On Error Resume Next
Dim item As Variant
item = col("nonexistent")
If Err.Number <> 0 Then
    Debug.Print "Key not found"
End If
```
