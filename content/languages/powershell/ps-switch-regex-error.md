---
title: "[Solution] Switch Regex Error"
description: "Switch -regex errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Switch Regex Error

Switch -regex errors.

### Common Causes
Wrong pattern; case sensitivity

### How to Fix
```powershell
switch -regex ($input) { "^test" { "matches" } }
```

### Examples
```powershell
switch -regex ($input) { "^[0-9]+$" { "number" } default { "other" } }
```
