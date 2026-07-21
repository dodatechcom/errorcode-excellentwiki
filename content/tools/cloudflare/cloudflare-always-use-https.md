---
title: "[Solution] Cloudflare Always Use HTTPS Error"
description: "Fix Cloudflare always use HTTPS errors. Resolve redirect loops and HTTPS enforcement."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Always Use HTTPS Error can prevent your application from working correctly.

## Common Causes

- Origin also redirects HTTP to HTTPS causing loop
- SSL mode set to Flexible with origin redirect
- Page rules create conflicting redirects
- Mixed content warnings

## How to Fix

### Fix Redirect Loops

```bash
curl -v http://your-domain.com 2>&1 | grep "< HTTP"
```

### Set Full Strict

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/ssl" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"value":"strict"}'
```

