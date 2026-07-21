---
title: "[Solution] Netlify API Error"
description: "Fix Netlify API errors. Resolve API request issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify API Error can prevent your application from working correctly.

## Common Causes

- API endpoint not found
- Authentication failed
- Rate limit exceeded
- Request malformed

## How to Fix

### Test API

```bash
curl -H "Authorization: Bearer {token}" https://api.netlify.com/api/v1/sites
```

