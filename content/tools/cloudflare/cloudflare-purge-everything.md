---
title: "[Solution] Cloudflare Purge Everything Error"
description: "Fix Cloudflare purge everything errors. Resolve mass cache purge failures."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Purge Everything Error can prevent your application from working correctly.

## Common Causes

- API token lacks permissions
- Zone is paused
- API rate limit exceeded
- Account limits reached

## How to Fix

### Purge All

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything":true}'
```

### Via Dashboard

1. Go to Caching > Configuration
2. Click Purge Everything

