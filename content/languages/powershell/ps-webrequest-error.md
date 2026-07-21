---
title: "[Solution] Web Request Error"
description: "HTTP requests fail with various errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Web Request Error

HTTP requests fail with various errors.

### Common Causes
Connection timeout; auth required; rate limiting

### How to Fix
```powershell
Invoke-WebRequest -Uri "https://example.com" -TimeoutSec 30
```

### Examples
```powershell
Invoke-RestMethod -Uri "https://api.example.com/data" -Headers @{"Authorization"="Bearer $token"}
```
