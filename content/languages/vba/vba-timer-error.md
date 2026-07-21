---
title: "[Solution] VBA Timer Error"
description: "Timer function errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Timer Error

Timer function errors.

### Common Causes
Application.OnTime scheduling; cancellation

### How to Fix
```vba
Application.OnTime Now + TimeValue("00:00:05"), "MyMacro"
```

### Examples
```vba
Dim nextTime As Date
nextTime = Now + TimeValue("00:01:00")
Application.OnTime nextTime, "MyMacro"
' Cancel:
Application.OnTime nextTime, "MyMacro", , False
```
