---
title: "[Solution] Netlify REST API Error"
description: "Fix Netlify REST API errors. Resolve REST API request issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify REST API Error can prevent your application from working correctly.

## Common Causes

- Endpoint not found
- Method not allowed
- Request body invalid
- Response format wrong

## How to Fix

### List Sites

```bash
curl -H "Authorization: Bearer {token}" https://api.netlify.com/api/v1/sites
```

