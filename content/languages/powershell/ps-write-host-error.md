---
title: "[Solution] Write-Host Error"
description: "Write-Host output not captured or formatted."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Write-Host Error

Write-Host output not captured or formatted.

### Common Causes
Color issues; not pipelineable

### How to Fix
```powershell
Write-Host "Processing..." -ForegroundColor Green
```

### Examples
```powershell
Write-Host "Error occurred" -ForegroundColor Red -BackgroundColor Black
```
