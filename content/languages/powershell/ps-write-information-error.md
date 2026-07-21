---
title: "[Solution] Write-Information Error"
description: "Write-Information not visible."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Write-Information Error

Write-Information not visible.

### Common Causes
InformationPreference set to SilentlyContinue

### How to Fix
```powershell
$InformationPreference = "Continue"
Write-Information "Processing"
```

### Examples
```powershell
Write-Information -MessageData "Starting analysis" -InformationAction Continue
```
