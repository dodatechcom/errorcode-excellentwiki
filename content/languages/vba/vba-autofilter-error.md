---
title: "[Solution] VBA AutoFilter Error"
description: "AutoFilter errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA AutoFilter Error

AutoFilter errors.

### Common Causes
Wrong field; wrong criteria; not on range

### How to Fix
```vba
ws.Range("A1:D" & lastRow).AutoFilter Field:=1, Criteria1:="=Yes"
```

### Examples
```vba
ws.Range("A1:D" & lastRow).AutoFilter _
    Field:=2, _
    Criteria1:=">=100", _
    Operator:=xlAnd
```
