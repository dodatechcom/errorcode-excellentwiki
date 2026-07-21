---
title: "[Solution] VBA Sort Error"
description: "Sort method errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Sort Error

Sort method errors.

### Common Causes
Wrong range; missing key; wrong order

### How to Fix
```vba
ws.Range("A1:D" & lastRow).Sort Key1:=ws.Range("A1"), Order1:=xlAscending
```

### Examples
```vba
With ws.Sort
    .SortFields.Clear
    .SortFields.Add Key:=ws.Range("A1:A" & lastRow)
    .SetRange ws.Range("A1:D" & lastRow)
    .Orientation = xlTopToBottom
    .Apply
End With
```
