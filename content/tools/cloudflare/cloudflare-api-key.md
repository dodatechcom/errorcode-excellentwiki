---
title: "[Solution] Cloudflare API Key Error"
description: "Fix Cloudflare API key errors. Resolve Global API key authentication issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare API Key Error can prevent your application from working correctly.

## Common Causes

- Key rotated or deleted
- Account password changed
- IP whitelist blocking access
- Key leaked and disabled

## How to Fix

### Generate New Key

1. Go to My Profile > API Tokens
2. Click View Global API Key

### Test

```bash
curl -X GET "https://api.cloudflare.com/client/v4/user" \
  -H "X-Auth-Email: your@email.com" \
  -H "X-Auth-Key: {global_api_key}"
```

### Migrate to Tokens

API tokens are preferred over Global API keys.

