---
title: "[Solution] Switch Statement Error"
description: "Switch statement syntax errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Switch Statement Error

Switch statement syntax errors.

### Common Causes
Missing script block; wrong comparison

### How to Fix
```powershell
switch ($value) { 1 { "one" } 2 { "two" } default { "other" } }
```

### Examples
```powershell
switch -regex ($input) { "^hello" { "greeting" } "^[0-9]+" { "number" } }
```
