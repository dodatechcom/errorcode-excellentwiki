---
title: "[Solution] VBA SendKeys Error"
description: "SendKeys errors."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA SendKeys Error

SendKeys errors.

### Common Causes
Wrong keys; timing issues; modal dialogs

### How to Fix
```vba
Application.SendKeys "{ENTER}"
```

### Examples
```vba
Application.SendKeys "^s"  ' Ctrl+S
```
