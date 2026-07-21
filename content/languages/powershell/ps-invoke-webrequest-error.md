---
title: "[Solution] Invoke-WebRequest Error"
description: "Invoke-WebRequest fails to fetch web content."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Invoke-WebRequest Error

Invoke-WebRequest fails to fetch web content.

### Common Causes
Wrong URL; SSL issues; proxy needed

### How to Fix
```powershell
Invoke-WebRequest -Uri "https://example.com"
```

### Examples
```powershell
$response = Invoke-WebRequest -Uri "https://example.com" -UseBasicParsing
$response.Content
```
