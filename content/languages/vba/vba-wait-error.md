---
title: "[Solution] VBA Wait Error"
description: "Wait and DoEvents errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Wait Error

Wait and DoEvents errors.

### Common Causes
Application.Wait wrong syntax; hanging

### How to Fix
```vba
Application.Wait Now + TimeValue("00:00:02")
```

### Examples
```vba
Dim endTime As Date
endTime = Now + TimeValue("00:00:01")
Do While Now < endTime
    DoEvents
Loop
```
