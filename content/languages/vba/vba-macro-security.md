---
title: "[Solution] VBA Macro Security"
description: "Macro security settings blocking code."
languages: ["vba"]
error-types: ["language-error"]
severities: ["error"]
---

# VBA Macro Security

Macro security settings blocking code.

### Common Causes
Security level too high; not signed

### How to Fix
```vba
' File > Options > Trust Center > Macro Settings
' Or sign with digital certificate
```

### Examples
```vba
' Save as .xlsm (macro-enabled)
' Trust location: add folder to trusted locations
```
