---
title: "[Solution] Invoke-RestMethod Error"
description: "Invoke-RestMethod fails with API calls."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Invoke-RestMethod Error

Invoke-RestMethod fails with API calls.

### Common Causes
Wrong URL; auth needed; SSL issues

### How to Fix
```powershell
Invoke-RestMethod -Uri "https://api.example.com/data"
```

### Examples
```powershell
Invoke-RestMethod -Uri "https://api.example.com/data" -Method Post -Body $json -ContentType "application/json"
```
